from flask import (
    Blueprint,
    request,
    redirect,
    render_template,
    make_response
)
from werkzeug.wrappers import response
from models import get_user_by_password
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
    "a2", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/login")
def a2():
    if request.cookies.get("sessionId"):
        response = make_response(redirect("/admin/welcome"))
        return response
    else:
        return render_template("a2.html")

@bp.route("/login/auth", methods=['POST'])
def a2_auth():
    username = request.form.get("username")
    password = request.form.get("password")
    user = get_user_by_password(username, password)
    if not user:
        return render_template("error.html", message="Invalid Crendentials")

    # Generate SessionID
    session_id = generate_session(username)
    response = make_response(redirect("/admin/welcome"))
    response.set_cookie("sessionId", session_id)

    return response

@bp.route("/admin/welcome")
def a2_welcome():
    if not request.cookies.get("sessionId"):
        return ("<h1>Not Authorized!</h1>")
    session_obj = parse_session(request.cookies.get("sessionId"))
    
    return render_template("welcome.html", username=session_obj['username'])

@bp.route("/admin/welcome", methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        file.save( "sitemap.xml")
        return redirect("/site-map")
    else:
        return "Invalid file"


@bp.route('/admin/logout')
def logout():
    response = make_response(redirect("/login"))
    response.set_cookie("sessionId", '',expires=0)
    return response