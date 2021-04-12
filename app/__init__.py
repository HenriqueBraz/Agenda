# -*- coding: utf-8 -*-
# coding: utf-8
from datetime import timedelta
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_session import Session


app = Flask(__name__, template_folder="templates")

from app.views import agenda_view, agendamento_view, confirmacao_view

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)
app.config['SECRET_KEY'] = b'\xba\x86\xa3\xc8\xe6\xe0o\xfbb[\xf3\xf7\x11\x2c)C'
app.config['TEMPLATES_AUTO_RELOAD'] = True
sess = Session()
sess.init_app(app)
csrf = CSRFProtect(app)
csrf.init_app(app)