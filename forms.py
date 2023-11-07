from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, URL, Optional, Length, NumberRange

class AddPetForm(FlaskForm):
    """Form - Add pets to the pet list."""

    name = StringField(
        "Pet Name",
        validators=[InputRequired()],
    )

    species = SelectField(
        "Species",
        choices=[("dog", "Dog"), ("cat", "Cat"), ("bear", "Bear"), ("bird", "Bird"), ("hampster","hampster")],
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )


class EditPetForm(FlaskForm):
    """Form - Edit pet information."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")