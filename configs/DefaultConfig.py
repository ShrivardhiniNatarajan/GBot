import configparser

config=configparser.ConfigParser()
config.read(r'C:\Users\shriv\OneDrive\Desktop\GoogleBot\config.ini')

DISCORD_OWNER_ID=config['DEFAULT'].get('discord_owner_id')
DISCORD_SDK=config['DEFAULT'].get('discord_sdk')
GEMINI_SDK=config['DEFAULT'].get('gemini_sdk')
#print(f"Discord SDK Token:", DISCORD_SDK)
