from database import db

class Libro(db.Model):
    __tablename__ = "libros"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = True)
    autor = db.Column(db.String(100), nullable = True)
    edicion = db.Column(db.Integer, nullable = True)
    disponibility = db.Column(db.String(100), nullable = True)

    def __init__(self, title, autor, edicion, disponibility):
        self.title = title
        self.autor = autor
        self.edicion = edicion
        self.disponibility = disponibility

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Libro.query.all()
    
    def get_by_id(id):
        return Libro.query.get(id)
    
    def update (self, title=None, autor=None, edicion = None, disponibility=None):
        if title is not None:
            self.title = title
        if autor is not None:
            self.autor = autor
        if edicion is not None:
            self.edicion = edicion        
        if disponibility is not None:
            self.disponibility = disponibility
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()