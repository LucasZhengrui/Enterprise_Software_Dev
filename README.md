# Natural Disaster Management

## 1 - About us

Our website application refers to the open-source data from https://www.kaggle.com/datasets/brsdincer/all-natural-disasters-19002021-eosdis, which used Django for the database and its creation, and edit operations. This website application allows users to check disaster data with login or without login, which means that clients can browse as a user or as a guest. And this website application has multiple views for the database, which would be available for different kinds of users. To be specific, we used plotly to improve the view of [dashboard](https://disaster-management.onrender.com/dashboard/). We can also announce a message to the website by using [SystemMessage](https://disaster-management.onrender.com/chat/), and the message can be shown on each page.

## 2 - Main features

* View the summary of disaster data
* View the detail of disaster data
* Edit the summary of disaster data
* Archive the data
* Recover the data
* Different views for the data (Maps, pie graph, and line chart)
* Message system station
* User list
* Login and add account
* Specific data downloader

## 3 - Database overview

![](https://i.imgur.com/VKXMjLK.png)

## 4 - Installation

### 4.1 If you are using Codio:

#### 4.1.1 Create a virtual environment and activate it in the terminal of Codio
``` shell
    python3 -m venv .venv 
```

``` shell
    source .venv/bin/activate 
```

#### 4.1.2 Clone the repository or pull the code from Github
``` shell
    git clone git@github.com:LucasZhengrui/Enterprise_Software_Dev_Note.git
```
Or if you have cloned before

``` shell
    git pull origin main
```

#### 4.1.3 Changed the site details in **ALLOWED_HOSTS** of ```mysite/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['127.0.0.1','albumhexagon-canvasgenesis-8000.codio-box.uk','sharonpackage-expandfood-8000.codio-box.uk','disaster-management.onrender.com', 'virgoprinter-iconpupil-8000.codio-box.uk']
```

#### 4.1.4 Install Django and Plotly in terminal

As for the Django installation

``` shell
    pip install django
```

As for the Plotly in terminal

``` shell
    pip install plotly
```

#### 4.1.5 Run the website application

``` shell
    python3 manage.py runserver 0.0.0.0:8000
```

P.S **8000** is decided by what did you input in 3.1.3

### 4.2 If you are using a local editor, such as Visual Studio Code, or Mac Terminal:

#### 4.2.1 Create a virtual environment and activate it in the terminal
``` shell
    python3 -m venv .venv 
```

``` shell
    source .venv/bin/activate 
```

#### 4.2.2 Clone the repository or pull the code from Github
``` shell
    git clone https://github.com/LucasZhengrui/Enterprise_Software_Dev_Note.git
```
Or if you have cloned before

``` shell
    git pull origin main
```

#### 4.2.3 Changed the site details in **ALLOWED_HOSTS** of ```mysite/setting.py```

For example:

``` shell
    ALLOWED_HOSTS = ['127.0.0.1','localhost']
```

#### 4.2.4 Install Django and Plotly in terminal

As for the Django installation

``` shell
    pip install django
```

As for the Plotly in terminal

``` shell
    pip install plotly
```

#### 4.2.5 Run the website application

``` shell
    python3 manage.py runserver
```

## 5 - Test

Besides the disaster table app, we have done unit testing for other apps. The table app does not need us to test inside the app, but we have their related testing in other apps. 

## 6 - Details of deploying the website application

The website application has been deployed to Render, here is its URL: https://disaster-management.onrender.com/ .

Build command:

``` shell
    pip install --upgrade pip && pip install -r requirements.txt
```

Start command:

``` shell
    gunicorn mysite.wsgi:application --worker-class=gevent --worker-connections=1000 --workers=4 --bind=0.0.0.0:$PORT
```