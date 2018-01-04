import discord
import asyncio
import sys
import os
import datetime
from discord.ext.commands import Bot


def main():
    
    
    client = discord.Client()
    
    
    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')
        
        
    client.run(os.environ['BOT_CLIENT_TOKEN'])
    
    
if __name__ == '__main__':
    main()
