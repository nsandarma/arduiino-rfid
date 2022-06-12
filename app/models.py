from app import SQLAlchemy,UserMixin,db

class Data_card(db.Model,UserMixin):
    __tablename__ = 'data_card'
    id = db.Column(db.Integer,primary_key=True)
    nama = db.Column(db.String,nullable=False)
    nim = db.Column(db.String,nullable=False,unique=True)
    email = db.Column(db.String,nullable=False,unique=True)
    password_portal = db.Column(db.String,nullable=False)
    # token = db.Column(db.Integer,nullable=False,unique=True)
    id_card = db.Column(db.String,nullable=False,unique=True)
    data = db.Column(db.String)

    def __repr__(self) -> str:
        return f'< data :  {self.nama}>'
