from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text



class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(100))
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"<User {self.username}>"