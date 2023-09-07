from typing import List
from typing import Tuple
from datetime import date
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from geoalchemy2 import Geometry
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Cryptid(Base):
    __tablename__ = "cryptid"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    other_names: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    wiki_link: Mapped[str] = mapped_column(String)
    media: Mapped[List["Media"]] = relationship(
        back_populates="cryptid", cascade="all"
    )
    sightings: Mapped[List["Sighting"]] = relationship(
        back_populates="cryptid", cascade="all"
    )


class Media(Base):
    __tablename__ = "media"

    id: Mapped[int] = mapped_column(primary_key=True)
    cryptid_id: Mapped[int] = mapped_column(ForeignKey("cryptid.id"))
    cryptid: Mapped["Cryptid"] = relationship(
        back_populates="media"
    )
    sighting_id: Mapped[int] = mapped_column(ForeignKey("sighting.id"))
    sighting: Mapped["Sighting"] = relationship(
        back_populates="media"
    )

    description: Mapped[str] = mapped_column(String)
    link: Mapped[str] = mapped_column(String)
    blob: Mapped[str] = mapped_column(String)


class Sighting(Base):
    __tablename__ = "sighting"

    id: Mapped[int] = mapped_column(primary_key=True)
    cryptid_id: Mapped[int] = mapped_column(ForeignKey("cryptid.id"))
    cryptid: Mapped["Cryptid"] = relationship(
        back_populates="sightings"
    )
    media: Mapped[List["Media"]] = relationship(
        back_populates="sighting", cascade="all"
    )
    description: Mapped[str] = mapped_column(String)
    date: Mapped[date] = mapped_column(Date)
    location: Mapped[Tuple[float, float]] = mapped_column(Geometry('POINT'))