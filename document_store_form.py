####################################################################################
# document_store_form.py                                                           #
# Author:        Alexander O'Dempsey (xander-odempsey@hotmail.com)                 #
# Modified by:                                                                     #
# Date Created:  29/04/2018                                                        #
# Last Modified:                                                                   #
# Brief:         Form for storing a document                                       #
####################################################################################

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import StringField, IntegerField, SubmitField

class DocumentStore(FlaskForm):
    id = IntegerField('id', validators=[DataRequired()])
    message = StringField('message', validators=[DataRequired()])
    ttl = IntegerField('ttl', validators=[DataRequired()])
    submit = SubmitField("Store Document")

