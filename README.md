# Valery WebHook Spammer

<p align="center">
<img src="https://i.pinimg.com/564x/a5/c1/1b/a5c11b552c3afd0d08273fd5f1677f59.jpg", width="500", height="500">
</p>

Valery WebHook Spammer is a powerful tool for spamming webhooks that allows you to send repeated messages to a specific webhook with a customizable time interval.

## Features

- Quickly send a large number of repeated messages to a specific webhook.
- Supports the use of proxies to hide your IP address and enhance anonymity.
- Customization options for message content, delay between sends, and request timeout.
- Intuitive and user-friendly interface.
- Utilize multiple threads to send spam in parallel
- Desktop notifications to track spamming progress and completion
- Connect to Discord RPC server to display spamming status on Discord Rich Presence

## Bypassing Rate Limits

Discord imposes rate limits on webhook requests to prevent abuse and ensure the stability of their service. However, Valery WebHook Spammer includes a feature to bypass these rate limits by implementing a retry mechanism. Here's how it works:

1. When a rate limit is encountered (HTTP status code 429), Valery WebHook Spammer will wait for the specified retry duration provided by the Discord API in the `Retry-After` header.
2. After the waiting period, the program will automatically retry sending the webhook request.

## Requirements

- Python 3.7 or above
- `pip` package manager

## Usage

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the command: `Valery.py`.
3. Follow the on-screen instructions to provide the necessary inputs, such as message, webhook URL, delay, threads count, etc.
4. Sit back and watch Valery WebHook Spammer in action!

## Disclaimer

The Valery WebHook Spammer tool is provided for educational and testing purposes only. The developer and contributors shall not be held responsible for any misuse or damage caused by the program. Use it responsibly and at your own risk.

## Credits

Valery WebHook Spammer was created by Hisako. Special thanks to overpower for his ideas and rate limit bypass
