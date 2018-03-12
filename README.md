# REAMDME

The project base on Flask and python3.6

## Install

> pip install -r  requirements.txt


###  About virtualenv and wrapper
If you do not want to install flask globally you can use virtualenv and virtualenvwrapper


>pip install virtualenv

>$ pip install virtualenvwrapper

>$ export WORKON_HOME=~/Envs

>$ source /usr/local/bin/virtualenvwrapper.sh


#### Basic Usage of virtualenv

1,Create a virtual environment:

>$ mkvirtualenv my_project

This creates the my_project folder inside ~/Envs.

2,Work on a virtual environment:

>$ workon my_project

Alternatively, you can make a project, which creates the virtual environment, and also a project directory inside $PROJECT_HOME, which is cd -ed into when you workon myproject.

>$ mkproject myproject

virtualenvwrapper provides tab-completion on environment names. It really helps when you have a lot of environments and have trouble remembering their names.

workon also deactivates whatever environment you are currently in, so you can quickly switch between environments.

only after you create your local python environment, you can do python install flask to install flask package in the local environment.


3,Deactivating is still the same:

>$ deactivate

4,To delete:

>$ rmvirtualenv venv


## How to run

>python manage.py server

## How to test

> python test.py

## API intereface

- Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.

service address: http://127.0.0.1:5000/api/company/companyname

- Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.

service address: http://127.0.0.1:5000/api/common

sample post json is samplerequest2.json

- Same as feature2 but only  send just the user id. and return the user names

service address: http://127.0.0.1:5000/api/commonid/id1/id2

only array of user name as result

- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface: { "username": "Ahi", "age":"30", "fruits":["banana", "apple"], "vegetables":["beetroot", "lettuce"]}

service address: http://127.0.0.1:5000/api/user/username

notice: the use name must use html encode, for example Decker Mckenzie should be Decker%20Mckenzie
