from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, FSInputFile
from data.database import Database
from config import Config, load_config

from lexicon import lexicon
from keyboards import start_keyboard

# config: Config = load_config()
# base = Database(config.db.database)
#
# router: Router = Router()

# @router.callback_query()
# async def callback_answer(call: CallbackQuery):
#     #колбэки - continue_1, continue_2, cancel
#     if call.data == 'cancel':
#         #сделать
#         await call.message.answer(text=lexicon.cancel, reply_markup=None)
#     if call.data == 'continue_1':
#         await call.message.edit_text(text='Продолжение', reply_markup=callback_2_keyboard)
#     if call.data == 'continue_2':
#         await call.message.edit_text(text='Продолжение 2', reply_markup=callback_3_keyboard)
#     if call.data == 'continue_3':
#         await call.message.edit_text(text='Продолжение 3')#, reply_markup=callback_3_keyboard)

#
# @router.message(CommandStart())
# async def start_answer(message: Message):
#     base.add_user(message.from_user.id, message.from_user)
#     await message.answer(text=lexicon.start, reply_markup=start_keyboard)

# @router.message(F.text.lower().contains('about'))
# async def about(message: Message):
#     #photo = FSInputFile('/root/bot/images/EngVers.png', 'rb')
#     #await message.answer_photo(photo, caption=LEXICON_EN.about, reply_markup=start_keyboard)
#     await message.answer(text=lexicon.about, reply_markup=start_keyboard)
#
# @router.message(F.text.lower().contains('sample'))
# async def sample(message: Message):
#     await message.answer(text=lexicon.sample, reply_markup=sample_keyboard)
#
#     await message.answer(text=lexicon.reserve_info, reply_markup=start_keyboard)

# @router.message()
# async def other(message: Message):
#     await message.answer(text=lexicon.sorry, reply_markup=start_keyboard)

