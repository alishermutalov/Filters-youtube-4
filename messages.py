from aiogram.types import Message
from aiogram import Router, F
from keyboards import menu_items


router = Router()

@router.message(F.text.lower()=='salom')
async def say_hi(message:Message):
    await message.answer(text=f"Assalomu alaykum, {message.from_user.first_name}")
    
@router.message(F.text.startswith('bot'))
async def info(message:Message):
    await message.answer(text="Ha, men Aiogramda yozilgan botman")
    
    
@router.message(F.text.contains('raqam'))
async def info(message:Message):
    await message.answer(text="Sizga qanday raqam kerak? Men 5 ni taklf qilaman!")
    
    
@router.message(F.text == "📱Menu")
async def asnwer_menu(message:Message):
    await message.answer(text="Quyidagilardan birini tanlang", reply_markup=menu_items)