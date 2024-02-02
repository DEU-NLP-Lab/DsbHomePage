# DsbHomePage
디지털스마트부산 동의대학교 홈페이지

db.sqlite3 파일이 .gitignore에 등록되어 올라가지 않았음

## 세팅

### 1. github Repository clone
```git clone https://github.com/915-Lab/DsbHomePage.git```

### 2. 방화벽 세팅
방화벽 포트 9091 오픈하기

### 3. clone 받은 곳으로 경로 이동
DsbHomePage\homePage까지 가면 manage.py가 있음

### 파이썬 관련 세팅
python version : 3.10.11
```
pip install django==4.2.9
pip install pillow==10.2.0
```
1. ```python manage.py makemigrations```
2. ```python manage.py migrate```
3. ```python manage.py runserver```   

## 실행
```python manage.py runserver 0.0.0.0:9091```