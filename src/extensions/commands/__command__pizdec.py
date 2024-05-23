"""common slash command template"""



import disnake
from disnake.ext import commands
from src.utils.funcs import pizda_vsemu
import asyncio

loop = asyncio.get_event_loop()

class pizdec(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="образец описания команды")
    async def pizdec(self, inter):
        await inter.response.defer(ephemeral=True)
        asyncio.run_coroutine_threadsafe(pizda_vsemu().mani_task(inter, self.bot), loop)



def setup(bot):
    bot.add_cog(pizdec(bot))
