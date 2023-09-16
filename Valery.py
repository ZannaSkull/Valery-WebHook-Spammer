from pypresence import Presence
from plyer import notification
import threading
import aiohttp
import asyncio
import random
import ctypes
import os

PINK = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"
PURPLE = "\033[35m"

def Title(title):
    Tutle = title.encode('cp1252')
    ctypes.windll.kernel32.SetConsoleTitleA(Tutle)

def Presence():
    RPC = Presence(client_id="1112872663384326154")
    RPC.connect()
    RPC.update(
        state="Valery | Spamming Webhooks",
        details="The Best Free WebHook Spammer!",
        large_image="valerylarge",
        large_text="Using The Lead of WebHook Spammers ❤ "
    )
    return RPC

def Bunner():
    ascii_text = r""" {bold}{pink}
    
    ██╗   ██╗ █████╗ ██╗     ███████╗██████╗ ██╗   ██╗     
    ██║   ██║██╔══██╗██║     ██╔════╝██╔══██╗╚██╗ ██╔╝⠀⠀    
    ██║   ██║███████║██║     █████╗  ██████╔╝ ╚████╔╝                 
    ╚██╗ ██╔╝██╔══██║██║     ██╔══╝  ██╔══██╗  ╚██╔╝   
     ╚████╔╝ ██║  ██║███████╗███████╗██║  ██║   ██║   ⠀ 
      ╚═══╝  ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ⠀⠀⠀⠀
            The Lead of WebHook Spammers⠀⠀⠀⠀⠀⠀⠀           
                  Hisako Made This.                                  
    {reset} """.format(bold=BOLD, pink=PINK, reset=RESET)

    os.system("cls" if os.name == "nt" else "clear")
    print(ascii_text)

def inputty(prompt, input_type):
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def Settings():
    Bunner()

    message = input(PURPLE + "Type message: " + RESET)
    webhook_url = input(PURPLE + "Enter webhook: " + RESET)
    delay = inputty(PURPLE + "Enter a delay: (0-5) ", int)
    threads_count = inputty(PURPLE + "Enter the number of threads: ", int)
    messages_count = inputty(PURPLE + "Enter the number of messages to spam: ", int)
    timeout = inputty(PURPLE + "Enter the request timeout (in seconds): ", float)

    use_proxies = input(PURPLE + "Do you want to use proxies? (Y/N): " + RESET)
    if use_proxies.lower() == "y":
        proxy_file_path = input(PURPLE + "Enter the path to the proxy file: " + RESET)
        with open(proxy_file_path, "r") as file:
            proxy_list = [proxy.strip() for proxy in file.readlines()]
    else:
        proxy_list = []

    return message, webhook_url, delay, threads_count, messages_count, timeout, proxy_list

async def Sex(webhook, msg, proxy, timeout):
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
                    retry_after = float(response.headers.get("Retry-After", "5"))
                    print("\033[91mRate limit reached. Waiting for retry... ({} seconds)\033[0m".format(retry_after))
                    await asyncio.sleep(retry_after)
                    return False
                else:
                    print("\033[91mFailed to send webhook. Status code:", response.status, "\033[0m")
                    return False
        except (aiohttp.ClientError, asyncio.TimeoutError):
            print("\033[91mFailed to send webhook.\033[0m")
            return False

async def Spammly(webhook_url, message, delay, messages_count, timeout, proxy_list):
    sent_count = 0
    while sent_count < messages_count:
        proxy = random.choice(proxy_list) if proxy_list else None
        success = await Sex(webhook_url, message, proxy, timeout)
        await asyncio.sleep(delay)

        if success:
            sent_count += 1

    return sent_count

def URGay(webhook_url, message, delay, messages_count, timeout, proxy_list):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        sent_count = loop.run_until_complete(Spammly(webhook_url, message, delay, messages_count, timeout, proxy_list))

        if not finished:
            finished = True
            notification.notify(
                title="Spam Finished",
                message="The spamming process has finished. Sent: {} Webhooks".format(sent_count),
                app_icon=None
            )
            print("\033[92mSuccessfully Valery Spammed\033[0m")

    except Exception as e:
        print("An error occurred:", e)

    RPC.close()

def main():
    Title("Valery")
    RPC = Presence()
    Bunner()
    message, webhook_url, delay, threads_count, messages_count, timeout, proxy_list = Settings()

    started = False
    finished = False

    threads = []
    for _ in range(threads_count):
        t = threading.Thread(target=URGay, args=(webhook_url, message, delay, messages_count, timeout, proxy_list))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
