from __future__ import annotations

from sqlalchemy import Column, UnicodeText
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, Relationship, SQLModel, create_engine


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(sa_column=Column(UnicodeText()))
    addresses: list["Address"] = Relationship(
        back_populates="user", sa_relationship_kwargs={"uselist": True}
    )


class Address(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(sa_column=Column(UnicodeText()))
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(
        back_populates="addresses", sa_relationship_kwargs={"uselist": False}
    )


engine = create_engine("sqlite:///example.db", echo=True)
Session = sessionmaker(engine)

SQLModel.metadata.create_all(engine)

session = Session()

new_user = User(name="John Doe")
new_address = Address(email="johndoe@example.com", user=new_user)
session.add(new_user)
session.add(new_address)
session.commit()

user = session.query(User).first()
if user is not None:
    print(f"User: {user.name}, Email: {user.addresses[0].email}")

session.close()
