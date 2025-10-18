from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    button = KeyboardButton(text="Sherik kerak")
    button2 = KeyboardButton(text="Ish joyi kerak")
    button3 = KeyboardButton(text="hodim kerak")
    button4 = KeyboardButton(text="Ustoz kerak")
    button5 = KeyboardButton(text="Shogirt kerak")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button, button2],
         [button3, button4],
            [button5],
        ],

        resize_keyboard=True
    )
    return rkm


def back_keyboard():
    button = KeyboardButton(text="🔙 back")
    rkm = ReplyKeyboardMarkup(
        keyboard=[
            [button],
        ],
        resize_keyboard=True
    )
    return rkm




