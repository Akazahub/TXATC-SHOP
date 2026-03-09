import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=[".", "!"], intents=intents)

# ROLE THAT CAN USE COMMANDS
ALLOWED_ROLE_ID = 1477803998345167031


@bot.check
async def globally_block_commands(ctx):
    return any(role.id == ALLOWED_ROLE_ID for role in ctx.author.roles)

@bot.command(name="tos")
async def tos(ctx):
    embed = discord.Embed(
        title="TXATC SHOP",
        description=(
            "📜 **TERMS OF SERVICE**\n\n"

            "💲 **Payment Rules**\n"
            "• Full payment required before order processing.\n"
            "• No cancellations after payment is sent.\n"
            "• No chargebacks, disputes, or payment reversals.\n"
            "• Wrong address (e.g., LTC, PayPal) = ❌ No refund.\n\n"

            "📦 **Delivery & Proof**\n"
            "• Orders are delivered via DM or Ticket.\n"
            "• Orders are processed after payment confirmation.\n"
            "• Shipping times are estimates and may vary.\n"
            "• Once shipped, responsibility transfers to buyer.\n\n"

            "🔁 **Refunds & Replacements**\n"
            "• No refunds unless stock is unavailable and valid proof is provided.\n"
            "• Replacements only for damaged or incorrect items.\n"
            "• Refunds only considered if wrong item was sent.\n"
            "• No replacements without proper evidence.\n"
            "• Claims must be submitted within 48 hours of delivery.\n"

            "**buying = agreeing to the tos**"
        ),
        color=discord.Color.dark_purple()
    )
    embed.set_footer(text="TXATC's manager")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1464614742818689067/1479671675791605780/2290a773-e160-4fe9-896e-e03fdc72577a.png?ex=69aedd62&is=69ad8be2&hm=c288cea57e2981d0aaf8f14fb42a4678a6ec2f53cd5a050920e11dfaed9c5661&=&format=webp&quality=lossless&width=960&height=960")
    embed.set_image(url="https://cdn.discordapp.com/attachments/1464614742818689067/1480222220587499612/2EF2A6FA-3D9C-441E-ADDA-7F10A315C866.png?ex=69aee3de&is=69ad925e&hm=5e0ec759b13a84ffdfa5e5dfa675a5510a0c7f104b279c4a14f3f8a25149e9f6&")
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="TXATC")
    )
    print(f"Logged in as {bot.user}")


@bot.command(name="legit")
async def legit(ctx):
    embed = discord.Embed(
        title="Is TXATC SHOP Legit?",
        description="React below:\n\n✅ = Yes\n❌ = No\n\nReact ❌ without proof may result in a ban.",
        color=discord.Color.dark_purple()
    )

    embed.set_footer(text="TXATC's manager")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1464614742818689067/1479671675791605780/2290a773-e160-4fe9-896e-e03fdc72577a.png?ex=69aedd62&is=69ad8be2&hm=c288cea57e2981d0aaf8f14fb42a4678a6ec2f53cd5a050920e11dfaed9c5661&=&format=webp&quality=lossless&width=960&height=960")

    msg = await ctx.send(embed=embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("❌")


@bot.command(name="payments")
async def payments(ctx):
    embed = discord.Embed(
        title="💳 Payment Methods",
        description="We only accepts the following payment methods:",
        color=discord.Color.dark_purple()
    )

    embed.add_field(
        name="",
        value="• **LTC**\n• **USDT**\n• **Paypal**\n• **Cashapp**",
        inline=False
    )

    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1464614742818689067/1479671675791605780/2290a773-e160-4fe9-896e-e03fdc72577a.png?ex=69aedd62&is=69ad8be2&hm=c288cea57e2981d0aaf8f14fb42a4678a6ec2f53cd5a050920e11dfaed9c5661&=&format=webp&quality=lossless&width=960&height=960")
    embed.set_footer(text="TXATC's manager")

    await ctx.send(embed=embed)


TOS_CHANNEL_ID = 1477673751721021575
PAYMENTS_CHANNEL_ID = 1479144203916415208


@bot.command(name="start")
async def start(ctx):
    tos_ch = ctx.guild.get_channel(TOS_CHANNEL_ID)
    pay_ch = ctx.guild.get_channel(PAYMENTS_CHANNEL_ID)

    embed = discord.Embed(
        title="TXACT",
        description=(
            "**Before purchasing please read the following:**\n"
            f"- 💳 **Check {pay_ch.mention}**, see the accepted payment options.\n"
            f"- 📜 **Read {tos_ch.mention}**, make sure you understand the terms before buying.\n\n"
            "**Important Note:**\n"
            "- Using a middleman is allowed."
        ),
        color=discord.Color.dark_purple()
    )

    embed.set_footer(text="TXATC's manager")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1464614742818689067/1479671675791605780/2290a773-e160-4fe9-896e-e03fdc72577a.png?ex=69aedd62&is=69ad8be2&hm=c288cea57e2981d0aaf8f14fb42a4678a6ec2f53cd5a050920e11dfaed9c5661&=&format=webp&quality=lossless&width=960&height=960")

    await ctx.send(embed=embed)


user_ltc = {}

@bot.command(name="setltc")
async def setltc(ctx, address):
    user_ltc[ctx.author.id] = address
    await ctx.send("LTC address saved.")

@bot.command(name="ltc")
async def ltc(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    address = user_ltc.get(member.id)

    if not address:
        await ctx.send("No LTC address set for this user.")
        return

    await ctx.send(address)


user_usdt = {}

@bot.command()
async def setusdt(ctx, address):
    user_usdt[ctx.author.id] = address
    await ctx.send("USDT address saved.")

@bot.command()
async def usdt(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    address = user_usdt.get(member.id)

    if not address:
        await ctx.send("No USDT address set for this user.")
        return

    await ctx.send(address)

@bot.command(name="ca")
async def cashapp(ctx):
    await ctx.send("$trap0utaspect")

@bot.command(name="pp")
async def paypal(ctx):
    await ctx.send("https://www.paypal.com/paypalme/Abdo2403")

@bot.command(name="blox")
async def bloxfruits(ctx):
    embed = discord.Embed(
        title="Blox Fruits",
        description=(
            "Galaxy kitsune $21/1\n"
            "Ember dragon $18/1\n"
            "Crimson kitsune $16/1\n"
            "West dragon $14/1\n"
            "East dragon $12/1\n"
            "Kitsunes $2/1\n\n"
            "**Anything else make a ticket to negotiate prices**"
        ),
        color=discord.Color.dark_purple()
    )

    embed.set_footer(text="TXATC's manager")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1464614742818689067/1479671675791605780/2290a773-e160-4fe9-896e-e03fdc72577a.png?ex=69aedd62&is=69ad8be2&hm=c288cea57e2981d0aaf8f14fb42a4678a6ec2f53cd5a050920e11dfaed9c5661&=&format=webp&quality=lossless&width=960&height=960")
    
    await ctx.send(embed=embed)

@bot.command(name="robux")
async def robux(ctx):
    embed = discord.Embed(
        title="Robux",
        description=(
            "<a:Fluxkigmaiarrow:1462418714790985821> 4.5$/1k —> **In-game gifting** or tax **not** covered <:robux:1464918905159024826>\n\n"
            "<a:Fluxkigmaiarrow:1462418714790985821> 5.5$/1k —> **Tax covered** <:robux:1464918905159024826>"
        ),
        color=discord.Color.dark_purple()
    )

    embed.set_footer(text="TXATC's manager")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1464614742818689067/1479671675791605780/2290a773-e160-4fe9-896e-e03fdc72577a.png?ex=69aedd62&is=69ad8be2&hm=c288cea57e2981d0aaf8f14fb42a4678a6ec2f53cd5a050920e11dfaed9c5661&=&format=webp&quality=lossless&width=960&height=960")
    await ctx.send(embed=embed)


TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN environment variable not found")

bot.run(TOKEN)



