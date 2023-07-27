import discord
from discord.ext import commands
import responses
import os
from pychess import chess_game
from dotenv import load_dotenv

# here we use ! to call the bot, when we call the bot we initialize the board    
def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix='!', intents=intents)
    game = chess_game.initialize_board()

    @bot.command()
    async def play_chess(ctx):
        await ctx.send('Let\'s play chess!')
        board_svg = chess_game.display_board(game)
        await ctx.send(file=discord.File(fp=board_svg, filename='board.svg'))
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')

    @bot.command()
    async def hello(ctx):
        await ctx.send('Hello, how are you?')
    
    @bot.command()
    async def move(ctx, move):
        global game
        success = chess_game.make_move(game, move)
        
        if success:
            board_svg = chess_game.display_board(game)
            await ctx.send(file=discord.File(fp=board_svg, filename='board.svg'))
        
            if chess_game.game_over(game):
                await ctx.send('Game over!')
                game = chess_game.initialize_board()
        else:
            await ctx.send('Invalid move')

    @bot.command()
    async def display_board(ctx):
        chess_game.display_board(game)
    
    @bot.command()
    async def send_message(message, user_message):
        try:
            response = responses.handle_response(user_message)
            await message.author.send(response) 
            message.channel.send(response)
        
        except Exception as e:
            print(e)
    
    bot.run(TOKEN)