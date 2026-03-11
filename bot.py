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
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/uivLzTs7ep6MdoHExeUGlX4lVxS89HpzpuM8T3sxBHA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1464359207368261866/1d4713cb32f5f57c0e611fcdee70be8f.png?format=webp&quality=lossless")
    embed.set_image(url="https://media.discordapp.net/attachments/1480478586036162632/1480610047267700871/banner.png?ex=69b04d0f&is=69aefb8f&hm=f2b32b4d63e8fe730be214442b6c490cb3ff93ddebfda34791dbcff67a7e435e&=&format=webp&quality=lossless&width=1376&height=917")
    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="TXATC discord.gg/txatc")
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
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/uivLzTs7ep6MdoHExeUGlX4lVxS89HpzpuM8T3sxBHA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1464359207368261866/1d4713cb32f5f57c0e611fcdee70be8f.png?format=webp&quality=lossless")

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

    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/uivLzTs7ep6MdoHExeUGlX4lVxS89HpzpuM8T3sxBHA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1464359207368261866/1d4713cb32f5f57c0e611fcdee70be8f.png?format=webp&quality=lossless")
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
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/uivLzTs7ep6MdoHExeUGlX4lVxS89HpzpuM8T3sxBHA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1464359207368261866/1d4713cb32f5f57c0e611fcdee70be8f.png?format=webp&quality=lossless")

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
            "**Galaxy kitsune $21/1**\n"
            "**Ember dragon $17/1**\n"
            "**Crimson kitsune $15/1**\n"
            "**West dragon $14/1**\n"
            "**East dragon $12/1**\n"
            "**Kitsunes $2/1\n**\n"
            "**Anything else make a ticket in <#1477674326806368538> to negotiate prices**"
        ),
        color=discord.Color.dark_purple()
    )

    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/uivLzTs7ep6MdoHExeUGlX4lVxS89HpzpuM8T3sxBHA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1464359207368261866/1d4713cb32f5f57c0e611fcdee70be8f.png?format=webp&quality=lossless")
    
    await ctx.send(embed=embed)

@bot.command(name="accs")
async def accs(ctx):
    embed = discord.Embed(
        title="Aged Accounts:",
        description=(
            "**2026-2024 - 1$/0.86€**\n"
            "**2023-2022 - 1.5$/1.3€**\n"
            "**2021-2020 - 2$/1.73€**\n"
            "**2019 - 3$/2.6€**\n"
            "**2018 - 4$/3.43€**\n"
            "**2017 - 6$/5.15€**\n"
            "**2016 - 12$/10.3€**\n\n"
            "Make a ticket in <#1477674326806368538> if interested"
        ),
        color=discord.Color.dark_purple()
    )
    
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/uivLzTs7ep6MdoHExeUGlX4lVxS89HpzpuM8T3sxBHA/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1464359207368261866/1d4713cb32f5f57c0e611fcdee70be8f.png?format=webp&quality=lossless")
    embed.set_footer(text="TXATC Shop")
    await ctx.send(embed=embed)

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN environment variable not found")

bot.run(TOKEN)









