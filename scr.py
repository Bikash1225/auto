import re
from pyrogram import Client, filters

#from config import API_ID, API_HASH, SESSION

app = Client(
     name='t',
     api_id=6258636,
     api_hash=72e82ac4cfe8fe0df32860140fc8014d,
     session_string=str(AQBff8wAHT9POWHDFxWU7vF_S-nW8JK_-LU5y3EqzWICbd0zK5m2gfmm8vxZXVCVEH6wiiHNrrzDf5f4rZ8wDxKQev0GgFrOA3c4fnmZu6fzEIbEoOXKJE798YRSWZZgiz1d9Yy-ZFjp6dCCwz4hbREyYZ2oxfl_2vrhMRLIhfuyboMBQXox23R5017Dk6wne4hcf1MHb34glMTfwnxOvjin9hoyjsj0WIodnsuUYeqVh-vyNCGn2ST-5RK4ta5Ttwp5dT-fjWci3-37PR6GCWjvrs927aR3Ehy8_NT2Tgv_fWEhPeG5wFWSwXOH8Lp14Kxv7xqovfMM5xSLg7l9mtgZ6PxMlgAAAAFskm5GAA),
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
