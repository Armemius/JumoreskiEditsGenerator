from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    Boolean,
)
from storage.base import Base


class TextData(Base):
    __tablename__ = "TextData"

    Id = Column(Integer, primary_key=True, autoincrement=True)
    hash = Column(BigInteger, nullable=False)
    text = Column(String, nullable=False)
    likes = Column(Integer, nullable=True)
    reposts = Column(Integer, nullable=True)
    used = Column(Boolean, nullable=False)
