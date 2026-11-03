"""Cross-check published results against the reconstructed clinic panel."""
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "results/EDA/tables"
PANEL = ROOT / "data/processed/의원_표시과목_시군구_long.csv"
START, END = "2022Q2", "2026Q2"
CORE = ["내과", "소아청소년과", "가정의학과"]


def main():
    panel = pd.read_csv(PANEL)
    key = ["분기", "시도", "시군구", "표시과목"]
    assert not panel.duplicated(key).any()
    assert panel["분기"].nunique() == 17
    assert panel["시도"].nunique() == 17
    seoul = panel.loc[panel["시도"].eq("서울특별시")]
    assert seoul["시군구"].nunique() == 25
    totals = seoul.groupby(["분기", "시군구"])["기관수"].sum()
    core = seoul.loc[seoul["표시과목"].isin(CORE)]
    counts = core.groupby(["분기", "시군구"])["기관수"].sum()
    share = (100 * counts / totals).unstack("분기")
    stored = pd.read_csv(TABLES / "서울자치구_핵심과비중.csv").set_index("시군구")
    share = share.loc[stored.index]
    np.testing.assert_allclose(share[[START, END]], stored[[START, END]], atol=0.005)
    change = share[END] - share[START]
    np.testing.assert_allclose(change, stored["변화(%p)"], atol=0.005)
    assert (int((change < 0).sum()), int((change > 0).sum())) == (20, 5)
    assert tuple(totals.groupby(level=0).sum().loc[[START, END]]) == (9359, 10634)
    assert tuple(counts.groupby(level=0).sum().loc[[START, END]]) == (1854, 1987)
    print("Clinic panel and published district results agree.")


if __name__ == "__main__":
    main()
