"""common slash command template"""



import disnake
from disnake.ext import commands



class slash_cmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="образец описания команды")
    async def slash_cmd(self, inter):
        await inter.send(f"образец слеш-команды", ephemeral=True)



def setup(bot):
    bot.add_cog(slash_cmd(bot))
