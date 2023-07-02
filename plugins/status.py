import asyncio
import time
import math
import os
import psutil
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, SUPPORT_CHAT, MELCOW_NEW_USERS, CHNL_LNK, GRP_LNK, NEWGRP
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp, get_settings
from Script import script
from pyrogram.errors import ChatAdminRequired

#@Client.on_message(filters.command('status') & filters.user(ADMINS) & filters.incoming)
#async def get_ststs(bot, message):
    #rju = await message.reply('Fetching stats..')
    #total_users = await db.total_users_count()
    #totl_chats = await db.total_chat_count()
    #files = await Media.count_documents()
    #size = await db.get_db_size()
    #free = 536870912 - size
    #size = get_size(size)
    #free = get_size(free)
    #await rju.edit_text(
            #text=script.USER_STATS_TXT.format(files, total_users, totl_chats, size, free),
            #disable_web_page_preview=True,
            ##reply_markup=reply_markup,
            #parse_mode=enums.ParseMode.HTML
       # )


@Client.on_message(filters.command('status') & filters.user(ADMINS) & filters.incoming)
async def get_ststs(bot, message):
        buttons = [[
            InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='about'),
            InlineKeyboardButton('⟲ Rᴇғʀᴇsʜ', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit_text(
            text=script.USER_STATS_TXT.format(total, users, chats, monsize, free),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
async def query.data == "rfrsh":
        await query.answer("Fetching MongoDb DataBase")
        buttons = [[
            InlineKeyboardButton('⟸ Bᴀᴄᴋ', callback_data='about'),
            InlineKeyboardButton('⟲ Rᴇғʀᴇsʜ', callback_data='rfrsh')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        total = await Media.count_documents()
        users = await db.total_users_count()
        chats = await db.total_chat_count()
        monsize = await db.get_db_size()
        free = 536870912 - monsize
        monsize = get_size(monsize)
        free = get_size(free)
        await query.message.edit_text(
            text=script.USER_STATS_TXT.format(total, users, chats, monsize, free),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
