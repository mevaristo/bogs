from entities import Base
from sqlalchemy import create_engine

DBAPI = 'psycopg2'
USER = 'bogs'
PASSWORD = 'pg_pass'
HOST = '127.0.0.1'
PORT = '5432'
DB = 'bogs_db'
CONNECTION_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}'

database_engine = create_engine(CONNECTION_URL, echo=True)
Base.metadata.create_all(database_engine)
