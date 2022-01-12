from flask import (
    Blueprint,
    render_template
)

bp = Blueprint(
    "auth", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/auth")
def auth():
    return render_template("auth.html")