Python 3.10.13 + SQLModel 0.0.16 + SQLAlchemy 2.0 Mapped attribute error:

sqlalchemy.exc.InvalidRequestError: When initializing mapper Mapper[User(user)], expression "relationship('list[Address]')" seems to be using a generic class as the argument to relationship(); please state the generic argument using an annotation, e.g. "addresses: Mapped[list['Address']] = relationship()"

When wrapping with Mapped:
sqlalchemy.exc.InvalidRequestError: When initializing mapper Mapper[User(user)], expression "relationship('Mapped[list[Address]]')" seems to be using a generic class as the argument to relationship(); please state the generic argument using an annotation, e.g. "addresses: Mapped[Mapped[list['Address]']] = relationship()"

Reproduction steps:
1. create venv + activate
2. make install (pip install -r requirements)
3. make run (python main.py) -> Error

Branch: https://github.com/verdude/sqlmodel-forward-refs/tree/sa14 forward reference issue with SQLModel 0.0.9 + SQLAlchemy 1.4
