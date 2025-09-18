# Python 활용해서 pdf 파일 생성


## 파이썬 실행 & 환경
python --version → 설치된 파이썬 버전 확인

python → 인터프리터(대화형 모드) 실행

python 파일이름.py → 지정한 파이썬 파일 실행

pip list → 설치된 라이브러리 목록 보기

pip install 패키지명 → 외부 라이브러리 설치

pip freeze > requirements.txt → 현재 환경의 패키지 목록 저장

## 사용할 python 지정 및 env 만드는 명령

c:\Python310\python -m venv venv
c:\Python313\python -m venv venv2
venv\Scripts\activate


## http 서버 실행 (FastAPI 사용)
uvicorn app(파일명):app --reload   

## 라이브러리 목록 보기

pip list 
pip freeze > requirements.txt
