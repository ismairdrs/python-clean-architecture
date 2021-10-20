import enum
from sqlalchemy import Column, String, Integer, ForeignKey, Enum

from src.infra.config import Base


class AnimalTypes(enum.Enum):
    """defining anymals types"""

    DOG = "dog"
    CAT = "cat"
    FISH = "fish"
    TURTLE = "turtle"


class Pets(Base):
    """database pets"""

    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self) -> str:
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}]"

    def __eq__(self, other):
        return all(
            [
                self.id == other.id,
                self.name == other.name,
                self.specie == other.specie,
                self.age == other.age,
                self.user_id == other.user_id,
            ]
        )
