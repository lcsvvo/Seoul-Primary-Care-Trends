# Notebooks

[01_clinic_composition.ipynb](01_clinic_composition.ipynb)는 원본 분석의 전처리와 EDA를 담은 실행 진입점.

1. [Data](../data/README.md)에 따라 17개 Excel 배치. 보조 분석에는 전국 인구, 종별 기관 수, 서울 인구와 소아의료 입력 추가.
2. Python 환경에서 `python -m pip install -r requirements.txt` 실행.
3. 저장소 루트에서 `python -m jupyter notebook notebooks/01_clinic_composition.ipynb` 실행 후 모든 셀을 순서대로 실행.
4. 저장소 루트에서 `python src/verify_results.py` 실행해 산출물과 핵심 집계 대조.

원본 Excel은 읽기 전용 입력. 실행하면 로컬 `data/processed/`와 `results/EDA/`에 표와 그림 생성. 한글 글꼴은 맑은 고딕, Apple SD Gothic Neo 또는 나눔고딕 사용. 배포 Notebook의 실행 출력은 비워둠. [실행과 대조 기록](../docs/validation.md)
