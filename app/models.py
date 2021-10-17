from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

from .db import DatabaseBase


class Business(DatabaseBase):
    __tablename__ = 'business'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True)
    identity = Column(String, unique=True, index=True)
    has_premium = Column(Boolean)


class User(DatabaseBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey('business.id', ondelete='CASCADE'))

    email = Column(String, index=True)
    first_name = Column(String)
    last_name = Column(String)
    is_admin = Column(Boolean)


class Testimonial(DatabaseBase):
    __tablename__ = 'testimonial'

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey('business.id', ondelete='CASCADE'))

    is_accepted = Column(Boolean)
    name = Column(String)
    title = Column(String)
    business_name = Column(String)
    picture_url = Column(String)
    text = Column(String)
    audio_url = Column(String)
    video_url = Column(String)
