import configs.DefaultConfig as defaultConfig
import utils.DiscordUtil as discordUtil

import asyncio
import discord
from discord.ext import commands,tasks
from cogs.GeminiCog import GeminiAgent
import datetime

intents=discord.Intents.all()
intents.message_content=True
intents.members=True
bot=commands.Bot(command_prefix="!",intents=intents,help_command=None)

# Reminder Storage
reminders = []

@bot.event
async def on_ready():
    print("Bot is online..")
    check_reminders.start()


@bot.event
async def on_member_join(member):
    print('New member is joining')
    guild=member.guild
    guildname=guild.name
    dmchannel=await member.create_dm()
    await dmchannel.send(f"Welcome to {guildname}! Feel free to ask any questions here.")

@bot.command(aliases = ["about"])
async def help(ctx):
    MyEmbed = discord.Embed(title = "Commands",
                            description = "These are the Commands that you can use for this bot. Once you are in a private message with the bot you can interact with it normally without issuing commands",
                            color = discord.Color.dark_purple())
    MyEmbed.add_field(name = "!query", value = "This command allows you to communicate with Gemini AI Bot on the Server. Please wrap your questions with quotation marks.", inline = False)
    MyEmbed.add_field(name = "!pm", value = "This command allows you to private message the Gemini AI Bot.", inline = False)
    MyEmbed.add_field(name = "!set_reminder", value = "This command allows you to set reminder.", inline = False)
    MyEmbed.add_field(name = "!delete_reminder", value = "This command allows you to delete reminder.", inline = False)
    MyEmbed.add_field(name = "!list_reminders", value = "This command allows you to view the list of reminders.", inline = False)
    await ctx.send(embed = MyEmbed)

@bot.command()
@commands.check(discordUtil.is_me)
async def unloadGemini(ctx):
    await bot.remove_cog('GeminiAgent')

@bot.command()
@commands.check(discordUtil.is_me)
async def reloadGemini(ctx):
    await bot.add_cog(GeminiAgent(bot))

async def startcogs():
    await bot.add_cog(GeminiAgent(bot))

@bot.command()
async def set_reminder(ctx, date_time: str, *, reminder_text: str):
    try:
        reminder_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        reminders.append({"time": reminder_time, "text": reminder_text, "channel": ctx.channel.id})
        await ctx.send(f"Reminder set for {date_time}: {reminder_text}")
    except ValueError:
        await ctx.send("Invalid date format. Use: YYYY-MM-DD HH:MM")

@tasks.loop(seconds=60)
async def check_reminders():
    now = datetime.datetime.now()
    to_remove = []
    for reminder in reminders:
        if now >= reminder["time"]:
            channel = bot.get_channel(reminder["channel"])
            if channel:
                await channel.send(f"Reminder: {reminder['text']}")
            to_remove.append(reminder)

    for reminder in to_remove:
        reminders.remove(reminder)

@bot.command()
async def delete_reminder(ctx, *, reminder_text):
    global reminders
    reminders = [r for r in reminders if r['text'] != reminder_text]
    await ctx.send(f"Deleted reminder: {reminder_text}")

@bot.command()
async def list_reminders(ctx):
    if not reminders:
        await ctx.send("No reminders set.")
        return

    reminder_list = "\n".join([f"{r['time']} - {r['text']}" for r in reminders])
    await ctx.send(f"Reminders:\n{reminder_list}")


asyncio.run(startcogs())
bot.run(defaultConfig.DISCORD_SDK)