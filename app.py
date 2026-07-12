from flask import Flask, render_template, session, redirect

from auth.login import login_bp
from auth.register import register_bp

app = Flask(__name__)

app.secret_key = "movie_theatre_secret_key"

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)


@app.route("/theatre")
def theatre():

    if "firstname" not in session:
        return redirect("/login")

    return render_template(
        "theatre.html",
        firstname=session.get("firstname"),
        lastname=session.get("lastname"),
        movie=session.get("movie")
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
