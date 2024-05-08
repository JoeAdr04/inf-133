def render_libro_list(libros):
    return{
        {
            "id": libro.id,
            "title": libro.title,
            "autor": libro.autor,
            "edicion": libro.edicion,
            "disponibility": libro.disponibility
        }
        for libro in libros
    }

def render_libro_detail(libro):
    return{
        "id": libro.id,
        "title": libro.title,
        "autor": libro.autor,
        "edicion": libro.edicion,
        "disponibility": libro.disponibility
    }