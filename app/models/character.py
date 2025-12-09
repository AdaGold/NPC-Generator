from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db


class Character(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    personality: Mapped[str]
    occupation: Mapped[str]
    age: Mapped[int]
    greetings: Mapped[list["Greeting"]] = relationship(back_populates="character")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "personality": self.personality,
            "occupation": self.occupation,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, data_dict):
        new_character = cls(
            name=data_dict["name"],
            personality=data_dict["personality"],
            occupation=data_dict["occupation"],
            age=data_dict["age"]
        )

        return new_character
