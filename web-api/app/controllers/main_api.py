from app import app
from flask import Blueprint

main_blueprint = Blueprint('main', __name__)
@main_blueprint.route('/')
def index():
    return "Main"