"""deafult messages and embeds"""



import disnake



def create_embeds(emb_dicts):
    """creates a list of disnake embeds from list of dicts"""
    res = []
    for element in emb_dicts:
        embed = disnake.Embed.from_dict(element)
        res.append(embed)
    if len(res)>0:
        return res
    else:
        embed = disnake.Embed.from_dict({"title": "Embed Title","title": "Embed Title","color": 0xFEE75C})
        return [embed]



interaction_deny = 'Ты так не можешь!'



"""embed dictionaries"""
"""
to set use:
    embed=disnake.Embed.from_dict(template)
"""
"""
template = {
    "title": "Embed Title",
    "title": "Embed Title",,
    "color": 0xFEE75C,
    "timestamp": datetime.datetime.now().isoformat(),
    "author": {
        "name": "Embed Author",
        "url": "https://disnake.dev/",
        "icon_url": "https://disnake.dev/assets/disnake-logo.png",
    },
    "thumbnail": {"url": "https://disnake.dev/assets/disnake-logo.png"},
    "fields": [
        {"name": "Regular Title", "value": "Regular Value", "inline": "false"},
        {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
        {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
        {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
    ],
    "image": {"url": "https://disnake.dev/assets/disnake-banner-thin.png"},
    "footer": {"text": "Embed Footer", "icon_url": "https://disnake.dev/assets/disnake-logo.png"},
}
"""