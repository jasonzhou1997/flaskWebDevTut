from ast import Pass
import email
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

#create registered forms

class RegisterForm(FlaskForm):
    #check if given username is already existing inside database
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username = username_to_check.data).first()
        if user:
            raise ValidationError("Username already exits! Please try a different username")
        
    def validate_email_address(self, emailaddress_to_check):
        email_address = User.query.filter_by(email_address = emailaddress_to_check.data).first()
        if email_address:
            raise ValidationError("Email Address already exists! Please try a different email address")
        
    username = StringField(label="User Name: ", validators=[Length(min=3, max=15), DataRequired()])
    email_address = StringField(label="Email Address: ", validators=[Email(), DataRequired()])
    password1 = PasswordField(label = "Password: ", validators = [Length(min=6), DataRequired()])
    password2 = PasswordField(label = "Confirm Password: ", validators=[EqualTo("password1"), DataRequired()])
    submit = SubmitField(label = "Create Account")
    
class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators = [DataRequired()])
    password = PasswordField(label='Password:', validators = [DataRequired()])
    submit = SubmitField(label = "Please Log in")
    
class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')
class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')
    
    
    
    