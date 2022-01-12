from flask import (
    Blueprint,
    request,
    render_template_string,
    make_response
)

bp = Blueprint(
    "a1", __name__,
    template_folder='templates',
    static_folder='static'
)

@bp.route("/search")
def a1():
    ### Server-Side Template Injection
    name = request.args.get("name", "")
    with open("templates/a1.html") as f:
        template = f.read()
    content = template.replace("{{ name }}", name)
    response = make_response(render_template_string(content))
    response.headers['X-Powered-By'] = 'Jinja 2.10'
    return response
