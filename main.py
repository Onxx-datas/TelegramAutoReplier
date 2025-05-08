from pyrogram import Client, filters

app = Client("my_session", api_id=12345678, api_hash="PUT_YOUR_OWN")

@app.on_message(filters.private)
async def dm_reply(client, message):
    await message.reply("Message to send automatically")

app.run()
