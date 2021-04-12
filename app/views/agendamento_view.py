# -*- coding: utf-8 -*-
# coding: utf-8

from app import app
from flask import render_template, request


@app.route('/agendamento', methods=['GET', 'POST'])
def agendamento():
    if request.method == 'POST':
        return render_template('/confirmacao.html')
    else:
        return render_template('/agendamento.html')
