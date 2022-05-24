
from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import NullPool


SQL_CONNECTION_STRING = f'postgresql+psycopg2://google_sheets:googlesheets' \
                        f'@0.0.0.0:5430/google_sheets_db'


client = create_engine(SQL_CONNECTION_STRING,
                       echo=False,
                       connect_args={'connect_timeout': 31536000},
                       pool_recycle=-1,
                       poolclass=NullPool,
                       pool_pre_ping=True)

session = Session(client)


def protected_commit():
    """
    Method to create protected commit in data base, in a case troubles during commit
    the will be canceled and there is no any data will be added to data base.
    :return:
    """
    try:
        session.commit()
        session.close()
    except Exception as error:
        logger.error(str(error))
        session.rollback()
        logger.error(str(error))
        raise error