@client.command()
async def skeet(ctx):
    async with ctx.typing():
        await ctx.send(f'no skeet, no speak!')
