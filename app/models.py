from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

from .db import DatabaseBase


class Business(DatabaseBase):
    __tablename__ = 'business'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True)
    identity = Column(String, unique=True, index=True)
    created_on = Column(Integer)

    users = relationship('User', back_populates='business')
    testimonials = relationship('Testimonial', back_populates='business')
    testimonial_requests = relationship('TestimonialRequest', back_populates='business')


class User(DatabaseBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey('business.id', ondelete='CASCADE'))

    email = Column(String, index=True)
    name = Column(String)
    is_admin = Column(Boolean)
    created_on = Column(Integer)

    business = relationship('Business', back_populates='users')


class TestimonialRequest(DatabaseBase):
    __tablename__ = 'testimonialrequest'

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey('business.id', ondelete='CASCADE'))

    public_id = Column(String, index=True, unique=True)
    created_on = Column(Integer)

    business = relationship('Business', back_populates='testimonial_requests')


class Testimonial(DatabaseBase):
    __tablename__ = 'testimonial'

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, ForeignKey('business.id', ondelete='CASCADE'))

    created_on = Column(Integer)
    is_accepted = Column(Boolean)
    giver_name = Column(String)
    giver_title = Column(String)
    business_name = Column(String)
    picture_url = Column(String)
    text = Column(String, default='')
    video_url = Column(String, default='')

    business = relationship('Business', back_populates='testimonials')
