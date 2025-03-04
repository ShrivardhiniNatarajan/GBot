import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import configs.DefaultConfig as defaultConfig

def is_me(ctx):
    return ctx.author.id == int(defaultConfig.DISCORD_OWNER_ID)
