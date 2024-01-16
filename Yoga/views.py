"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Yoga import app
from flask import Flask, render_template, request
import openai


@app.route('/yoga_builder', methods=['GET', 'POST'])
def yoga_builder():
    routine = ""
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = openai.Completion.create(
            engine="text-davinci-004",
            prompt=f"Create a yoga routine based on the following preferences: {user_input}",
            max_tokens=150
        )
        routine = response.choices[0].text.strip()

    return render_template('yoga_builder.html', routine=routine)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
