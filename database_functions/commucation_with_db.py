from settings import get_logger
from database_functions.my_connect import get_connect

logger = get_logger(__name__)


def post_query(func):
    def wrapper(*args, **kwargs):
        conn = get_connect()
        cursor = conn.cursor()
        try:
            query = func(*args, **kwargs)
            cursor.execute(query)
            conn.commit()
            logger.debug('operation is Done!')
        except Exception as error:
            logger.error(error)
            return str(error)
        finally:
            cursor.close()
            conn.close()
        return 'Данные успешно добавлены в БД'
    return wrapper


def get_data(func):
    def wrapper(*args, **kwargs) -> list:
        query = func(*args, **kwargs)
        conn = get_connect()
        cursor = conn.cursor()
        try:
            cursor.execute(query)
            row = cursor.fetchall()
            return row
        except Exception as error:
            logger.error(error)
        finally:
            cursor.close()
            conn.close()

    return wrapper


def get_value(func):
    def wrapper(*args, **kwargs) -> str:
        result = func(*args, **kwargs)
        if result:
            return result[0][0]

    return wrapper


def get_raw(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)[0]
        if result:
            return result[0]

    return wrapper
