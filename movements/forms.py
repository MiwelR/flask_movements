from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField, DecimalField
from wtforms.validators import DataRequired, Length, ValidationError, AnyOf, Email
from wtforms.widgets import TextArea, Select
from wtforms.fields.html5 import DateField

from datetime import date

def validate_fecha(form, field):
        hoy = date.today()
        if field.data < hoy:
            raise ValidationError('La fecha debe ser superior o igual a hoy')

class MiForm(FlaskForm):
    fecha = DateField('Fecha:', validators=[DataRequired('Debe introducir una fecha correcta')])
    concepto = StringField('Concepto:', validators=[DataRequired('Debe introducir un concepto')])
    cantidad = DecimalField('Cantidad:', validators=[DataRequired('Debe introducir una cantidad numérica')])
    enviar = SubmitField('Enviar')

