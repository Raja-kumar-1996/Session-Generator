from pyrogram import Client

api_id = int(input("Enter API_ID: "))
api_hash = input("Enter API_HASH: ")

app = Client(
    "my_account",
    api_id=api_id,
    api_hash=api_hash,
    in_memory=True
)

with app:
    print("\nSession String:\n")
    print(app.export_session_string())
