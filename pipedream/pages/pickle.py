from flask import (
    Blueprint,
    request,
    redirect,
    render_template,
    make_response
)
import base64,pickle

bp = Blueprint(
    "debug", __name__,
    template_folder='templates',
    static_folder='static'
)



class User(object):

    def __init__(self, username):
        self.username = username


class TestUser:
    admin: int = 0
pickled_user = pickle.dumps(TestUser())
encoded_user = base64.b64encode(pickled_user)
print(encoded_user,"encoded")

@bp.route("/debug")
def debug():
        # response = make_response(redirect("/admin/welcome"))
        # response.set_cookie("sessionId", session_id)
        response = make_response(redirect("/debug/denied"), {"message":"Only Admins can see this page"})
        token = request.cookies.get('token')
        if token == None:
            token = encoded_user
            response.set_cookie(key='token',value=token.decode('utf-8'),expires=1651321936)
            return response
        else:
            token = base64.b64decode(token)
            # return token
            admin = pickle.loads(token)
            print("admin 43",admin)
            # return admin
            if admin.admin == 1:
                response = make_response("/")
                return response

        return response


@bp.route("/debug/denied")
def denied():
      response = render_template("noAccess.html")
      return response