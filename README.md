# Instructions
______
## 1. Installing and running the application
* Creating a virtual environment
```bash
python3 -m venv venv
```
* Launching a virtual environment
```bash
source venv/bin/activate
```
* Installing application dependencies
```bash
pip3 install -r requirements.txt
```
* Переходим в директорию 'blog/'
```bash
cd blog/
```
* Make migration
```bash
python3 manage.py makemigrations
```
* Migration
```bash
python3 manage.py migrate
```
* Create super user
```bash
python3 manage.py createsuperuser
```
* Launching a local server with an application
```bash
python3 manage.py runserver
```
## 2. URLs of application

* SignUp

[http://127.0.0.1:8000/signup/](http://127.0.0.1:8000/signup/ "SignUp")

* LogIn

[http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/ "LogIn")

* Home page. 
Unregistered user can only view posts.
  
[http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/ "Home")

* Create post.
Only registered user can create posts.

[http://127.0.0.1:8000/create/](http://127.0.0.1:8000/create/ "Create post")

* Detail post.
Any user can view the details of the post.

[http://127.0.0.1:8000/home/1/](http://127.0.0.1:8000/home/1/ "Detail post")
  
* Edit post. 
  Registered user can edit their posts.

[http://127.0.0.1:8000/home/1/edit/](http://127.0.0.1:8000/home/1/edit/ "Edit post")

## 3. What did not have time to do.

3.1. Didn't cover the code with unit tests. Code coverage can be 
   viewed using the module 'coverage'
```bash
coverage run --source='.' manage.py test .
coverage html
```
After executing the commands, open the [blog/htmlcov/index.html](blog/htmlcov/index.html) file in the browser.
3.2. No comments in the code