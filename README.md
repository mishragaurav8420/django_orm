# django_orm
create virtual env-->
               python -m venv venv


Activate virtual env-->

             .\venv\Scripts\activate
extension vs code-->
django
python
sqlite
docker

PIP->python pakage index(package manager for python)
PyPi--> python pakage repository
pip install .....//install
pip uninstall ...//uninstall
pip list  //list of all install pakage
pip freeze > requirements.txt



install Django
pip install django
then 
pip freeze > requirements.txt


new django project 
django-admin startproject core .  ->.(current working folder)
new app
python manage.py startapp newapp


start django server-->
python manage.py runserver
127.0.0.1 ->Ip address register  for your computer
8000: by default portnumber


migrate
python manage.py migrate

when need setup in other system-->
pip install -r requirements.txt

                                                  Django orm
--------------------------------------------------------------------------------------------------------------------
object relation mapping
manage databaseinteractions
design or architectural pattern
Rapid development
code maintenance
security
one language

--------------------------------------------------------------------------------------------------------------------
                                                  define django models and fields
------------------------------------------------------------------------------------------------------------------
Traditional Approach
3rd party software(gui)

the django approach-->
Active Record Pattern
table defined by an oops class

define django models and fileds
oops class 
containes fileds.behaviours


                                      model manager--------------------------
--------------------------------------------------------------------------------------------------------
model---->model manager(queryset api)<-------->database
select * from student;
student.object.all()
model=student
manager=objects
queryset api method=all()


role of model manager
interface
quersets api
objects
modify data return from database

go throw-->django queryset api
