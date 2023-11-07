"""Pet Adoption Application"""

from flask import Flask, render_template, redirect, jsonify, url_for
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'


with app.app_context():
    connect_db(app)
    db.create_all()
    new_pet1 = Pet(name="Bobby the Bear", species="bear", photo_url="https://www.freeiconspng.com/uploads/panda-bear-icon-33.png", age=5, notes="no notes", available=True)
    db.session.add(new_pet1)
    db.session.commit()
    new_pet2 = Pet(name="Kitty", species="cat", photo_url="https://www.freeiconspng.com/uploads/panda-bear-icon-33.png", age=5, notes="no notes", available=True)
    db.session.add(new_pet2)
    db.session.commit()
    new_pet3 = Pet(name="Doggy", species="dog", photo_url="https://www.freeiconspng.com/uploads/panda-bear-icon-33.png", age=5, notes="no notes", available=True)
    db.session.add(new_pet3)
    db.session.commit()
    

@app.route("/")
def list_pets():
    """Show pets."""

    pets = Pet.query.all()
    return render_template("pet_gallery.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('list_pets'))

    else:
        return render_template("add_pet_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect(url_for('list_pets'))

    else:
        return render_template("edit_form.html", form=form, pet=pet)


@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Display information about a specific pet."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)