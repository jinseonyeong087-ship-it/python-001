# Python 기초 명령어


## 파이썬 실행 & 환경 (window)
python --version → 설치된 파이썬 버전 확인

python → 인터프리터(대화형 모드) 실행

python 파일이름.py → 지정한 파이썬 파일 실행

pip list → 설치된 라이브러리 목록 보기

pip install 패키지명 → 외부 라이브러리 설치

pip freeze > requirements.txt → 현재 환경의 패키지 목록 저장

## 사용할 python 지정 및 env 만드는 명령
- 가상환경(venv) 만들기
python -m venv venv

- 가상환경 활성화
Windows (PowerShell): venv\Scripts\activate  

## 패키지 설치 & 저장
- 패키지 설치: pip install fastapi uvicorn
- 라이브러리 목록보기: pip list
- 현재 환경 라이브러리 저장: pip freeze > requirements.txt

## python 실행
cd 파일명
python 파일명.py

## 가상환경 비활성화
작업 끝나면: deactivate

## http 서버 실행 (FastAPI 사용)
uvicorn app(파일명):app --reload   

### FastAPI란?
- Python 3.7+ 에서 사용할 수 있는 고성능 웹 프레임워크
- 데이터 검증과 자동 문서화 지원
