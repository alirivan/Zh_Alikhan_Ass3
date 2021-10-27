
from flask import *
from functools import *
import datetime
from flask_sqlalchemy import SQLAlchemy
import pymysql
import jwt


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Alik1234@localhost/Ass33'
app.config['SECRET_KEY']='Secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db=SQLAlchemy(app)


class Users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    login=db.Column(db.String(255),nullable=False,unique=True)
    password=db.Column(db.String(255),nullable=False)
    token=db.Column(db.Text,nullable=False,default='')

    def __init__(self,id,login, password, token):
           self.id = id
           self.login = login
           self.password = password
           self.token = token

new_ex1 = Users(1,"asdf@gmai.com", "1234rtew", "12w3elkmjnb32yquioalsd,mnfdewapoiujh" )
new_ex2 = Users(3,"asfghjkldf@gmai.com", "1ghjkl234rtew", "12wcvghjkl3elkmjnb32yquioalsd,mnfghjfdewapoiujh" )
new_ex3 = Users(2,"asdfjbb@gmai.com", "1234rjjnjnjtew", "12wjjjnbjn3elkmjnb32yquioalsd,mnfdewapoiujh" )
db.session.add(new_ex1)
db.session.add(new_ex2)
db.session.add(new_ex3)
db.session.commit()




@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        token=request.form['tok']
        return redirect('/protected?token='+token)
    return render_template('index.html')

@app.route('/login')
def login():
    auth= request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    user=Users.query.filter_by(login=auth.username).first()
    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})
    if auth and auth.password==user.password:
        token = jwt.encode(
            {'username': user.login, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)},
            app.config['SECRET_KEY'])
        user = Users.query.filter_by(login=auth.username).first()
        user.token = token
        db.session.commit()
        return jsonify({'token':jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"])})
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login required'})

@app.route('/protected')
def check():
    token = request.args.get('token')
    if not token:
        return '<h1>Hello, token is missing </h1>', 403
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    except:
        return '<h1>Hello, Could not verify the token</h1>', 403
    return '<h1>Hello, token which is provided is correct</h1>'

if __name__=='__main__':
    app.run(debug=True)


