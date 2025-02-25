# Todo

## 목차

- [배포 주소](#배포-주소)
- [화면](#화면)
- [프로젝트 정보](#프로젝트-정보)
- [시작 가이드](#시작-가이드)
- [주요 기능](#주요-기능)
- [개발환경](#개발환경)

## 배포 주소

- http://localhost:8000(로컬배포)

## 화면

![image](https://github.com/SmartInsideAI/DEMO_DJANGO_NY/assets/169418219/76b1e63c-dcf5-4d9f-b9d8-3e6e2e3eb737)

## 프로젝트 정보

### Todo 프로젝트

Django를 기반으로 websocket과 redis, celery를 사용해보는 데모 프로젝트

## 시작 가이드

### Requirements

```
+ Docker Desktop 실행 (다운: https://docs.docker.com/desktop)
```

### 실행 방법

```
1. 도커 실행
   docker-compose up -d (V1.13.0 부턴 docker compose up -d)
2. web 접속
   http://localhost:8000
3. 계정 생성
   python manage.py createsuperuser  
4. 정적 파일 모음
   python manage.py collectstatic
```

## 주요 기능

+ 설정한 날짜 기준으로 반복 설정된 주기에 따라 task 생성(데이터 자동 삽입)
+ 새로 생성된 task 알림 보내기(DB 변동 알람)

## 개발환경

+ 사용언어: ![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
+ 사용 웹 프레임 워크: ![Django Badge](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=fff&style=for-the-badge)
+ 데이터 베이스: ![MySQL Badge](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=fff&style=for-the-badge)
+ 운영체제: ![Windows Badge](https://img.shields.io/badge/Windows-0078D4?logo=windows&logoColor=fff&style=for-the-badge)
+ IDE:![PyCharm Badge](https://img.shields.io/badge/PyCharm-000?logo=pycharm&logoColor=fff&style=for-the-badge)