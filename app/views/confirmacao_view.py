# -*- coding: utf-8 -*-
# coding: utf-8

from app import app
from flask import render_template


@app.route('/confirmacao', methods=['GET', 'POST'])
def confirmacao():
    return render_template('/confirmacao.html')
