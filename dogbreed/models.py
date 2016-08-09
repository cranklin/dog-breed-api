from dogbreed.base.models import *
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import joinedload, contains_eager


class Vote(db.Model, ModelDictMixin):
    __tablename__ = 'votes'
    __table_args__ = {'mysql_charset': 'utf8', 'mysql_engine': 'InnoDB'}
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.id'), primary_key=True)
    dog = db.relationship("Dog", back_populates="votes")
    counter = db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        super(Vote, self).__init__()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def __repr__(self):
        return '<Vote %r>' % self.dog_id


class Breed(BaseModel):
    __tablename__ = 'breeds'
    __table_args__ = {'mysql_charset': 'utf8', 'mysql_engine': 'InnoDB'}
    breed_name = db.Column(db.String(80), unique=True, index=True)
    dogs = db.relationship("Dog", back_populates='breed')

    def __init__(self, **kwargs):
        super(Breed, self).__init__()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def __repr__(self):
        return '<Breed %r>' % self.breed_name


class Dog(BaseModel):
    __tablename__ = 'dogs'
    __table_args__ = {'mysql_charset': 'utf8', 'mysql_engine': 'InnoDB'}
    photo_url = db.Column(db.String(255), unique=True)
    dog_name = db.Column(db.String(80))
    dog_description = db.Column(db.Text)
    breed_id = db.Column(db.Integer, db.ForeignKey('breeds.id'))
    breed = db.relationship("Breed", back_populates="dogs")
    votes = db.relationship("Vote", uselist=False, back_populates="dog")


    def __init__(self, **kwargs):
        super(Dog, self).__init__()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def __repr__(self):
        return '<Dog %r>' % self.id


class Client(BaseModel):
    __tablename__ = 'clients'
    __table_args__ = {'mysql_charset': 'utf8', 'mysql_engine': 'InnoDB'}
    client_name = db.Column(db.String(80))

    def __init__(self, **kwargs):
        super(Client, self).__init__()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    def __repr__(self):
        return '<Client %r>' % self.client_name


