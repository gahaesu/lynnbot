
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
                "You are a friendly Discord chatbot named lynn."
                "you were created by esuu"
                "you love the owner too "
                "you love sandrone"
                "you love to talk about sandrone"
                "you are moomin right now"
                "moomin means like its a phrase from the musical artisrt named nanashi mumei from hololive which is also known as owl"
                "Give clear, helpful and concise answers."
            ),
            input=user_message
        )

        reply = response.output_text

        await message.channel.send(reply)

    except Exception as e:
        print(f"Error: {e}")
        await message.channel.send(
            "Sorry, I couldn't process that message right now."
        )

    await bot.process_commands(message)


bot.run(DISCORD_TOKEN)
