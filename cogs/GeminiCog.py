import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import configs.DefaultConfig as defaultConfig
import utils.DiscordUtil as discordUtil
from discord.ext import commands
import google.generativeai as genai
import json
import datetime


genai.configure(api_key=defaultConfig.GEMINI_SDK)
DISCORD_MAX_MESSAGE_LENGTH=2000
PLEASE_TRY_AGAIN_ERROR_MESSAGE='There was an issue with your question please try again....'

class GeminiAgent(commands.Cog):
    
    def __init__(self, bot):
        self.bot=bot
        self.model=genai.GenerativeModel('gemini-2.0-flash-lite')

    @commands.Cog.listener()
    async def on_message(self,msg):
        try:
            if msg.content=='ping gemini-agent':
                await msg.channel.send('Gemini Agent is online')
            elif 'Direct Message' in str(msg.channel) and not msg.author.bot:
                response = self.gemini_generate_content(msg.content)
                dmchannel = await msg.author.create_dm()
                await self.send_message_in_chunks(dmchannel,response)  
        except Exception as e:
            return PLEASE_TRY_AGAIN_ERROR_MESSAGE+str(e)
    

    @commands.command()
    async def query(self,ctx,question):
        try:
            response=self.gemini_generate_content(question)
            await self.send_message_in_chunks(ctx,response)
        except Exception as e:
            return PLEASE_TRY_AGAIN_ERROR_MESSAGE+str(e)
        
    @commands.command()
    async def pm(self,ctx):
        dmchannel=await ctx.author.create_dm()
        await dmchannel.send('Hi How can I help you today?')
        
    def gemini_generate_content(self,content):
        try:
            return self.model.generate_content(content,stream=True)
        except Exception as e:
            return PLEASE_TRY_AGAIN_ERROR_MESSAGE+str(e)
    
    async def send_message_in_chunks(self,ctx,response):
        message = ""
        for chunk in response:
            message += chunk.text
            if len(message) > DISCORD_MAX_MESSAGE_LENGTH:
                extraMessage = message[DISCORD_MAX_MESSAGE_LENGTH:]
                message = message[:DISCORD_MAX_MESSAGE_LENGTH]
                await ctx.send(message)
                message = extraMessage
        if len(message) > 0:
            while len(message) > DISCORD_MAX_MESSAGE_LENGTH:
                extraMessage = message[DISCORD_MAX_MESSAGE_LENGTH:]
                message = message[:DISCORD_MAX_MESSAGE_LENGTH]
                await ctx.send(message)
                message = extraMessage
            await ctx.send(message)

   
