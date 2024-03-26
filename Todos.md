## Boiler plate
## configs
## **render_template** funtion, redirect(url_for())
## Static files {{ url_for('static', filename='css/style.css')}}
## templating engine
## db -flask_sqlalchemy, 
## Authentication better to use sessions    
    -- flask_login -- flask_login.LoginManager() --flask_login.User, --login_required()
## Search algorithm

## @login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

## db design 
    

    1. User

    # Name
    # Email 
    # password
    # profile-pic <path> default='image.jpeg'
   ~ # Role in collge {student, professor, other}
