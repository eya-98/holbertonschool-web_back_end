#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import User, Base
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """ DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        add user
        """
        DBSession = self._session
        new_user = User(email=email, hashed_password=hashed_password)
        DBSession.add(new_user)
        DBSession.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """takes in arbitrary keyword arguments and returns the first
        row found in the users table as filtered by the method’s
        input arguments"""
        DBSession = self._session
        query = DBSession.query(User).filter_by(**kwargs)
        result = query.first()
        if (result is None):
            raise NoResultFound
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """The method will use find_user_by to locate the user to update,
        then will update the user’s attributes as passed in the method’s
        arguments then commit changes to the database"""
        DBSession = self._session
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if hasattr(user, key) is False:
                raise ValueError
            setattr(user, key, value)
        DBSession.commit()
