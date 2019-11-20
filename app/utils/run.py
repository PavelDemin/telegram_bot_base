from app import config
from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging


logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.INFO)

bot = Bot(config.TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage)