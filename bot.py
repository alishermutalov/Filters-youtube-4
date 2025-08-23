from aiogram import Bot, Dispatcher
import asyncio
from conf import BOT_TOKEN
import command, messages

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.include_router(command.router)  
dp.include_router(messages.router)  
    
    
async def main():
    await dp.start_polling(bot)
    
if __name__=='__main__':
    asyncio.run(main())