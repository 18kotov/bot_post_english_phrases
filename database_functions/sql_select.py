from settings import get_logger
from database_functions.commucation_with_db import get_data

logger = get_logger(__name__)


@get_data
def get_phrases_x_days_ago(x: int) -> list:
    phrases = f"SELECT russian, english FROM phrases WHERE date = CURRENT_DATE - INTERVAL '{x} days';"
    return phrases



if __name__ == '__main__':
    pass
