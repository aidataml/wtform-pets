"""Pet Adoption Model"""

from flask_sqlalchemy import SQLAlchemy
DEFAULT_IMAGE_URL = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"
db = SQLAlchemy()


class Pet(db.Model):
    """Pet database for available adoptions."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Photo url image for pet."""

        return self.photo_url or DEFAULT_IMAGE_URL


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
