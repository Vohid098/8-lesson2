from aiogram import Router
from handler import start

router = Router()


def setup_message_router():
    router.include_router(start.router)


    return router