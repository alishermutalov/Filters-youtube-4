from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command('start'))
async def cmd_start(message:types.Message):
    await message.answer(text=f"Salom, {message.from_user.username}!")
    
    
@router.message(Command('help'))
async def cmd_help(message:types.Message):
    await message.answer(text="ℹ️ Mavjud komandalar: /start, /help, /about!")

    
@router.message(Command('about'))
async def cmd_about(message:types.Message):
    await message.answer(text="🤖 Men aiogram 3 yordamida yozilgan botman.")
    