import os
import discord
from discord.ext import commands
import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PREFIX = "ger "
client = commands.Bot(command_prefix=PREFIX, activity=discord.Game(name=f"{PREFIX}help"))
client.remove_command("help")

def main():
    @client.event
    async def on_ready():
        print("Bot has successfully logged in as: {}".format(client.user))
        print("Bot ID: {}\n".format(client.user.id))

    list_user = []

    @client.command()
    async def help(ctx):
        embed=discord.Embed(
                title="List of commands",
                color=discord.Color.orange()

        )
        embed.add_field(
            name="**ger ask**",
            value="Ask any german related question. " \
                  "Ex. `ger ask can you explain in english 'akkusativ' with an example?`",
            inline=False
        )
        embed.add_field(
            name="**ger correct**",
            value="Corrects a sentence in German if the bot thinks it is incorrect. " \
                  "Ex. `ger correct Der hamer klein ist`",
            inline=False
        )
        embed.set_footer(
            text="Warning: this bot is still being developed and you may encounter errors"
        )
        emoji = "\u2705"
        await ctx.message.add_reaction(emoji)
        await ctx.author.send(embed=embed)

    channel = 898294817845559337 # Change Discord channel ID
    owner = 530621162250567681 # Change Discord owner ID

    @client.command()
    async def ask(ctx, *, question):

        if ctx.channel == channel or ctx.author.id == owner:
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
        if ctx.message.channel == channel:
            async with ctx.typing():
                correction = OpenAI.correct(sentence)
                if correction.strip() == sentence.strip():
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
