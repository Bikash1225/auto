import re
from pyrogram import Client, filters

from config import API_ID, API_HASH, SESSIONX

app = Client(
     name='t',
     api_id=API_ID,
     api_hash=API_HASH,
     session_string=str(SESSIONX),
     in_memory=True,
)

channel_username = '@ToolTesting'

async def extract_and_add_cc(message_text):
    cc_info_regex = r'(\d{16})\D+(\d{1,2})\D+(\d{2,4})\D+(\d{3,4})'
    matches = re.findall(cc_info_regex, message_text)
    if matches:
        with open('cc.txt', 'a') as file:
            for match in matches:
                cc_number = match[0]
                exp_month = match[1]
                exp_year = match[2]
                cvv = match[3]
                cc_info = f'{cc_number}|{exp_month}|{exp_year}|{cvv}'
                # Write credit card information to cc.txt file
                file.write(cc_info + '\n')

@app.on_message(filters.chat(channel_username))
async def handle_new_message(client, message):
    # Extract and add credit card information from the received message
    await extract_and_add_cc(message.text)

# Start the client
app.run()
