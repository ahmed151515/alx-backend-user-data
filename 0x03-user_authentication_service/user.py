#!/usr/bin/env python3
"""cearte user use SQLAlchemy
    """

from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """class for user

    Args:
        base (_type_): _description_
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
