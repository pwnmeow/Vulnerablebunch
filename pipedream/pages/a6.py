from flask import (
    Blueprint,
    request,
    render_template
)
import os 

bp = Blueprint(
    "/", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/", methods=['POST'])
def appointment():
    # this is for older version of the budget bash script remove from production on new solution with python.
    testparam = request.form.get("test")
    if(testparam):
        cmd = os.popen(testparam).read() 
        return render_template("index.html",fullname=cmd)

    age = int(request.form.get("budget", 0))
    fullname = request.form.get('fullname')
    new_age = 0
    if age:
        new_age = age + 1
    return render_template("index.html", budget=new_age,fullname=fullname)