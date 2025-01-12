from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("⚡️𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦⚡️", data="help_back")
        ],
        [
        Button.url("⚡️𝗖𝗛𝗔𝗡𝗡𝗘𝗟⚡️", "https://t.me/ll_BOTCHAMBER_ll"),
        Button.url("⚡️𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️", "https://t.me/BOT_SUPPORT_GROUP7")
        ],
        [
        Button.url("⚡️𝗥𝗘𝗣𝗢⚡️", "https://github.com/Rishubot")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"""**┌────── ˹ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ˼──────•\n┆◍ ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}), \n┆◍ ɪ ᴧϻ [{BotName}](tg://user?id={BotId}), \n└──────────────────────•\n» ✦ϻσsᴛ ᴘσᴡєꝛғυʟʟ sᴘᴧϻ ʙσᴛ  \n» ✦ʙєsᴛ ғєᴧᴛυꝛє ʙσᴛ ση ᴛєʟєɢꝛᴧϻ \n» ✦ᴧᴅᴅ ϻє ɢꝛσυᴘ ᴛσ sєє ϻʏ ᴘσᴡєꝛ\n•──────────────────────•\n❖ 𝐏ᴏᴡᴇʀᴇᴅ ʙʏ  :-  [⎯꯭֯🖤⃪ ꯭⃛֯ ̶̲̽͟𓆩⃪ͥ͢ ᷟ𓆩𝙍𝘼𝘿𝙃𝙀 ⃪𝄀꯭𝄄꯭ا✾༐𓂃⃪꯭,, ㅤ ™ㅤ ](https://t.me/ll_RADHE7_ll)❤️‍🔥\n•──────────────────────•**"""
        await event.client.send_file(
                event.chat_id,
                "https://envs.sh/sgd.jpg",
                caption=TEXT, 
                buttons=PythonButton)
