from src.utils.funcs import threadsafe_handled, coro_blank

import disnake
from disnake.ext import commands

import asyncio



dropdown_loop = asyncio.get_event_loop()



class dropdown_click (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_dropdown")
    async def dropdown_click(self,inter = disnake.MessageInteractionData):
        click = inter.data.values
        if click[0] == 'custom_value':
            asyncio.run_coroutine_threadsafe(threadsafe_handled(), dropdown_loop)
        


def setup(bot):
    bot.add_cog(dropdown_click(bot))