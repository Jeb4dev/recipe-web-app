from flask import Blueprint

account = Blueprint('account', __name__)

from .login import login
from .register import register
# from .logout import logout
