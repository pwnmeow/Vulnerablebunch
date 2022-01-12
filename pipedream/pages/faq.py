from flask import (
    Blueprint,
    render_template
)

bp = Blueprint(
    "faq", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/faq")
def index():
    return render_template("faq.html")