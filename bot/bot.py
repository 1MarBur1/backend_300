import asyncio
import logging

from dataclasses import dataclass

from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram import Bot, Dispatcher
from data.database import Database
from config import Config, load_config

from aiogram.types import InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

@dataclass
class lexicon:
    #фразы
    start = '<b>Приветствую!</b>\nВы попали в приложение, помогающее улучшать экологию Екатеринбурга.'
    sorry = 'Извините, я вас не понимаю :('
    # кнопки
    webapp_button = 'Открыть приложение'

#стартовая клавиатура
app_btn = InlineKeyboardButton(text=lexicon.webapp_button, web_app=WebAppInfo(url='https://notbaryga.github.io/webapp/index.html'))
start_keyboard = InlineKeyboardBuilder().row(app_btn).as_markup()

# Инициализируем логгер
logger = logging.getLogger(__name__)

# Загружаем конфиг в переменную config
config: Config = load_config()

# Инициализируем бот и диспетчер и бд
bot: Bot = Bot(token=config.tg_bot.token,
               parse_mode='HTML')
base = Database(config.db.database)

dp: Dispatcher = Dispatcher()

@dp.message(CommandStart())
async def start_answer(message: Message):
    base.add_user(message.from_user.id, message.from_user)
    await message.answer(text=lexicon.start, reply_markup=start_keyboard)

@dp.message()
async def other(message: Message):
    await message.answer(text=lexicon.sorry, reply_markup=start_keyboard)

# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())