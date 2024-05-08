from flask import Blueprint, request, jsonify
from models.library_model import Libro
from views.library_view import render_libro_list, render_libro_detail

libro_bp = Blueprint("libro", __name__)

@libro_bp.route("/library/<int:id>", methods = ["GET"])
def get_libros():
    libros = Libro.get_all()
    return jsonify(render_libro_list(libros))


@libro_bp.route("/Libros/<int:id>", methods=["GET"])
def get_libro(id):
    libro = libro.get_by_id(id)
    if libro:
        return jsonify(render_libro_detail(libro))
    return jsonify({"error": "libro no encontrado"}), 404

@libro_bp.route("/libros", methods=["POST"])
def create_libro():
    data = request.json
    title = data.get("title")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibility = data.get("disponibility")

    # Validación simple de datos de entrada
    if not title or not autor or edicion or disponibility is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo animal y guardarlo en la base de datos
    libro = Libro(title=title, autor=autor, edicion=edicion, disponibility=disponibility)
    libro.save()

    return jsonify(render_libro_detail(libro)), 201


# Ruta para actualizar un animal existente
@libro_bp.route("/libros/<int:id>", methods=["PUT"])
def update_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "libro no encontrado"}), 404

    data = request.json
    title = data.get("title")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibility = data.get("disponibility")

    # Actualizar los datos del animal
    libro.update(title=title, autor=autor, edicion=edicion, disponibility = disponibility)

    return jsonify(render_libro_detail(libro))


# Ruta para eliminar un animal existente
@libro_bp.route("/libros/<int:id>", methods=["DELETE"])
def delete_libro(id):
    libro = Libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "libro no encontrado"}), 404

    # Eliminar el animal de la base de datos
    libro.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
