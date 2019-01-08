from flask import Blueprint, render_template


test_controller = Blueprint('test', __name__, template_folder='templates')

@test_controller.route('/')
def test_route():
    return render_template('test/index.html')