from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from handler import setup_message_router


API_TOKEN = "8019523539:AAG4mjFrpulE05EYMBB8J0LUMKvxYopkTHI"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


async def main():
    handler_router = setup_message_router()
    dp.include_router(handler_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
