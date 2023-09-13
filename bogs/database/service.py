from sqlalchemy import select
from sqlalchemy.orm import Session
from entities import Cryptid, Media, Sighting


def get_cryptid_by_id(cryptid_id: int) -> Cryptid:
    result = Session.execute(
        select(Cryptid).where(Cryptid.id == cryptid_id)
    ).first()

    return result

def save_cryptid(cryptid: Cryptid) -> int:
    Session.add(cryptid)