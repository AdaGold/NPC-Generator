from flask import Blueprint, request, abort, make_response
from ..db import db
from ..models.character import Character
from ..models.greeting import Greeting
from sqlalchemy import func, union, except_

bp = Blueprint("characters", __name__, url_prefix="/characters")


@bp.post("")
def create_character():

    request_body = request.get_json()
    try:
        new_character = Character.from_dict(request_body)
        db.session.add(new_character)
        db.session.commit()

        return new_character.to_dict(), 201

    except KeyError as e:
        abort(make_response({"message": f"missing required value: {e}"}, 400))


@bp.get("")
def get_characters():
    character_query = db.select(Character)

    characters = db.session.scalars(character_query)
    response = [character.to_dict() for character in characters]

    return response


@bp.get("/<char_id>")
def get_character(char_id):
    character = validate_model(Character, char_id)
    return character.to_dict()


@bp.get("/<char_id>/greetings")
def get_greetings(char_id):
    pass


@bp.post("/<char_id>/generate")
def add_greetings(char_id):
    pass


def generate_greetings(character):
    pass


def validate_model(cls, id):
    try:
        id = int(id)
    except:
        response = {"message": f"{cls.__name__} {id} invalid"}
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == id)
    model = db.session.scalar(query)
    if model:
        return model

    response = {"message": f"{cls.__name__} {id} not found"}
    abort(make_response(response, 404))
