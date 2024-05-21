from flask import render_template
from flask_login import current_user

def list_libros(libros):
    return render_template(
        "animals.html",
        libros = libros,
        title  ="lista de libros",
        current_user = current_user,
    )

def create_libro():
    return render_template(
        "create_animal.html", title ="crear Libro", current_user = current_user
    )

def update_libro(libro):
    return render_template(
        "update_libro.html",
        title = "editar libro",
        libro = libro,
        current_user = current_user,
    )
