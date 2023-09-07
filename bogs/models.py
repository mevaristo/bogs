import datetime

from pydantic import BaseModel


class Media(BaseModel):
    id: int
    cryptid_id: int
    sighting_id: int
    description: int
    link: str
    blob: str


class Cryptid(BaseModel):
    id: int
    name: str
    other_names: str
    description: str
    wiki_link: str


class Sighting(BaseModel):
    id: int
    cryptid_id: int
    description: str
    date: datetime.date
    location: tuple[float, float]
