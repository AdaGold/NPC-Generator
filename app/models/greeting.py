from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db


class Greeting(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    greeting_text: Mapped[str]
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    character: Mapped["Character"] = relationship(back_populates="greetings")

    def to_dict(self):
        return {
            "id": self.id,
            "greeting": self.greeting_text,
        }
