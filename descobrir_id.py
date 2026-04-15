from pyrogram import Client

api_id = 123456  # Seu api_id
api_hash = "seu_api_hash"  # Seu api_hash

app = Client("minha_sessao", api_id=api_id, api_hash=api_hash)

with app:
    chat = app.get_chat("https://t.me/+")  # Link do canal que você entrou
    print(f"🆔 chat_id do canal: {chat.id}")
