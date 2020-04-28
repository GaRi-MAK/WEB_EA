from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, \
    TextAreaField
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
    title = StringField(_l('Editions Title'), validators=[DataRequired()])
    content = TextAreaField(_l('Content'), validators=[DataRequired(), Length(min=0, max=500)])
    url = TextAreaField(_l('Url'), validators=[DataRequired(), Length(min=0, max=500)])
    submit = SubmitField(_l('Submit'))

class InfoEditionsDESCForm(FlaskForm):
    title = StringField(_l('Description Title'), validators=[DataRequired()])
    content = TextAreaField(_l('Content'), validators=[DataRequired(), Length(min=0, max=500)])
    edition_id = TextAreaField(_l('Edition ID'), validators=[DataRequired(), Length(min=0, max=500)])
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
    name = StringField(_l('Service Name'), validators=[DataRequired()])
    intro = TextAreaField(_l('Intro of Service'), validators=[DataRequired(), Length(min=0, max=500)])
    url = TextAreaField(_l('Link of Service'), validators=[DataRequired(), Length(min=0, max=500)])
    submit = SubmitField(_l('Submit'))
class ServiceTypeForm(FlaskForm):
    title = StringField(_l('Service Title'), validators=[DataRequired()])
    content = TextAreaField(_l('Content of ServiceType'))
    service_id = TextAreaField(_l('Id of Service'))
    submit = SubmitField(_l('Submit'))


class PartnersContentForm(FlaskForm):
    c_title = StringField(_l('Content Title'), validators=[DataRequired()])
    content = TextAreaField(_l('Content of Partners'))
    submit = SubmitField(_l('Submit'))

class WhySQLForm(FlaskForm):
    name = StringField(_l('Item Name'), validators=[DataRequired()])
    url = TextAreaField(_l('Link of Item'))
    submit = SubmitField(_l('Submit'))
class WhySQLContentForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired()])
    content = TextAreaField(_l('Content'))
    whysql_id= TextAreaField(_l('Id of WhySQL'))
    submit = SubmitField(_l('Submit'))
class HowToBuyForm(FlaskForm):
    title = StringField(_l('Title'), validators=[DataRequired()])
    content = TextAreaField(_l('Content'))
    url = TextAreaField(_l('Link of Item'))
    submit = SubmitField(_l('Submit'))