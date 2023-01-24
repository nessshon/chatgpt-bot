<h1 align="center">🤖 ChatGPT Telegram Bot</h1>

## Requirements

* Python 3.10 and above.
* Systemd or Docker.

## Usage

Clone this repo via [link](https://github.com/nessshon/chatgpt-bot)

```bash
git clone https://github.com/nessshon/chatgpt-bot
```

Go to the project folder

```bash
cd chatgpt-bot
```

Create environment variables file

```bash
cp .env.example .env
```

Edit [environment variables](#environment-variables-reference) in `.env`

```bash
nano .env
```

### Launch using Docker

1. Install [docker](https://docs.docker.com/get-docker) and [docker compose](https://docs.docker.com/compose/install/)

2. Build and run your container
   ```bash
   docker-compose up -d
   ```

### Environment variables reference

| Variable     | Description                                             |
|--------------|---------------------------------------------------------|
| BOT_TOKEN    | Token, get it from [@BotFather](https://t.me/BotFather) |
| ADMIN_IDS    | List admin ID                                           |
| OPENAI_TOKEN | OpenAI secret token                                     |
