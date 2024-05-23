from src.utils.funcs import threadsafe_handled, coro_blank

import disnake
from disnake.ext import commands

import asyncio



button_loop = asyncio.get_event_loop()



class button_click (commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_button_click")
    async def button_click(self,inter = disnake.MessageInteraction):
        click = inter.component.custom_id
        if click == 'custom_id':
            asyncio.run_coroutine_threadsafe(threadsafe_handled(), button_loop)



def setup(bot):
    bot.add_cog(button_click(bot))