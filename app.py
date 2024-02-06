import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from config import TOKEN
# Подтягивание токена из скрытого конфига
bot = Bot(token=TOKEN)


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Ответ на стартовую команду
    """
    await message.answer(f"Салам, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: types.Message) -> None:
    """
    Обработчик перенаправит полученное сообщение обратно отправителю
    По умолчанию обработчик сообщений обрабатывает все типы сообщений (текст, фотографию, стикер т.д.)
    """
    try:
        # Отправит копию полученного сообщения
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # отработка ошибок
        await message.answer("Cтрах потерял?")


async def main() -> None:
    # Инициализация экземпляра бота с режимом анализа по умолчанию, который будет передаваться всем вызовам API
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())