from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField, SubmitField

class EmbedSearch(FlaskForm):

    lineItemId = StringField('lineItemId', validators=[validators.InputRequired(),validators.length(max=200),validators.Optional(strip_whitespace=True)])
    previewURL = StringField('previewURL', validators=[validators.InputRequired(),validators.length(max=500),validators.Optional(strip_whitespace=True)])
    search_lineItemID = SubmitField(label='Search')
    snap = SubmitField(label='Screenshot')
    preview = SubmitField(label='Preview')
    # appNotification = SubmitField(label='Genarate QR Code')
