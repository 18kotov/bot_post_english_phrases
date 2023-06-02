import os
import time
import datetime
from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart, Command
from logic.prepare_info import get_list_messages_for_today, get_quantity_phrases_repeat_today
from settings import get_logger


logger = get_logger(__name__)

user1 = int(os.getenv('user1'))
user2 = int(os.getenv('user2'))
users = {user1, user2}

router = Router()


@router.message(CommandStart(), F.from_user.id.in_(users))
async def get_start(message: Message, bot):
    logger.debug('Получена комманда start')
    await message.answer(f'Привет {message.from_user.first_name}. Начнем!')
    chat_id = message.chat.id
    await send_periodic_messages(bot, chat_id)


@router.message(Command("today"), F.from_user.id.in_(users))
async def get_start(message: Message):
    logger.debug('Получена комманда today')
    quantity = get_quantity_phrases_repeat_today()
    await message.answer(f'ок. сегодня повторяем фраз: {quantity}')
    logger.debug('Отправленно сообщение с количеством фраз')


async def send_periodic_messages(bot, chat_id):
    list_message = get_list_messages_for_today()
    logger.debug(f'Длина списка фраз на сегодня: {len(list_message)}')
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().time()
        start_time = datetime.time(hour=9, minute=0)
        end_time = datetime.time(hour=20, minute=0)
        if start_time <= current_time <= end_time:
            for message in list_message:
                msg_rus = await bot.send_message(chat_id, message['russian'])
                logger.debug(f'send english phrase')
                time.sleep(60)
                msg_eng = await bot.send_message(chat_id, message['english'])
                logger.debug(f'send russian phrase')
                time.sleep(900)
                await bot.delete_message(chat_id=chat_id, message_id=msg_rus.message_id)
                logger.debug(f'delete russian phrase')
                await bot.delete_message(chat_id=chat_id, message_id=msg_eng.message_id)
                logger.debug(f'delete english phrase')


if __name__ == "__main__":
    pass
