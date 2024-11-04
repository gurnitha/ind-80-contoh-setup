# ind-80-contoh-setup
Membuat contoh setup untuk setiap proyek Django
Github: https://github.com/gurnitha/ind-80-contoh-setup


## 1. SETUP

#### 0. Menentukan lokasi proyek

#### 1. Membuat remote repositori

#### 2. Menklon remote repositori

#### 3. Membuat lingkungan virtual

#### 4. Mengaktifkan lingkungan virtual

#### 5. Menonaktifkan lingkungan virtual

#### 6. Menginstal Django

#### 7. Memverifikasi versi Django yang telah diinstal

#### 8. Meningkatkan versi pip


## 2. PROYEK DJANGO

#### 1. Menginisiasi proyek Django

	(venv312512) λ django-admin startproject config

	C:\Users\ING\Desktop\workspace\ind-80-contoh-setup(main -> origin)
	(venv312512) λ ls
	config/  README.md  venv312512/

	        modified:   README.md
	        new file:   config/config/__init__.py
	        new file:   config/config/asgi.py
	        new file:   config/config/settings.py
	        new file:   config/config/urls.py
	        new file:   config/config/wsgi.py
	        new file:   config/manage.py

#### 2. Memodifikasi struktur proyek Django

        modified:   README.md
        renamed:    config/config/__init__.py -> src/config/__init__.py
        renamed:    config/config/asgi.py -> src/config/asgi.py
        renamed:    config/config/settings.py -> src/config/settings.py
        renamed:    config/config/urls.py -> src/config/urls.py
        renamed:    config/config/wsgi.py -> src/config/wsgi.py
        renamed:    config/manage.py -> src/manage.py


## 3. MENSETING PROYEK

#### 1. Menseting bahasa dan waktu

        modified:   README.md
        modified:   src/config/settings.py

#### 2. Menseting path untuk templates

	(venv312512) λ mkdir templates

	(venv312512) λ python manage.py check
	C:\Users\ING\Desktop\workspace\ind-80-contoh-setup\src\config\settings.py
	C:\Users\ING\Desktop\workspace\ind-80-contoh-setup\src\config
	C:\Users\ING\Desktop\workspace\ind-80-contoh-setup\src
	System check identified no issues (0 silenced).

        modified:   README.md
        modified:   config/settings.py

#### 3. Menseting path untuk file statis

	(venv312512) λ mkdir static

	(venv312512) λ python manage.py check
	System check identified no issues (0 silenced).

#### 4. Menseting path untuk file media

	# config/urls.py

	# Modul Django
	from django.contrib import admin
	from django.urls import path
	from django.conf import settings
	from django.conf.urls.static import static

	urlpatterns = [
	    path('admin/', admin.site.urls),
	]

	if settings.DEBUG:
	    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

	(venv312512) λ python manage.py check
	System check identified no issues (0 silenced).


## 4. DATABASE

#### 1. Membuat MySQL database

	E:\_WORKSPACE\laragon\www
	λ mysql -u root
	Welcome to the MySQL monitor.  Commands end with ; or \g.
	Your MySQL connection id is 8
	Server version: 8.0.30 MySQL Community Server - GPL

	Copyright (c) 2000, 2022, Oracle and/or its affiliates.

	Oracle is a registered trademark of Oracle Corporation and/or its
	affiliates. Other names may be trademarks of their respective
	owners.

	Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

	mysql> 

	mysql> CREATE DATABASE ind_80_dj5_torangbisaapa;
	Query OK, 1 row affected (1.44 sec)

	mysql> show databases;
	+---------------------------------------------------------+
	| Database                                                |
	+---------------------------------------------------------+
	| ind_80_dj5_torangbisaapa                                |
	+---------------------------------------------------------+

#### 2. Menghubungan proyek dengan database

	DATABASES = {
	    'default': {
	    'ENGINE': 'django.db.backends.mysql',
	    'NAME': 'ind_80_dj5_torangbisaapa',
	    'USER': 'root',
	    'PASSWORD': '',
	    'HOST':'localhost',
	    'PORT':'3306',
	    }
	}

        modified:   README.md
        modified:   config/settings.py

#### 3. Menginstal mysqlclient

	(venv312512) λ pip install mysqlclient

#### 4. Melindungi File penting

        new file:   .env.example
        modified:   README.md
        modified:   config/settings.py

#### 5. Mengganti database dengan PostgreSQL database

        modified:   README.md
        modified:   config/settings.py