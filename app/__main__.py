from aiogram import Dispatcher, Bot
from aiogram.utils import executor
from aiogram.utils.exceptions import Unauthorized
from aiogram.contrib.fsm_storage.memory import MemoryStorage


def init():
    from . import logging
    logging.setup()

    from environs import Env
    env = Env()
    env.read_env()

    bot = Bot(token=env.str("BOT_TOKEN"), parse_mode=None)
    dp = Dispatcher(bot=bot, storage=MemoryStorage())

    import openai
    openai.api_key = env.str("OPENAI_TOKEN")

    admin_ids = env.list("ADMIN_IDS")
    bot["admin_ids"] = admin_ids

    try:
        from . import main

        executor.start_polling(
            dispatcher=dp,
            skip_updates=False,
            reset_webhook=True,
            on_startup=main.on_startup,
            on_shutdown=main.on_shutdown
        )
    except Unauthorized:
        logging.logger.error("Invalid bot token!")

    except Exception as e:
        logging.logger.error(e)


if __name__ == "__main__":
    init()
