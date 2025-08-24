from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="📱Menu")
]], resize_keyboard=True)


menu_items = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Go'sht"), KeyboardButton(text="Sut")],
    [KeyboardButton(text="Sabzi"), KeyboardButton(text="Kartoshka")],
], resize_keyboard=True
)