import psycopg2
import os
from settings import get_logger

logger = get_logger(__name__)


def get_connect():
    # Connect to the database
    try:
        conn = psycopg2.connect(
            host=os.getenv('host'),
            port=os.getenv('port'),
            user=os.getenv('user'),
            password=os.getenv('password'),
            database=os.getenv('database')
        )
        return conn
    except Exception as error:
        logger.error(error)
        raise Exception('Возникли проблемы с подключением к БД')


if __name__ == '__main__':
    get_connect()
