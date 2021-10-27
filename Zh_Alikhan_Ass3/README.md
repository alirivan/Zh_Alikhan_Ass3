# Logging in using JWT

<h2>Installation</h2>

```
pip3 install  flask
pip3 install flask_sqlalchemy
pip3 install  mysqlclient
pip3 install MySQLdb
pip3 install Flask-SQLAlchemy
pip3 install mysql-python
pop3 install jwt
```

<h2>Usage </h2>

```
from flask import *
import datetime
from flask_sqlalchemy import SQLAlchemy
import pymysql
import jwt
```

<h2>Examples</h2>
There are 2 functions when you visit index page:
1. logging | you should write your login and password
2. protected | you should write token
