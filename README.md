# ZoneZero
## Introduction.
###### ZoneZero is a python - Flask based web application.

###### It utilises tomcat7 as a server.
ZoneZero uses CAS [Flask-CAS] single sign on to authorise users.

###### ZoneZero is a note taking application that enables one to take notes, edit and view them.

## Getting Started.
###### Operating System - Linux
###### Python Version - 2.7.14

### Open terminal/bash and input:

#### Prerequisites & Setup:

###### Installation of sqlite database that is used.
    `sudo apt-get install sqlite3`
        
###### If not yet installed git.
    `sudo apt-get install git`

Otherwise,

    `git clone https://github.com/Maxwell-Icharia/ZoneZero`

###### Extract the application from the github repository.

    `cd ZoneZero/`

###### Access the application and it's contents.
[All the terminal commands are to be done while in this directory]

###### ZoneZero/

#### Application Setup:

###### Install pip in order to install various requirements needed by the application.
    `sudo apt-get install python-pip`

###### Use pip to install a virtual environment for running the application.
    `sudo pip install virtualenv`

###### Create a new virtual environment that will be used to run the application without tampering with your system's various installed modules.
    `virtualenv venv`

###### Activate your virtual environment.
    `. venv/bin/activate`

###### Install all the requirements needed to run the application found in the requirements.txt file.
    `pip install -r requirements.txt`

###### Run the application.
    `python run.py`
