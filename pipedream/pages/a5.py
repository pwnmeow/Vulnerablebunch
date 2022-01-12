from flask import (
    Blueprint,
    request,
    redirect,
    make_response,
    render_template
)
import os
from models import (
    get_user,
    get_user_by_password
)

from utils import (
    generate_session,
    parse_session
)
UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'xml'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


bp = Blueprint(
    "a5", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/super-admin/login")
def a5():
    return render_template("a5.html")

@bp.route("/super-admin/login", methods=['POST'])
def a5_auth():
    username = request.form.get("username")
    password = request.form.get("password")
    user = get_user_by_password(username, password)
    if not user:
        return render_template("error.html", message="Invalid Credentials")
    
    # Generate SessionID
    session_id = generate_session(username)
    response = make_response(redirect("/super-admin/profile/{}".format(username)))
    response.set_cookie("sessionId", session_id)
    
    return response


@bp.route("/super-admin/profile/<username>")
def a5_profile(username):
    if not request.cookies.get("sessionId"):
        return ("<h1>Not Authorized!</h1>")
    session = parse_session(request.cookies.get("sessionId"))
    user = get_user(username)
    if not user:
        return render_template("404.html")
    print(user)
    return render_template("profile.html", user=user)
