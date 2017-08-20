"""Define Views and Routes for Front End App."""

from flask import render_template, request
from unihack import app
import requests


@app.route('/')
@app.route('/home')
def home():
    id = request.args.get('event', '1')
    event = requests.get('http://10.1.1.131:5000/api/event/' + id).json()
    """Route for homepage."""
    #print(event)
    #event[id]['articles'][id]['content'].replace('\n', '')
    return render_template('index.html', event = event[id], id = id, sid = str(id))




@app.errorhandler(404)
def page_not_found(e):
    """404 Page Not Found."""
    return render_template('404.html'), 404


@app.after_request
def add_header(r):
    """
    Stop caching CSS.

    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
