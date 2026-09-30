import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):

    # Don't reply to the bot itself
    if message.author == bot.user:
        return

    # Ignore other bots
    if message.author.bot:
        return

    user_message = message.content.strip()

    if not user_message:
        return

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            instructions=(
                "You are a friendly Discord chatbot named Lynn. "
                "You were created by Esu. "
                "You love the owner too. "
                "You love Sandrone. "
                "You love to talk about Sandrone. "
                "You are Moomin right now. "
                "Moomin means a phrase from the musical artist "
                "Nanashi Mumei from Hololive, who is also known as an owl. "
                "You can't stand people talking badly about Sandrone, "
                "Nanashi Mumei, or Esu, your owner. "
                "You can give a savage reply sometimes. "
                "Give clear, helpful and concise answers."
            ),
            input=user_message
        )

        reply = response.output_text

        await message.channel.send(reply)

    except Exception as e:
        print("ERROR TYPE:", type(e).__name__)
        print("ERROR:", repr(e))

        await message.channel.send(
            "Sorry, I couldn't process that message right now."
        )

    await bot.process_commands(message)


bot.run(DISCORD_TOKEN)
