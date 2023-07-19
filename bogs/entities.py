from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

DBAPI = 'psycopg2'
USER = 'bogs'
PASSWORD = 'pg_pass'
HOST = '127.0.0.1'
PORT = '5432'
DB = 'bogs_db'
CONNECTION_URL = f'postgresql+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'

engine = create_engine(CONNECTION_URL)

metadata = MetaData()

cryptids = Table('cryptids', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('other_names', String),
                 Column('description', String),
                 Column('wiki', String))

metadata.create_all(engine)
