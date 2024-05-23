import logging

from disnake.ext import commands



log = logging.getLogger(__name__)



class start(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log.critical(f'started {self.bot.user}')
        print(f'started {self.bot.user}')




def setup(bot):
    bot.add_cog(start(bot))