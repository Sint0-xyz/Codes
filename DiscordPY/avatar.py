@client.command()
async def avatar(ctx, member : discord.Member=None):
    if member == None:
        member = ctx.author

    memberAvatar = member.avatar_url

    avaEmbed = discord.Embed(title=f"{member.name}'s Avatar", color=discord.Color.random())
    avaEmbed.set_image(url=memberAvatar)

    await ctx.send(embed=avaEmbed)
