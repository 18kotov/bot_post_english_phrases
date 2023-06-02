from typing import List, Union
from database_functions.sql_select import get_phrases_x_days_ago
from settings import get_logger

logger = get_logger(__name__)


def get_list_messages_for_today() -> List[dict]:
    logger.debug('старт сбора фраз на сегодня')
    intervals = [1, 3, 7, 12, 16, 35, 50]
    list_phrases = []
    for x in intervals:
        list_tuple = get_phrases_x_days_ago(x)
        list_dict = [tuple_to_dict(x) for x in list_tuple]
        list_phrases.extend(list_dict)
    logger.debug('список фраз на сегодня собран')
    return list_phrases


def get_list_phrases(list_tuple: Union[List[tuple], None]) -> List[str]:
    list_phrases = []
    if list_tuple is None:
        return list_phrases
    for x in list_tuple:
        list_phrases.append(x[0])

    return list_phrases


def tuple_to_dict(input: tuple) -> dict:
    phrases_dict = {'english': input[1], 'russian': input[0]}
    return phrases_dict


def get_quantity_phrases_repeat_today() -> int:
    logger.debug('получаем длину списка фраз на сегодня')
    quantity = 0
    try:
        quantity = len(get_list_messages_for_today())
    except Exception as error:
        logger.error(error)

    return quantity


if __name__ == "__main__":
    pass
