from sqlalchemy import select
from sqlalchemy.orm import Session
from .engine import database_engine as engine
from .entities import Cryptid, Media, Sighting


def get_cryptid_by_id(cryptid_id: int) -> Cryptid | None:
    with Session(engine) as session:
        cryptid = session.get(Cryptid, cryptid_id)
        return cryptid


def save_cryptid(cryptid: Cryptid):
    with Session(engine) as session:
        with session.begin():
            session.add(cryptid)


def save_cryptid_sighting(sighting: Sighting, cryptid_id: int):
    with Session(engine) as session:
        with session.begin():
            cryptid = session.get(Cryptid, cryptid_id)
            cryptid.sightings.append(sighting)
            session.add(cryptid)


def save_cryptid_media(media: Media, cryptid_id: int):
    with Session(engine) as session:
        with session.begin():
            cryptid = session.get(Cryptid, cryptid_id)
            cryptid.media.append(media)
            session.add(cryptid)


def delete_cryptid(cryptid: Cryptid):
    with Session(engine) as session:
        with session.begin():
            session.delete(cryptid)


def update_cryptid(cryptid: Cryptid):
    with Session(engine) as session:
        with session.begin():
            session.add(cryptid)
