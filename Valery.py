import random
import asyncio
import aiohttp
from plyer import notification
import threading

PINK = "\033[95m"
RESET = "\033[0m"

ascii_text = r""" {pink}

██╗   ██╗ █████╗ ██╗     ███████╗██████╗ ██╗   ██╗
██║   ██║██╔══██╗██║     ██╔════╝██╔══██╗╚██╗ ██╔╝
██║   ██║███████║██║     █████╗  ██████╔╝ ╚████╔╝ 
╚██╗ ██╔╝██╔══██║██║     ██╔══╝  ██╔══██╗  ╚██╔╝  
 ╚████╔╝ ██║  ██║███████╗███████╗██║  ██║   ██║   
  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   
        The Lead of WebHook Spammers
              Hisako Made This.                                  

{reset} """.format(pink=PINK, reset=RESET)

print(ascii_text)
message = input("Type message: ")
webhook_url = input("Enter webhook: ")
delay = int(input("Enter a delay: (0-5) "))
threads_count = int(input("Enter the number of threads: "))
messages_count = int(input("Enter the number of messages to spam: "))
timeout = float(input("Enter the request timeout (in seconds): "))

use_proxies = input("Do you want to use proxies? (Y/N): ")
if use_proxies.lower() == "y":
    proxy_file_path = input("Enter the path to the proxy file: ")
    with open(proxy_file_path, "r") as file:
        proxy_list = [proxy.strip() for proxy in file.readlines()]
else:
    proxy_list = []

spamming_started = False
spamming_finished = False

async def send_webhook(webhook, msg, proxy):
    async with aiohttp.ClientSession() as session:
        try:
            webhook_data = {
                "content": msg,
                "username": "Valery",
                "avatar_url": "https://i.pinimg.com/564x/a5/c1/1b/a5c11b552c3afd0d08273fd5f1677f59.jpg"
            }
            async with session.post(webhook, json=webhook_data, timeout=timeout) as response:
                if response.status == 204:
                    print("\033[95mWebhook sent successfully.\033[0m")
                    return True
                elif response.status == 429:
                    print("\033[91mRate limit reached. Waiting for retry...\033[0m")
                    await asyncio.sleep(float(response.headers.get("Retry-After", "5")))
                    return False
                else:
                    print("\033[91mFailed to send webhook. Status code:", response.status, "\033[0m")
                    return False
        except (aiohttp.ClientError, asyncio.TimeoutError):
            print("\033[91mFailed to send webhook.\033[0m")
            return False

async def spam_webhooks():
    global spamming_started
    global spamming_finished

    if not spamming_started:
        spamming_started = True
        notification.notify(
            title="Spamming Started",
            message="The spamming process has started.",
            app_icon=None
        )

    tasks = []
    sent_count = 0
    while sent_count < messages_count:
        proxy = random.choice(proxy_list) if proxy_list else None
        task = send_webhook(webhook_url, message, proxy)
        tasks.append(task)
        await asyncio.sleep(delay)

        if await task:
            sent_count += 1

    if not spamming_finished:
        spamming_finished = True
        notification.notify(
            title="Spam Finished",
            message="The spamming process has finished. Sent: {} Webhooks".format(sent_count),
            app_icon=None
        )

def run_spamming():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(spam_webhooks())

    except Exception as e:
        print("An error occurred:", e)

threads = []
for _ in range(threads_count):
    t = threading.Thread(target=run_spamming)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
