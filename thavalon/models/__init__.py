from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)

    def save(self):
        """
        Save this object to the database. Because of how SQLAlchemy works,
        this will commit the session, flushing any other pending changes
        that have been added.
        """
        db.session.add(self)
        return db.session.commit()

    @classmethod
    def get_one(cls, **kwargs):
        """
        Select one object matching the given filters.
        """
        return cls.query.filter_by(**kwargs).first()
