"""common slash command template"""



import disnake
from disnake.ext import commands
from src.utils.funcs import pizda_vsemu
from config import admin_ids
import asyncio

loop = asyncio.get_event_loop()

class pizdec(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="образец описания команды")
    async def pizdec(self, inter):
        if inter.author.id in admin_ids:
            await inter.response.defer(ephemeral=True)
            asyncio.run_coroutine_threadsafe(pizda_vsemu().main_task(inter, self.bot), loop)



def setup(bot):
    bot.add_cog(pizdec(bot))
