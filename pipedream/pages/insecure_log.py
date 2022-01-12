
from flask import (
    Blueprint,
    request,
    redirect,
    render_template,
    make_response
)


from werkzeug.wrappers import response

bp = Blueprint(
    "insecure_log", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/logs")
def logs():
    # response = make_response(redirect("/admin/welcome"))
    # response.set_cookie("sessionId", session_id)
    debug = request.cookies.get('debug')
    print(debug)
    if debug == "True":
    #    return "here your logs"
        response = render_template('logs.txt')
        # response['Content-Type'] =  'text/plain'
        return response           
    else: 
        response = render_template('noLogs.html')
        # response.set_cookie("debug", False)
        return response
    # response = 
    # return response
