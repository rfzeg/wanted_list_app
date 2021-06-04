#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Wishlist Flask app using PostgreSQL via SQLAlchemy
Author: Roberto Zegers R.
Copyright: Copyright (c) 2021, Roberto Zegers R.
License: BSD-3-Clause
Date: June 2021
Usage: python3 app.py
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://roberto@localhost:5432/whishlistdb'
db = SQLAlchemy(app)

class Wish(db.Model):
  __tablename__ = 'whishes'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)

  def __repr__(self):
    return f'<Whish {self.id} {self.description}>'

db.create_all()

@app.route('/whishes/create', methods=['POST'])
def create_wish():
  description = request.form.get('description', '')
  wish = Wish(description=description)
  db.session.add(wish)
  db.session.commit()
  return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', data=Wish.query.all())

if __name__ == '__main__':
  app.run(debug=True)
