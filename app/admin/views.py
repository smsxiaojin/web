# coding:utf8
from . import admin
from app.home import home
from flask import render_template, redirect, url_for, flash, session, request
from app.admin.forms import ContactFrom
from app.models import Contact
from functools import wraps
from app import db, app
from werkzeug.utils import secure_filename
import os
import uuid
import datetime


def admin_login_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "admin" not in session:
            return redirect(url_for("admin.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function






@admin.route("/contact/con/", methods=["GET", "POST"])
@admin_login_req
def moiveadd():
    form = ContactForm()

    if form.validate_on_submit():
        data = form.data
        file_url = secure_filename(form.url.data.filename)
        file_logo = secure_filename(form.logo.data.filename)

        contact = Contact(
            name=data["name"],

            message=data["message"],
            email=data["email"],



            tag_id=int(data["tag_id"]),
            release_time=data["release_time"],
            length=data["length"]
        )
        db.session.add(contact)
        db.session.commit()
        flash("成功提交！", "ok")
        return redirect(url_for("home.contact"))

    return render_template("home.contact", form=form)


