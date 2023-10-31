# django

1. 프로젝트 생성
```
django-admin startproject <pjtname> .
```

2. 가상환경 설정
> 가상환경?    
```
python -m venv venv
```

3. 가상환경 활성화/비활성화
```
활성화
<!-- window -->
source venv/Scripts/activate
<!-- macOS -->
source venv/bin/activate

비활성화
deactivate
```

4. 가상환경 내부에 django 설치
```
pip install django
```

5. 서버 실행 확인(종료 `ctrl + c`)
```
python manage.py runserver
```

6. 앱생성
```
django-admin startapp <appname>
> migrations폴더 생성
```
프로젝트/앱 생성할 때만 django-admin ~
다른때는 python ~

7. 앱등록
- `settings.py`의 `INSTALLED_APPS`에 등록
    `<appname>`을 등록 
    > '' 사이에 작성
```

```

8. `urls.py` 수정 (u
rl~ 길잡이, 이정표)
```
from django.urls import path
<!-- views 모듈 불러오기 -->
from app_intro import views 

<!-- urlpatterns에 path('index/', vi
