import os
import time
import datetime
from aiogram.types import Message
from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart, Command
from logic.prepare_info import get_list_messages_for_today, get_quantity_phrases_repeat_today, get_list_messages_day
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
    list_message = get_list_messages_for_today()
    await send_periodic_messages(bot, chat_id, list_message)


@router.message(Command("1_day"), F.from_user.id.in_(users))
async def day1(message: Message, bot):
    logger.debug('Получена комманда 1_day')
    await message.answer(f'Привет {message.from_user.first_name}. Начнем повтор вчерашних фраз!')
    chat_id = message.chat.id
    list_message = get_list_messages_day(1)
    await message.answer(f'Кол-во фраз {len(list_message)}')
    await send_periodic_messages(bot, chat_id, list_message)


@router.message(Command("3_day"), F.from_user.id.in_(users))
async def day3(message: Message, bot):
    logger.debug('Получена комманда 3_day')
    await message.answer(f'Привет {message.from_user.first_name}. Начнем повтор фраз добавленных 3 дня назад!')
    chat_id = message.chat.id
    list_message = get_list_messages_day(3)
    await message.answer(f'Кол-во фраз {len(list_message)}')
    await send_periodic_messages(bot, chat_id, list_message)


@router.message(Command("7_day"), F.from_user.id.in_(users))
async def day7(message: Message, bot):
    logger.debug('Получена комманда 7_day')
    await message.answer(f'Привет {message.from_user.first_name}. Начнем повтор фраз добавленных 7 дней назад!')
    chat_id = message.chat.id
    list_message = get_list_messages_day(7)
    await message.answer(f'Кол-во фраз {len(list_message)}')
    await send_periodic_messages(bot, chat_id, list_message)


@router.message(Command("12_day"), F.from_user.id.in_(users))
async def day12(message: Message, bot):
    logger.debug('Получена комманда 12_day')
    await message.answer(f'Привет {message.from_user.first_name}. Начнем повтор фраз добавленных 12 дней назад!')
    chat_id = message.chat.id
    list_message = get_list_messages_day(12)
    await message.answer(f'Кол-во фраз {len(list_message)}')
    await send_periodic_messages(bot, chat_id, list_message)


@router.message(Command("16_day"), F.from_user.id.in_(users))
async def day16(message: Message, bot):
    logger.debug('Получена комманда 16_day')
    await message.answer(f'Привет {message.from_user.first_name}. Начнем повтор фраз добавленных 16 дней назад!')
    chat_id = message.chat.id
    list_message = get_list_messages_day(16)
    await message.answer(f'Кол-во фраз {len(list_message)}')
    await send_periodic_messages(bot, chat_id, list_message)


@router.message(Command("35_day"), F.from_user.id.in_(users))
async def day35(message: Message, bot):
    logger.debug('Получена комманда 35_day')
    await message.answer(f'Привет {message.from_user.first_name}. Начнем повтор фраз добавленных 35 дней назад!')
    chat_id = message.chat.id
    list_message = get_list_messages_day(35)
    await message.answer(f'Кол-во фраз {len(list_message)}')
    await send_periodic_messages(bot, chat_id, list_message)


@router.message(Command("50_day"), F.from_user.id.in_(users))
async def day50(message: Message, bot):
    logger.debug('Получена комманда 50_day')
    await message.answer(f'Привет {message.from_user.first_name}. Начнем повтор фраз добавленных 50 дней назад!')
    chat_id = message.chat.id
    list_message = get_list_messages_day(50)
    await message.answer(f'Кол-во фраз {len(list_message)}')
    await send_periodic_messages(bot, chat_id, list_message)


@router.message(Command("today"), F.from_user.id.in_(users))
async def get_start(message: Message):
    logger.debug('Получена комманда today')
    quantity = get_quantity_phrases_repeat_today()
    await message.answer(f'ок. сегодня повторяем фраз: {quantity}')
    logger.debug('Отправленно сообщение с количеством фраз')


async def send_periodic_messages(bot, chat_id, list_message):
    logger.debug(f'Длина списка фраз на сегодня: {len(list_message)}')
    for message in list_message:
        msg_rus = await bot.send_message(chat_id, message['russian'])
        logger.debug(f'send english phrase')
        time.sleep(60)
        msg_eng = await bot.send_message(chat_id, message['english'])
        logger.debug(f'send russian phrase')
        time.sleep(300)
        await bot.delete_message(chat_id=chat_id, message_id=msg_rus.message_id)
        logger.debug(f'delete russian phrase')
        await bot.delete_message(chat_id=chat_id, message_id=msg_eng.message_id)
        logger.debug(f'delete english phrase')


if __name__ == "__main__":
    pass
