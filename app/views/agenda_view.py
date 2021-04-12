# -*- coding: utf-8 -*-
# coding: utf-8

from app import app
from flask import url_for, render_template, redirect


@app.route('/')
def inicio():
    return redirect(url_for('agenda'))


@app.route('/agenda')
def agenda():
    return render_template('/agenda.html')
