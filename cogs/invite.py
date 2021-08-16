import discord
from discord.ext import commands
from discord_slash import cog_ext



class invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['Invite','inv', 'inviteme'])
    async def invite(self, ctx):
        dm_embed = discord.Embed(
            color=0xA6FF0A
        )
        dm_embed.add_field(name ="THANK YOU FOR CHOOSING ME!",value="[click here](https://discord.com/api/oauth2/authorize?client_id=876540023615397908&permissions=260382780481&scope=bot%20applications.commands) to invite me")

        ch_embed = discord.Embed(
            color=0xA6FF0A,
            description=f":white_check_mark: Check you dm {ctx.author.mention}"
        )
        await ctx.send(embed=ch_embed)
        await ctx.author.send(embed=dm_embed)

    @cog_ext.cog_slash(name="invite", description='invite the bot in your server')
    async def invite(self, ctx):
        dm_embed = discord.Embed(
            color=0xA6FF0A
        )
        dm_embed.add_field(name ="THANK YOU FOR CHOOSING ME!",value="[click here](https://discord.com/api/oauth2/authorize?client_id=876540023615397908&permissions=260382780481&scope=bot%20applications.commands) to invite me")

        ch_embed = discord.Embed(
            color=0xA6FF0A,
            description=f":white_check_mark: Check you dm {ctx.author.mention}"
        )
        await ctx.send(embed=ch_embed)
        await ctx.author.send(embed=dm_embed)



def setup(client):
    client.add_cog(invite(client))
    