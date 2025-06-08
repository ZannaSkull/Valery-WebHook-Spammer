from pypresence import AioPresence
from plyer import notification
import asyncio
import aiohttp
import random
import socket
import ctypes
import time
import os


# Codici colore ANSI
PINK = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"
PURPLE = "\033[35m"

MAX_FAILS = 5 

def GamingTitle(title):
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        print(f'\33]0;{title}\a', end='', flush=True)

def print_banner():
    ascii_text = f"""{BOLD}{PINK}
    
    ██╗   ██╗ █████╗ ██╗     ███████╗██████╗ ██╗   ██╗     
    ██║   ██║██╔══██╗██║     ██╔════╝██╔══██╗╚██╗ ██╔╝⠀⠀    
    ██║   ██║███████║██║     █████╗  ██████╔╝ ╚████╔╝                 
    ╚██╗ ██╔╝██╔══██║██║     ██╔══╝  ██╔══██╗  ╚██╔╝   
     ╚████╔╝ ██║  ██║███████╗███████╗██║  ██║   ██║   ⠀ 
      ╚═══╝  ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ⠀⠀⠀⠀
            The Lead of WebHook Spammers⠀⠀⠀⠀⠀⠀⠀           
                  Hisako Made This.                                  
    {RESET}"""
    os.system("cls" if os.name == "nt" else "clear")
    print(ascii_text)

class RateLimitBucket:
    def __init__(self):
        self.remaining = 1
        self.reset_time = 0
        self.semaphore = asyncio.Semaphore(1)

    async def wait_for_slot(self):
        async with self.semaphore:
            now = time.time()
            if self.remaining <= 0 and now < self.reset_time:
                wait = self.reset_time - now
                print(f"{PURPLE}Rate limit active, waiting {wait:.2f}s...{RESET}")
                await asyncio.sleep(wait)
            self.remaining = max(self.remaining - 1, 0)

    def update(self, headers):
        try:
            self.remaining = int(headers.get("X-RateLimit-Remaining", self.remaining))
            reset_after = float(headers.get("X-RateLimit-Reset-After", 0))
            self.reset_time = time.time() + reset_after
        except (TypeError, ValueError):
            pass

class RateLimiter:
    def __init__(self):
        self.buckets = {}
        self.global_lock = asyncio.Lock()
        self.global_reset = 0
        self.global_remaining = 1

    def get_bucket(self, bucket_id):
        if bucket_id not in self.buckets:
            self.buckets[bucket_id] = RateLimitBucket()
        return self.buckets[bucket_id]

    async def wait_global(self):
        async with self.global_lock:
            now = time.time()
            if self.global_remaining <= 0 and now < self.global_reset:
                wait = self.global_reset - now
                print(f"{PURPLE}Global rate limit active, waiting {wait:.2f}s...{RESET}")
                await asyncio.sleep(wait)
            self.global_remaining = max(self.global_remaining - 1, 0)

    def update_global(self, headers):
        try:
            self.global_remaining = int(headers.get("X-RateLimit-Global-Remaining", self.global_remaining))
            reset_after = float(headers.get("X-RateLimit-Global-Reset-After", 0))
            self.global_reset = time.time() + reset_after
        except (TypeError, ValueError):
            pass

rate_limiter = RateLimiter()

async def fetch_proxies():
    url = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                text = await resp.text()
                proxies = [line.strip() for line in text.splitlines() if line.strip()]
                if not proxies:
                    print(f"{PURPLE}No proxies found, continuing without proxy.{RESET}")
                else:
                    print(f"{PURPLE}Downloaded {len(proxies)} proxies.{RESET}")
                return proxies
    except Exception as e:
        print(f"{PURPLE}Failed to fetch proxies: {e}{RESET}")
        return []

def read_input(prompt, input_type):
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

async def configure_input():
    print_banner()
    message = input(f"{PURPLE}Type message: {RESET}")
    webhook_url = input(f"{PURPLE}Enter webhook URL: {RESET}")
    delay = read_input(f"{PURPLE}Enter a delay (seconds): {RESET}", float)
    threads_count = read_input(f"{PURPLE}Enter the number of threads: {RESET}", int)
    messages_count = read_input(f"{PURPLE}Enter the total number of messages per task: {RESET}", int)
    timeout = read_input(f"{PURPLE}Enter request timeout (seconds): {RESET}", float)
    use_proxies = input(f"{PURPLE}Use automatic proxies? (Y/N): {RESET}").lower() == 'y'
    proxy_list = await fetch_proxies() if use_proxies else []
    return message, webhook_url, delay, threads_count, messages_count, timeout, proxy_list

async def configure_presence():
    SexyRPC = AioPresence(client_id="1112872663384326154")
    await SexyRPC.connect()
    await SexyRPC.update(
        state="Valery | Spamming Webhooks",
        details="The Best Free WebHook Spammer!",
        large_image="valerylarge",
        large_text="Using The Lead of WebHook Spammers ❤"
    )
    return SexyRPC

async def SendHook(session, webhook, msg, proxy, timeout, Proxy_Queue, Proxy_Fail_Counter):
    webhook_data = {
        "content": msg,
        "username": "Valery",
        "avatar_url": "https://i.pinimg.com/564x/a5/c1/1b/a5c11b552c3afd0d08273fd5f1677f59.jpg"
    }
    proxy_url = f"http://{proxy}" if proxy else None

    await rate_limiter.wait_global()
    bucket = rate_limiter.get_bucket(webhook)
    await bucket.wait_for_slot()

    try:
        async with session.post(webhook, json=webhook_data, proxy=proxy_url, timeout=timeout) as response:
            headers = response.headers
            rate_limiter.update_global(headers)
            bucket.update(headers)

            if response.status == 204:
                print(f"{PINK}Webhook sent successfully.{RESET}")
                if proxy:
                    Proxy_Fail_Counter[proxy] = 0
                return True
            elif response.status == 429:
                retry_after = float(headers.get("Retry-After", 1))
                print(f"{PURPLE}Rate limit 429. Waiting {retry_after}s before retry...{RESET}")
                await asyncio.sleep(retry_after)
                return False
            else:
                print(f"{PURPLE}HTTP error {response.status}{RESET}")
                return False
    except (aiohttp.ClientError, asyncio.TimeoutError, socket.gaierror) as e:
        print(f"{PURPLE}Network error while sending webhook: {e}{RESET}")
        if proxy:
            Proxy_Fail_Counter[proxy] = Proxy_Fail_Counter.get(proxy, 0) + 1
            if Proxy_Fail_Counter[proxy] < MAX_FAILS:
                await Proxy_Queue.put(proxy)
            else:
                print(f"{PURPLE}Proxy {proxy} removed after {MAX_FAILS} failures.{RESET}")
        return False
    except Exception as e:
        print(f"{PURPLE}Unknown error while sending webhook: {e}{RESET}")
        return False

async def SpamTask(webhook_url, message, delay, messages_count, timeout, proxy_list, semaphore, Proxy_Queue, Proxy_Fail_Counter):
    connector = aiohttp.TCPConnector(ssl=False)
    timeout_obj = aiohttp.ClientTimeout(total=timeout)

    async with aiohttp.ClientSession(connector=connector, timeout=timeout_obj) as session:
        for _ in range(messages_count):
            proxy = None
            if Proxy_Queue and not Proxy_Queue.empty():
                proxy = await Proxy_Queue.get()

            async with semaphore:
                success = await SendHook(session, webhook_url, message, proxy, timeout, Proxy_Queue, Proxy_Fail_Counter)
            if success and proxy:
                await Proxy_Queue.put(proxy)
            if delay > 0:
                await asyncio.sleep(delay)

async def main_async():
    GamingTitle("Valery")
    SexyRPC = await configure_presence()
    Proxy_Fail_Counter = {} 
    try:
        message, webhook_url, delay, threads_count, messages_count, timeout, proxy_list = await configure_input()

        Proxy_Queue = asyncio.Queue()
        for proxy in proxy_list:
            Proxy_Queue.put_nowait(proxy)

        semaphore = asyncio.Semaphore(threads_count)

        tasks = [
            SpamTask(webhook_url, message, delay, messages_count, timeout, proxy_list, semaphore, Proxy_Queue, Proxy_Fail_Counter)
            for _ in range(threads_count)
        ]

        await asyncio.gather(*tasks)

        notification.notify(
            title="Spam Completed",
            message=f"Spam task completed",
            app_icon=None
        )

        await SexyRPC.close()
        print(f"{BOLD}{PINK}Operation completed successfully!{RESET}")
    except Exception as e:
        print(f"{PURPLE}Error in main loop: {e}{RESET}")

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
