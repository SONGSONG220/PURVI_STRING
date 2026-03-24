from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID
from RAUSHAN.db.users import add_served_user, get_served_users

# Aapka Sudo User ID
sudo_user_id = 7812646657

@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(client, msg: Message):
    # User ko database mein add karna
    await add_served_user(msg.from_user.id)
    
    # FIX: 'Client' ki jagah 'client' variable ka use kiya hai
    try:
        await client.send_message(chat_id=sudo_user_id, text=f"DONE: {msg.from_user.id}")
    except Exception as e:
        print(f"Error sending message to sudo: {e}")

@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(client, msg: Message):
    users_list = await get_served_users()
    users_count = len(users_list)
    await msg.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users_count} ᴜsᴇʀs", quote=True)
    
