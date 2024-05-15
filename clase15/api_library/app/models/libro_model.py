from database import db


# Define la clase `Libro` que hereda de `db.Model`
# `Libro` representa la tabla `Libros` en la base de datos
class Libro(db.Model):
    __tablename__ = "Libros"

    # Define las columnas de la tabla `Libros`
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    edicion = db.Column(db.Integer, nullable=False)
    dispo = db.Column(db.Integer, nullable=False)

    # Inicializa la clase `Libro`
    def __init__(self, titulo, autor, edicion,dispo):
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.dispo = dispo

    # Guarda un Libro en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los Libroes de la base de datos
    @staticmethod
    def get_all():
        return Libro.query.all()

    # Obtiene un Libro por su ID
    @staticmethod
    def get_by_id(id):
        return Libro.query.get(id)

    # Actualiza un Libro en la base de datos
    def update(self, titulo=None, autor=None, edicion=None, dispo=None):
        if titulo is not None:
            self.titulo = titulo
        if autor is not None:
            self.autor = autor
        if edicion is not None:
            self.edicion = edicion
        if dispo is not None:
            self.dispo = dispo
        db.session.commit()

    # Elimina un Libro de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()
