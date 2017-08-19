"""Define Views and Routes for Front End App."""

from flask import render_template
from unihack import app


@app.route('/')
@app.route('/home')
def home():
    """Route for homepage."""
    return render_template('index.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
  app.run(debug=True)
