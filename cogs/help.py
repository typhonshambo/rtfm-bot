import discord
from discord.ext import commands
import json
from discord_components import *

with open ('././config/config.json', 'r') as f:
    config = json.load(f)
    prefix = config['prefix']


class help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['h'],invoke_without_command=True)
    async def help(self, ctx):
        help_embed = discord.Embed(
            color=0x0AFF4D,
            title="COMMAND LIST",
            description=f"""
            :small_blue_diamond: `{prefix}rtfm <name>` - shows docs regarding <name>
            :small_blue_diamond: `{prefix}help` - shows this command list
            """
        )
        help_embed.set_thumbnail(url="https://media.discordapp.net/attachments/460568954968997890/761037965987807232/dpycogs.png")
        await ctx.send(embed=help_embed,
        components=[
                [
                    Button(label="Support Server", style=5, url="https://discord.gg/m5mSyTV7RR"),
                    Button(label="Github", style=5, url="https://github.com/typhonshambo")
                ]
            ]
        )



def setup(client):
    client.add_cog(help(client))
    