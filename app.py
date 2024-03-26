from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user





app = Flask(__name__)
app.config['SECRET_KEY'] = '9704223828'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'

bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'





@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
#db schema



class User(db.Model, UserMixin):


    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable = False, unique=True)
    password = db.Column(db.String(120), nullable = False)
    image_file = db.Column(db.String(120), default='default.jpeg')

    def __repr__(self):
        return f'id:{self.id} Name:{self.name} Email:{self.email} Pass:{self.password} image:{self.image_file}'


class Utils:
    
    def isUnique(emailx):
        print("in utils" ,emailx)
        dbRes = User.query.filter_by(email=emailx).first()
        print(dbRes)
        
        return dbRes
        



@app.route('/', methods=['GET', 'POST'])
def registor():

    dis = 'none'

    if (request.method == 'POST'):
       
        
        name =request.form['name']
        email =request.form['email']
        password =request.form['password']
    

        print('*'*50)
        print( email)




        if Utils.isUnique(email):
            dis='block'
            print("user Exsists")



            return render_template('Registor.html', display=dis)

        
            
        try:
            hashed_password = bcrypt.generate_password_hash(password)
            u1 = User(name=name, email=email, password=hashed_password)
            db.session.add(u1)
            db.session.commit()
                
        except Exception as e:
            print(e)
        
    return render_template('Registor.html', display= dis)




@app.route('/login' ,methods=['GET', 'POST'])
def login():


    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']


        print(email, password, "in login")

        user = User.query.filter_by(email=email).first()
        print(user)
        if user:

            if bcrypt.check_password_hash(user.password, password):




                login_user(user)

                print("Authetication success")
                return redirect(url_for('dashboard'))

        
            

        else:

            print("Invalid Username or Password")


    return render_template('login.html')



@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():

    #make a request to this end point to logout
    return 'Logged in'




app.run(debug=True, host='0.0.0.0', port=5000)