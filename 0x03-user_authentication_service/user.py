#!/usr/bin/env python3
"""cearte user use SQLAlchemy
    """

from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class User(base):
    """class for user

    Args:
        base (_type_): _description_
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id= Column(String)
    reset_token= Column(String)
