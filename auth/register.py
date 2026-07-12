from flask import Blueprint, render_template, request, redirect, url_for
from database.db import get_connection

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        favourite_movie = request.form["favourite_movie"]

        if password != confirm_password:
            return "Password and Confirm Password do not match."

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO users
            (username, firstname, lastname, password, favourite_movie)
            VALUES (%s,%s,%s,%s,%s)
            """,
            (
                username,
                firstname,
                lastname,
                password,
                favourite_movie
            )
        )

        connection.commit()

        cursor.close()
        connection.close()

        return redirect(url_for("login.login"))

    return render_template("register.html")
