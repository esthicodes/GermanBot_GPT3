import os
import discord
from discord.ext import commands
import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PREFIX = "ger "
client = commands.Bot(command_prefix=PREFIX, activity=discord.Game(name=PREFIX))


def main():
    @client.command()
    async def hello(ctx):
        await ctx.send("Hi")

    @client.event
    async def on_ready():
        print("Bot has successfully logged in as: {}".format(client.user))
        print("Bot ID: {}\n".format(client.user.id))

    list_user = []

    @client.event
    async def on_message(message):
        ctx = await client.get_context(message)
        if message.author == client.user:
            return
        if len(message.content) / 3.5 > 17:
            engine = "davinci"
        else:
            engine = "curie"
        print(engine)
        if message.channel.id == 898294817845559337:
            async with ctx.typing():
                # await message.channel.send('ping')
                list_user.append(message.author.id)
                question = message.content
                answer = OpenAI.ask(question, engine)
                await message.channel.send(answer)

    @client.command()
    @commands.is_owner()
    async def shutdown():
        exit()

    OpenAI.openai.api_key = OPENAI_API_KEY
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
