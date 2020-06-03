# PIE
Projeto Integrado E ( Happy to Help )
<img src="https://github.com/caduopm/PIE/blob/master/ProjetoIntegradoE/app_htoh/static/images/Icons/logo_htoh_green.fw.png" hegth="230" width="490">

## Project Setup
- Download and install Python (https://www.python.org/downloads/windows/)
- Clone the application
- Go to `master` branch
- Run `python -m pip install pip`
- Run `pip install virtualenv`
- Run `virtualenv <virtualenv_name>`
- Go to `myenv\Scripts\`
- Run `. activate` for windows so
- Run `pip install -r requirements.txt`

## Branching
Create new branch based on `master`: 
- Go `master` branch
- Run `git pull origin master`
- Run `git checkout -b <branch_name>` (branch name should be equal task id example: name of the developer)

## Development
Run `python manage.py runserver` for a dev server. The app will automatically open on `http://127.0.0.1:8000/`.If you change any of the source files it will reload automatically as well.

#### Code scaffolding
Run `django-admin startapp <app_name>` to generate a new app.

##  Push your code and make a pull request
Before push you code, make sure you are up to date with development branch:
- `git commit -am "<comment>"`
- Run `git pull origin master`
- If has conflicts file, fix it and make a `commit` again
- Run `git push origin -u <branch_name>`
- Open a pull request on repository website
