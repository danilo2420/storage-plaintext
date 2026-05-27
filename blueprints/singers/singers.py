from flask import Blueprint

singers_bp = Blueprint("singers", __name__, url_prefix="/singers")

@singers_bp.route("/test")
def testSingers():
    return "Singers works!"