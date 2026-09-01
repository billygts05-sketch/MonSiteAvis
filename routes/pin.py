import os

from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from werkzeug.utils import secure_filename

from database import Kim, db

pin_bp = Blueprint('pin', __name__)

@pin_bp.route("/", methods=["GET", "POST"])
def accueil():

    if request.method == "POST":

        email = request.form.get("email")
        text = request.form.get("text")
        photo = request.files.get("fichier")

        if email == "":
            flash("veuiller remplir tous les champs")
            return render_template("accueil.html")

        if len(text) <= 5:
            flash("le text doit contenir au moins 5 caracteres !")
            return render_template("accueil.html")

        if len(email) >= 50:
            flash("email est trot long")
            return render_template("accueil.html")

        if photo and photo.filename != "":
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = None

        nouvel_avis = Kim(email=email, text=text, photo=filename)
        db.session.add(nouvel_avis)
        db.session.commit()

        flash("Message recu avec succes")

        return redirect(url_for("pin.succes"))

    return render_template("accueil.html")

@pin_bp.route("/success")
def succes():
    return render_template("success.html")