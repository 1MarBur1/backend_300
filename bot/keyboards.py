from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon import lexicon

#стартовая клавиатура
app_btn = InlineKeyboardButton(text=lexicon.webapp_button, web_app=WebAppInfo(url='https://notbaryga.github.io/webapp/index.html'))
point_btn = InlineKeyboardButton(text=lexicon.create_point_button, callback_data='continue_1')
start_keyboard = InlineKeyboardBuilder().row(app_btn).as_markup()

#колбэк клавиатура для 1 шага
continue_btn = InlineKeyboardButton(text=lexicon.continue_button, callback_data='continue_2')
cancel_btn = InlineKeyboardButton(text=lexicon.cancel_button, callback_data='cancel')
callback_1_keyboard = InlineKeyboardBuilder().row(continue_btn).row(cancel_btn).as_markup()

#колбэк клавиатура для 2 шага
continue_btn = InlineKeyboardButton(text=lexicon.continue_button, callback_data='continue_2')
cancel_btn = InlineKeyboardButton(text=lexicon.cancel_button, callback_data='cancel')
callback_2_keyboard = InlineKeyboardBuilder().row(continue_btn).row(cancel_btn).as_markup()

#колбэк клавиатура для 3 шага
continue_btn = InlineKeyboardButton(text=lexicon.continue_button, callback_data='continue_3') #поменять
cancel_btn = InlineKeyboardButton(text=lexicon.cancel_button, callback_data='cancel')
callback_3_keyboard = InlineKeyboardBuilder().row(continue_btn).row(cancel_btn).as_markup()

# #клавиатура для отправки запроса payeer
# request_btn = InlineKeyboardButton(text=lexicon.send_request_button, url=payeer_invite_link)
# ready_btn = InlineKeyboardButton(text=lexicon.ready_button, callback_data='payeer')
# payeer_kb = InlineKeyboardBuilder().row(request_btn, ready_btn).as_markup()
#
# #клавиатура для отправки запроса other
# request2_btn = InlineKeyboardButton(text=lexicon.send_request_button, url=other_invite_link)
# ready_btn = InlineKeyboardButton(text=lexicon.ready_button, callback_data='other')
# other_kb = InlineKeyboardBuilder().row(request2_btn, ready_btn).as_markup()
#
# #клавиатура для проверки оплаты payeer
# paid_btn = InlineKeyboardButton(text=lexicon.paid_button, callback_data='check')
# paid_keyboard = InlineKeyboardBuilder().row(paid_btn).as_markup()
#
# #клавиатура для пробника
# btn_sample = InlineKeyboardButton(text=lexicon.see_sample_button, url=sample_folder)
# sample_keyboard = InlineKeyboardBuilder().row(btn_sample).as_markup()
