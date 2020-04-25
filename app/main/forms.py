from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, \
    TextAreaField, BooleanField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class InfoEditionsForm(FlaskForm):
    name = StringField(_l('Editions Name'), validators=[DataRequired()])
    intro = TextAreaField(_l('Intro'), validators=[DataRequired(), Length(min=0, max=500)])
    url = TextAreaField(_l('Link'), validators=[DataRequired(), Length(min=0, max=500)])
    submit = SubmitField(_l('Submit'))


class InfoEditionsDESCForm(FlaskForm):
    title = StringField(_l('Description Title'), validators=[DataRequired()])
    content = TextAreaField(_l('Content'), validators=[DataRequired(), Length(min=0, max=500)])
    infoeditions_id = TextAreaField(_l('Edition ID'), validators=[DataRequired(), Length(min=0, max=500)])
    submit = SubmitField(_l('Submit'))


class CloudServiceForm(FlaskForm):
    title = StringField(_l(' Cloud Service Delivers Title'), validators=[DataRequired()])
    content = TextAreaField(_l('Cloud Service Delivers Content'), validators=[DataRequired()])
    even = TextAreaField(_l('Even or Odd'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class MainProductForm(FlaskForm):
    title = StringField(_l('Main Product Title'), validators=[DataRequired()])
    intro = TextAreaField(_l('Intro of MainProduct'), validators=[DataRequired(), Length(min=0, max=500)])
    url = TextAreaField(_l('Link of MainProduct'), validators=[DataRequired(), Length(min=0, max=500)])
    icon = TextAreaField(_l('icon of MainProduct'), validators=[DataRequired(), Length(min=0, max=500)])
    submit = SubmitField(_l('Submit'))


class ServiceForm(FlaskForm):
    type = StringField(_l('Type'), validators=[DataRequired()])
    intro = TextAreaField(_l('Intro of Service'), validators=[DataRequired(), Length(min=0, max=500)])
    url = TextAreaField(_l('Link of Service'), validators=[DataRequired(), Length(min=0, max=500)])
    submit = SubmitField(_l('Submit'))


class ServiceTypeForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired()])
    content = TextAreaField(_l('Content'), validators=[DataRequired(), Length(min=0, max=500)])
    service_id = TextAreaField(_l('ID of ServiceType'), validators=[DataRequired(), Length(min=0, max=500)])
    submit = SubmitField(_l('Submit'))


class BusinessClientForm(FlaskForm):
    name = StringField(_l('Name of BusinessClient'), validators=[DataRequired()])
    intro = TextAreaField(_l('Intro of BusinessClient'), validators=[DataRequired()])
    industry = TextAreaField(_l('Industry of BusinessClient'), validators=[DataRequired()])
    country = TextAreaField(_l('Country of BusinessClient'), validators=[DataRequired()])
    url = TextAreaField(_l('Link of BusinessClient'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class InformationForm(FlaskForm):
    title = StringField(_l('Title of Information'), validators=[DataRequired()])
    subtitle = TextAreaField(_l('Subtitle of Information'))
    content = TextAreaField(_l('Content of Information'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

class InformationForm(FlaskForm):
    title = StringField(_l('Title of Information'), validators=[DataRequired()])
    subtitle = TextAreaField(_l('Subtitle of Information'))
    content = TextAreaField(_l('Content of Information'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))
class ContactForm(FlaskForm):
    region = StringField(_l('Region of Information'))
    country = TextAreaField(_l('Country of Information'))
    phone = TextAreaField(_l('Phone of Information'))
    email = TextAreaField(_l('Email of Information'))
    flag = TextAreaField(_l('Flag of Information'))
    submit = SubmitField(_l('Submit'))