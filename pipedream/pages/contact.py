from flask import (
    Blueprint,
    request,
    render_template
)
import urllib
bp = Blueprint(
    "contact", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/contact")
def index():
    return render_template("contact.html")

@bp.route("/contact", methods=['POST'])
def store():
    url = request.form.get("url")
    return urllib.request.urlopen(url).read() # Noncompliant