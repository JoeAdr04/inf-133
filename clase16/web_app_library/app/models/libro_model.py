from database import db

class Libro(db.Model):
    __tablename__ = "libros"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(), nullable=False)
    edicion = db.Column(db.Integer, nullable=False)
    dispo = db.Column(db.String(100), nullable=False)

    def __init__ (self,titulo, autor, edicion, dispo):
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.dispo = dispo

    def sava(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Libro.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Libro.query.get(id)
    
    def update(self, titulo=titulo, autor=  autor, edicion=edicion, dispo=dispo):
        if titulo is not None:
            self.titulo = titulo
        if autor is not None:
            self.autor = autor
        if edicion is not None:
            self.edicion = edicion
        if dispo is not  None:
            self.dispo = dispo
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()