from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship



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
    
class Choice(Base):
    ORDER_STATUSES = (
        ("pending", "Pending"),
        ("in-transit", "In Transit"),
        ("delivered", "Delivered"),
        ("cancelled", "Cancelled")
    )

    PIZZA_SIZES = (
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large"),
        ("extra-large", "Extra Large")
    )
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(String(10), default="pending", choices=ORDER_STATUSES)
    pizza_size = Column(String(10), choices=PIZZA_SIZES)
    user_id = Column(Integer, ForeignKey("user.id"))

    def __repr__(self):
        return f"<Order {self.id}>"




User.orders = relationship("Choice", back_populates="user")
Choice.user = relationship("User", back_populates="orders")
