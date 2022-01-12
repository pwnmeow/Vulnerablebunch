from flask import (
    Blueprint,
    render_template
)

bp = Blueprint(
    "pricing", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/pricing")
def index():
    return render_template("pricing.html")