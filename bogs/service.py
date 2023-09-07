from sqlalchemy import select
from database.entities import Cryptid


def get_cryptid_by_id(cryptid_id: int):
    return select(Cryptid).where(Cryptid.id == cryptid_id)
