from flask import Blueprint, render_template, request, redirect, session
from database.db import get_connection

login_bp = Blueprint("login", __name__)

@login_bp.route("/", methods=["GET", "POST"])
@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username=%s
            AND password=%s
            """,
            (username, password)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user:

            session["firstname"] = user["firstname"]
            session["lastname"] = user["lastname"]
            session["movie"] = user["favourite_movie"]

            return redirect("/theatre")

        return "Invalid Username or Password"

    return render_template("login.html")
