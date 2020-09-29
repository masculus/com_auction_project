from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, IntegerField, DecimalField, SelectField, DateField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired('User Name is required')])
    password = PasswordField('Password', validators=[InputRequired('Password is required')])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired('User Name is required')])
    email = StringField('Email Address', validators=[Email('Email is required'), Email('Email is not valid')])
    
    #add buyer/seller - check if it is a buyer or seller hint : Use RequiredIf field

    #linking two fields - password should be equal to data entered in confirm
    password = PasswordField('Password', validators=[InputRequired(),
                  EqualTo('confirm', message='Passwords should match')])
    confirm = PasswordField('Confirm Password')

    #submit button
    submit = SubmitField("Register")

class ListingForm(FlaskForm):
    title = StringField('Listing Title', validators=[InputRequired('Listing title is required')])
    starting_bid = DecimalField('Starting Bid', validators=[InputRequired('Must enter a starting bid')])
    brand = SelectField('Brand', choices=[('Apple', 'Apple'), ('Microsoft', 'Microsoft'), ('Dell', 'Dell'), ('HP', 'HP'), ('Lenovo', 'Lenovo'), ('Acer', 'Acer')])
    cpu = SelectField('CPU', choices=[('i3', 'i3'), ('i5', 'i5'), ('i7', 'i7')])
    ram = SelectField('RAM', choices=[('4GB', '4GB'), ('8GB', '8GB'), ('16GB', '16GB'), ('32GB', '32GB')])
    storage = SelectField('Storage', choices=[('64GB', '64GB'), ('128GB', '128GB'), ('256GB', '256GB'), ('512GB', '512GB'), ('1TB', '1TB')])
    condition = SelectField('Condition', choices=[('Excellent', 'Excellent'), ('Good', 'Good'), ('Minor defects', 'Minor defects'), ('Used', 'Used'), ('New', 'New')])
    end_date =  DateField('End Date', format='%d/%m/%Y')
    
    # For testing purposes (will need to be changed)
    image = StringField('Image', validators=[InputRequired('Image is required')])
    seller = StringField('Seller', validators=[InputRequired('Seller alias is required')])

    description = TextAreaField('Description', validators=[InputRequired('Description is required'), Length(min=10, max=300, message='Description is too short or too long')])

    submit = SubmitField('Post Listing')

class ReviewForm(FlaskForm):
    feedback = TextAreaField('Review', [InputRequired('Review is required'), Length(min=5, max=400, message='Review is too long or too short')])
    submit = SubmitField('Post Review') 