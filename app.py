#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
  return render_template('index.html', data=[{
    'description': 'Wanted item 1'
    },{
    'description': 'Wanted item 2'
    },{
    'description': 'Wanted item 3'
    }])

if __name__ == '__main__':
  app.run(debug=True)
