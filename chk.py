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

# Replace '123456789' with the chat ID of your private channel
channel_chat_id = -1001926973349

async def send_message_to_bot(cc):
    cc_without_destination = cc.replace("tg://resolve?domain=deltachk", "")
    await app.send_message('DeltaCheckBot', f'/tb {cc_without_destination}')
    print(cc_without_destination)
    await asyncio.sleep(21)  # Introduce a 21-second delay

async def forward_message_to_channel(message_text):
    # Forward the entire message text to the specified private channel
    await app.send_message(channel_chat_id, message_text)

async def main():
    done = 0
    total_cc_count = sum(1 for line in open('cc.txt'))
    while True:
        with open('cc.txt', 'r') as file:
            cc_lines = file.readlines()
            if 'cc' in ''.join(cc_lines):
                for line in cc_lines:
                    cc = line.strip()
                    await send_message_to_bot(cc)
                    done += 1
                    if done == total_cc_count:
                        await asyncio.sleep(10)
                        done = 0
            else:
                await asyncio.sleep(10)

async def start_app():
    await app.start()
    await main()

asyncio.get_event_loop().run_until_complete(start_app())
