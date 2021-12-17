# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import Client
from ..vars import Var

StreamBot = Client(
    session_name= 'Web Streamer',
    api_id=Var.18162286,
    api_hash=Var.a0b565a5bbc2024075706bac692430b2,
    bot_token=Var.55838383:yourtbottokenhere,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)
