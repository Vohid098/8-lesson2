from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def about_inline_keyboard():
    button = InlineKeyboardButton(text="Fullname", callback_data="fullname")
    button2 = InlineKeyboardButton(text="Photo", callback_data="photo")
    button3 = InlineKeyboardButton(text="Job", callback_data="job")
    button4 = InlineKeyboardButton(text="Back", callback_data="back")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2, button3],
            [button4]
        ],
    )
    return ikm


def photo_inline_keyboard():
    button = InlineKeyboardButton(text="👍 like", callback_data="like")
    button2 = InlineKeyboardButton(text="👎 dislike", callback_data="dislike")
    button3 = InlineKeyboardButton(text="Back", callback_data="back2")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2],
            [button3]
        ],
    )
    return ikm


def media_inline_keyboard():
    button = InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/shohruh_abdurahmon/")
    button2 = InlineKeyboardButton(text="Youtube", url="https://www.youtube.com/@Shoxdev")
    button3 = InlineKeyboardButton(text="Telegram", url="https://t.me/shohruh_abdurahmon")
    button4 = InlineKeyboardButton(text="Back", callback_data="back3")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button, button2, button3],
            [button4]
        ],
    )
    return ikm



