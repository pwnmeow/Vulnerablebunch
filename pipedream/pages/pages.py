from flask import (
    Blueprint,
    render_template,
    request
)

bp = Blueprint(
    "pages", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/pages")
def index():
    # return "ok"
    return render_template( request.args.get('page') + ".html")