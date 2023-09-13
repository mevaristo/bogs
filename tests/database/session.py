from bogs.database.engine import database_engine as engine
import bogs.database.service as service
import bogs.database.entities as entities
from sqlalchemy import text
import unittest
from datetime import date


def create_sample_cryptid() -> entities.Cryptid:
    return entities.Cryptid(
        name="Zombie",
        other_names="Undead",
        description="Not dead, not alive, only stops when is hit in the head.",
        wiki_link="https://en.wikipedia.org/wiki/Zombie"
    )


def create_sample_media_list() -> list[entities.Media]:
    return [
        entities.Media(
            description="Zombie in my garden",
            link="https://cdn.pixabay.com/photo/2017/01/27/14/50/zombie-2013270_1280.png"
        ),
        entities.Media(
            description="Zombie in my pool",
            link="https://cdn.pixabay.com/photo/2019/11/28/14/33/zombie-4659324_1280.png"
        )
    ]


def create_sample_sighting() -> entities.Sighting:
    srid = 4326
    lon = -64.9951
    lat = -4.872

    return entities.Sighting(
        description="The day when a zombie appeared in my garden.",
        date=date(1999, 2, 27),
        location=f'SRID={srid};POINT({lon} {lat})'
    )


def create_complete_cryptid() -> entities.Cryptid:
    cryptid = create_sample_cryptid()
    cryptid.media = create_sample_media_list()
    cryptid.sightings = [create_sample_sighting()]

    return cryptid


sample_cryptid = create_sample_cryptid()
sample_sighting = create_sample_sighting()
sample_media = create_sample_media_list()
cryptid_id = 1


class DatabaseTest(unittest.TestCase):
    def setUp(self) -> None:
        return

    def tearDown(self) -> None:
        return

    def test_connection(self):
        test_str = 'connection text'

        with engine.connect() as connection:
            result = connection.execute(text(f"select '{test_str}'"))
            self.assertEqual([(test_str,)], result.all())

    def test_insert(self):
        service.save_cryptid(sample_cryptid)

    def test_sighting_insert(self):
        service.save_cryptid_sighting(sample_sighting, cryptid_id)

    def test_media_insert(self):
        service.save_cryptid_media(sample_media[0], cryptid_id)

    def test_cryptid_obj(self):
        obj = sample_cryptid
        self.assertIsNone(obj.id)

    def test_complete_cryptid(self):
        obj = create_complete_cryptid()
        self.assertIsNotNone(obj.sightings)


if __name__ == '__main__':
    unittest.main()
