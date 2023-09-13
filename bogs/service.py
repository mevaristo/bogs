from sqlalchemy import select
from database.entities import Cryptid
import models as mod


def get_cryptid_by_id(cryptid_id: int) -> mod.Cryptid:
    return mod.Cryptid(select(Cryptid).where(Cryptid.id == cryptid_id))
