# (c) Code-X-Mania

from Code_X_Mania.bot import StreamBot
from Code_X_Mania.vars import Var
from Code_X_Mania.utils.human_readable import humanbytes
from Code_X_Mania.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
db = Database(Var.DATABASE_URL, Var.SESSION_NAME)
from pyshorteners import Shortener

def get_shortlink(url):
   shortlink = False 
   try:
      shortlink = Shortener().dagd.short(url)
   except Exception as err:
       print(err)
       pass
   return shortlink

START_TEXT = """
<b>Hey </b> {}\n
<b>I am Telegram File Direct Link Generator as well as File Streamer Bot. </b>\n
<b>✪ Use Help Command to Know how to Use me.</b>\n
<b><b>✪ Made With 💕 By </b>@Tellybots_4u</b>"""

HELP_TEXT = """
<b>✪ Send Me Any File or Media .</b>\n
<b>✪ I Will Provide You Instant Direct Download link and Online Streaming link.</b>\n
<b>✪ Add me in Your Channel as Admin To Get Direct Download link button and online Stream Link Button </b>\n
<b>✪ Streaming Link as well as Instant Link Generator With Fastest Speed</b>\n
"""

ABOUT_TEXT = """
<b>🤖 My Name : Telly File Stream Bot</b>\n
<b>🚦 Version : <a href='https://telegram.me/tellybots_4u'>2.0</a></b>\n
<b>💫 Source Code : <a href='https://t.me/tellybots_digital'>Click Here</a></b>\n
<b>🗃️ Library : <a href='https://pyrogram.org'>Click Here</a></b>\n
<b>👲 Developer : <a href='https://telegram.me/tellybots_4u'>TellyBots_4u</a></b>\n
<b>📦 Last Updated : <a href='https://telegram.me/tellybots_4u'>[ 15-Oct-21 ] 10:00 PM</a></b>"""

START_BUTTONS = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('📡 Update Channel', url='https://t.me/tellybots_4u'), InlineKeyboardButton('💬 Support Group', url='https://t.me/tellybots_support')],
                    [InlineKeyboardButton('🚦 Bot Status', url='https://t.me/tellybots_4u'), InlineKeyboardButton('⛔ Close', callback_data='close')]
                ]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('Help ❔', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    else:
        await update.message.delete()


@StreamBot.on_message(filters.command('start') & filters.private & ~filters.edited)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\nMy New Freind [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started Your Bot!!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="Sorry Sir, Yᴏᴜ Are Banned To Use Me. Contact Our Support Group\n\n @tellybots_support **They Will help you**",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>Join My Update Channel To Use Me 🤖</b>",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                            InlineKeyboardButton("Join Now 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="<b>Something Went Wrong Contact Our Support Group</i> <b><a href='http://t.me/tellybots_support'>[ Click Here ]</a></b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True)
                return
        await m.reply_text(
            text=START_TEXT.format(m.from_user.mention),
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
              )                                                                         
                                                                                       
                                                                            
    else:
        if Var.UPDATES_CHANNEL != "None":
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == "kicked":
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**Sorry Sir, You Are Banned To Use Me. Contact Our Support Group** @tellybots_support",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Please Join My Update Channel To Use Me**!\n\n**Due To Overload, Only Channel Subscribers Can Use Me**!",
                    reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("🤖 Jᴏin Update Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Something Went Wrong. Contact Our Support Group** [Tellybots_Support](https://t.me/tellybots_support).",
                    parse_mode="markdown",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, message_ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = Var.URL + 'watch/' + str(log_msg.message_id)
        shortlink = get_shortlink(stream_link)
        if shortlink:
            stream_link = shortlink
        online_link = Var.URL + 'download/' + str(log_msg.message_id)
        shortlinka = get_shortlink(online_link)
        if shortlinka:
            online_link = shortlinka

        msg_text ="""

<b>🗃️ File Name :</b> <b>{}</b>

<b>📦 File Size :</b> <b>{}</b>

<b>📝 Note : Link will be expired in 24hrs </b>

<b>🎉 By</b> <b> @Tellybots_4u </b>"""
"""

        await m.reply_text(
            text=msg_text.format(file_name, file_size, online_link, stream_link),
            parse_mode="HTML",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🎬 Watch Online", url=stream_link), #Stream Link
                                                InlineKeyboardButton('Download 📥', url=online_link)]]) #Download Link
        )


@StreamBot.on_message(filters.private & filters.command(["about"]))
async def start(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )


@StreamBot.on_message(filters.command('help') & filters.private & ~filters.edited)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined **\n\nMy New Friend [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started Your Bot !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<b>Sᴏrry Sir, Yᴏu Are Banned To Use Me. Cᴏntact Our Support Group</b>",
                    parse_mode="HTML",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Please Join My Update Channel To Use Me!**\n\nDue To Overload, Only Channel Subscribers Can Use Me!",
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("🤖 Join My Update Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="Something Went Wrong. Contact Our Support Group [Tellybots_Support](https://t.me/tellybots_4u).",
                parse_mode="markdown",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text=HELP_TEXT,
        parse_mode="HTML",
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
        )

