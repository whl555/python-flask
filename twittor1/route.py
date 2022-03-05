
from flask import render_template, redirect, url_for
from twittor1.forms import LoginForm


def index():
    name = {"username": "Whl",
            "password": "271826",
            "time": 20220306}
    title = 'flask'
    rows = [{"name": 'a', "money": 1}, {"name": 'a', "money": 1},
            {"name": 'b', "money": 2}, {"name": 'a', "money": 3}]
    return render_template("index.html", name=name, title=title)


def login():
    form = LoginForm()
    name = {"username": "Whl",
            "password": "271826",
            "time": 20220306}
    if form.validate_on_submit():
        msg = "username={}, remember_me={}, password={}".format(
            form.username.data,
            form.remember_me.data,
            form.password.data
        )
        print(msg)
        return redirect(url_for("index"))
    return render_template("login.html", name=name, title="Sign In", form=form)
