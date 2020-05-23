from flask import current_app, Blueprint
bp = Blueprint("all", __name__)

@bp.route("/")
def index():
    return "Hello!"