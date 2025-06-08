# Valery WebHook Spammer

<p align="center">
<img src="https://i.pinimg.com/564x/a5/c1/1b/a5c11b552c3afd0d08273fd5f1677f59.jpg", width="500", height="500">
</p>

**Valery WebHook Spammer** is an advanced and modern tool for mass sending messages via webhooks. Designed to be fast, configurable, and reliable, it leverages Python's asynchronous capabilities to deliver high performance and intelligent handling of platform-imposed limits such as those from Discord.

---

## 🚀 Key Features

- Fast and massive sending of messages.
- Advanced and automatic proxy management: downloads public proxies, with automatic rotation and removal of non-working proxies.  
- Intelligent Discord rate limit bypass, respecting both global and bucket-specific limits to avoid blocks and temporary bans.  
- Improved user interface with guided input, colorful banner, and desktop notifications.  
- Fully asynchronous, using `asyncio` to maximize speed and scalability.  
- Full customization of message, avatar, delay, timeout, number of messages, and more.  
- Discord Rich Presence integration to display spamming status directly on your Discord profile.

---

## 🔄 Rate Limit Bypass and Handling

Discord enforces strict rate limits on webhook requests to prevent abuse and ensure service stability. Valery WebHook Spammer implements a sophisticated mechanism to handle and bypass these limits effectively:

- When a rate limit is encountered (HTTP status code 429), the program reads the `Retry-After` header provided by Discord, which specifies how many seconds to wait before retrying.
- The spammer respects both **global** and **bucket-specific** rate limits by implementing a **rate limit bucket logic**, ensuring requests are paced correctly to avoid triggering blocks or bans.
- Requests that hit rate limits are automatically retried after the specified delay, maintaining a smooth and continuous spamming process without manual intervention.
- This approach prevents unnecessary failures and maximizes throughput while complying with Discord’s API policies.
- Additionally, the program intelligently manages concurrent requests using asynchronous queues and semaphores to balance speed and rate limit compliance.

This advanced rate limit handling ensures that Valery WebHook Spammer can send large volumes of messages efficiently without being blocked or timed out by Discord.
## Requirements

- Python 3.8 or above
- Package manager `pip`

---

## 📝 How to Use

1. Download or clone the project.  
2. Open a terminal in the project folder.  
3. Run the script with: python Valery.py
4. Follow the on-screen instructions to input:  
- Message to send  
- Webhook URL  
- Delay between messages  
- Number of messages to send  
- Request timeout  
- Proxy usage (automatic)  
5. Monitor progress in the console, desktop notifications, and via Discord Rich Presence.

---

## ⛔ Disclaimer

Valery WebHook Spammer is provided for educational and testing purposes only.  
The author and contributors are not responsible for any misuse or damage caused by this software.  
Use this tool responsibly and at your own risk.

---

## 👤 Credits

Valery WebHook Spammer was created by **Hisako**.  

---

> **Note:** The use of spamming tools is prohibited by the Terms of Service of many platforms. Use this software only on webhooks you own or in controlled testing environments.
