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

    @client.command()
    async def ask(ctx, *, question):
        words = len(question.split())
        print(words)
        if 2 >= words > 0:
            OpenAI.ptype = "oneshot"
        elif 6 >= words > 2:
            OpenAI.ptype = "simple"
        elif words > 6:
            OpenAI.ptype = "complex"
        async with ctx.typing():
            # await message.channel.send('ping')
            list_user.append(ctx.message.author.id)
            answer = OpenAI.ask(question)
            await ctx.send(answer)


    @client.command()
    async def correct(ctx, *, sentence):
        async with ctx.typing():
            correction = OpenAI.correct(sentence)
            if correction == sentence:
                await ctx.send("I think there is no issue with your sentence")
            else:
                await ctx.send(f"Maybe you should try saying: '{correction}'")



    @client.command()
    @commands.is_owner()
    async def shutdown():
        exit()

    OpenAI.openai.api_key = OPENAI_API_KEY
    client.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
