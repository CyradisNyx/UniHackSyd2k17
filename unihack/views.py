"""Define Views and Routes for Front End App."""

from flask import render_template
from unihack import app


@app.route('/')
@app.route('/home')
def home():
    """Route for homepage."""
    return render_template('index.html')
