from pyrogram import Client

api_id = 12345678
api_hash = "PUT_YOUR_OWN"

app = Client("my_session", api_id=api_id, api_hash=api_hash)

with app:
    print("Logged in successfully!")