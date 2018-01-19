# coding:utf8
from . import home
from flask import render_template, redirect, url_for, request


@home.route("/")
def index():
    return render_template("home/index.html")


@home.route("/contact/")
def contact():
    return render_template("home/contact.html")

@home.route("/single/")
def single():
    return render_template("home/single.html")

@home.route("/blog/")
def blog():
    return render_template("home/blog.html")


