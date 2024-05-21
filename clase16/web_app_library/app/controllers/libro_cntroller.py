from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.libro_model import Libro
from views import libro_view

from utils.decorators import role_required

libro_bp = Blueprint("libro", __name__)

@libro_bp.route("/libros")
@login_required
def list_libros():
    libros = Libro.get_all()
    return libro_view.list_libros(libros)

@libro_bp.route("/libros/create", )

