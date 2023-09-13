from typing import List
from datetime import date, datetime
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from geoalchemy2 import Geometry
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import registry
from sqlalchemy import func

mapper_registry = registry()


@mapper_registry.mapped_as_dataclass
class Cryptid:
    __tablename__ = "cryptid"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    other_names: Mapped[str] = mapped_column(String, default=None)
    description: Mapped[str] = mapped_column(String, default=None)
    wiki_link: Mapped[str] = mapped_column(String, default=None)
    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.current_timestamp(), default=None
    )
    media: Mapped[List["Media"]] = relationship(
        default_factory=list, back_populates="cryptid", cascade="all"
    )
    sightings: Mapped[List["Sighting"]] = relationship(
        default_factory=list, back_populates="cryptid", cascade="all"
    )


@mapper_registry.mapped_as_dataclass
class Media:
    __tablename__ = "media"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    cryptid: Mapped["Cryptid"] = relationship(
        init=False, back_populates="media"
    )
    sighting: Mapped["Sighting"] = relationship(
        init=False, back_populates="media"
    )

    cryptid_id: Mapped[int] = mapped_column(ForeignKey("cryptid.id"), default=None)
    sighting_id: Mapped[int] = mapped_column(ForeignKey("sighting.id"), default=None)

    description: Mapped[str] = mapped_column(String, default=None)
    link: Mapped[str] = mapped_column(String, default=None)
    blob: Mapped[str] = mapped_column(String, default=None)

    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.current_timestamp(), default=None
    )


@mapper_registry.mapped_as_dataclass
class Sighting:
    __tablename__ = "sighting"

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    cryptid_id: Mapped[int] = mapped_column(ForeignKey("cryptid.id"), default=None, init=False)
    cryptid: Mapped["Cryptid"] = relationship(
        init=False, back_populates="sightings"
    )
    media: Mapped[List["Media"]] = relationship(
        init=False, default_factory=list, back_populates="sighting", cascade="all"
    )
    description: Mapped[str] = mapped_column(String, default=None)
    date: Mapped[date] = mapped_column(Date, default=None)
    location: Mapped[str] = mapped_column(Geometry('POINT'), default=None)

    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.current_timestamp(), default=None
    )

