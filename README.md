# Django
การใช้งาน-Django การสร้างเว็บไซต๋
 Django

ติดตั้ง virtualenv
pip install virtualenv
python3 -m pip install virtualenv

 environment
virtualenv venv
python3 -m virtualenv venv

Activate
.\venv\scripts\activate  // windows
source ./venv/bin/activate # for mac

ติดตั้ง  django
pip install django==3.2
pip3 install django==3.2

  � djangoschool �
django-admin startproject djangoschool

cd djangoschool ���� �ѹ server ������� localhost:8000
python manage.py runserver

����觷����㹡�����ҧ�ҹ�����Ţͧ admin �����á
python manage.py migrate

--------------------------------
���ҧ user �ͧ admin

***************************************
for windows
python -m virtualenv
python -m virtualenv venv
.\venv\scripts\activate

หลังจากสร้าง models เสร็จให้รัน 2 คำสั่งที่สำคัญคือ
python manage.py makemigrations
python manage.pt migrate

