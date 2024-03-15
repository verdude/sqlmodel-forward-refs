from __future__ import annotations


from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: int | None = Column(Integer, primary_key=True)
    name: str = Column(String)
    addresses: list[Address] = relationship(
        "Address", back_populates="user", uselist=True
    )


class Address(Base):
    __tablename__ = "addresses"

    id: int | None = Column(Integer, primary_key=True)
    email: str = Column(String)
    user_id: int = Column(Integer, ForeignKey("users.id"))
    user: User = relationship("User", back_populates="addresses", uselist=False)


engine = create_engine("sqlite:///example.db", echo=True)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

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
