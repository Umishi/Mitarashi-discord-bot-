import discord
import random
import requests

from discord.ui import Button, View
from discord.ext import commands


bot = discord.Bot()

file1 = open('data.txt', 'r')
data_list = file1.readlines()
TOKEN = data_list[0]
member_mention = data_list[1]
file1.close

file2 = open('messageData.txt','r',encoding='utf-8')
message_list = file2.readlines()
file2.close

server = []

@bot.slash_command(guild_ids = server, name = "ping", description = "ピン")
async def ping(ctx):
    await ctx.respond('pong')

def dice(time):
    s = 0
    for num in range(time):
        result = random.randint(1, 6)
        s = s + result
    return s

def dice20(time):
    s = 0
    for num in range(time):
        result = random.randint(1, 20)
        s = s + result
    return s

def dice100(time):
    s = 0
    for num in range(time):
        result = random.randint(1, 100)
        s = s + result
    return s


def str_dice():
    stR = dice(3)
    return(stR)

def con_dice():
    con = dice(3)
    return(con)

def pow_dice():
    pow = dice(3)
    return(pow)

def dex_dice():
    dex = dice(3)
    return(dex)

def app_dice():
    app = dice(3)
    return(app)

def siz_dice():
    size = dice(2) + 6
    return(size)

def int_dice():
    int = dice(2) + 6
    return(int)

def edu_dice():
    edu = dice(3) + 3
    return(edu)

def sum():
    STR = "STR : " + str(str_dice()) + "\n"
    CON = "CON : " + str(con_dice()) + "\n"
    POW = "POW : " + str(pow_dice()) + "\n"
    DEX = "DEX : " + str(dex_dice()) + "\n"
    APP = "APP : " + str(app_dice()) + "\n"
    SIZ = "SIZ : " + str(siz_dice()) + "\n"
    INT = "INT : " + str(int_dice()) + "\n"
    EDU = "EDU : " + str(edu_dice()) + "\n"

    SUM = STR + CON + POW + DEX + APP + SIZ + INT + EDU
    return(SUM)


@bot.slash_command(guild_ids = server, name = "coc_dice", description = "クトゥルフ神話TRPG 6版の能力値を一括振りします")
async def coc_dice(ctx):
    button = Button(label ="ダイスを振る", style = discord.ButtonStyle.green, emoji = "🎲")
    async def button_callback(interaction):
        await interaction.response.send_message(sum())
    button.callback = button_callback

    view = View(timeout=None)
    view.add_item(button)
    await ctx.respond("coc_能力値決め", view = view)

@bot.slash_command(guild_ids = server, name = "amongmap", description = "among us のマップを表示します")
async def amongmap(ctx):
    button1 = Button(label = "THE_SKELD", style = discord.ButtonStyle.grey)
    button2 = Button(label = "MIRA_HQ", style = discord.ButtonStyle.green)
    button3 = Button(label = "POLUS", style = discord.ButtonStyle.blurple)
    button4 = Button(label = "AIRSHIP", style = discord.ButtonStyle.red)

    view_am = View(timeout=None)
    view_am.add_item(button1)
    view_am.add_item(button2)
    view_am.add_item(button3)
    view_am.add_item(button4)
    await ctx.respond("among us マップ一覧", view = view_am)

    async def button1_callback(interaction):
        await interaction.response.send_message('kanbatch様作', file=discord.File("the_skeld.png"))
    button1.callback = button1_callback

    async def button2_callback(interaction):
        await interaction.response.send_message('kanbatch様作', file=discord.File("mira_hq.png"))
    button2.callback = button2_callback

    async def button3_callback(interaction):
        await interaction.response.send_message('kanbatch様作', file=discord.File("polus.png"))
    button3.callback = button3_callback

    async def button4_callback(interaction):
        await interaction.response.send_message('kanbatch様作', file=discord.File("airship.png"))
    button4.callback = button4_callback

@bot.slash_command(guild_ids = server, name = "create", description = "シナリオ情報、諸連絡、キャラシ、雑談、メイン（ボイス）のチャンネルを持つカテゴリを作成します")
async def create(ctx, *, category_name):
    Category_name = category_name
    Category = await ctx.guild.create_category(Category_name)
    await Category.create_text_channel("シナリオ情報")
    await Category.create_text_channel("諸連絡")
    await Category.create_text_channel("キャラシ")
    await Category.create_text_channel("雑談")
    await Category.create_voice_channel("メイン")
    await ctx.respond(f"カテゴリ {category_name}を作成しました！")


@bot.slash_command(guild_ids = server, name = "d6", description = "6面ダイスを召喚します")
async def d6(ctx):
    dice_button = Button(label ="🎲", style = discord.ButtonStyle.green)
    async def dice_button_callback(interaction):
        dice_result = dice(1)
        await ctx.send(interaction.user.name + "　1d6　=>　"+ str(dice_result))
    dice_button.callback = dice_button_callback
    view_diceb = View(timeout=None)
    view_diceb.add_item(dice_button)
    await ctx.respond("1d6ダイス", view=view_diceb)

@bot.slash_command(guild_ids = server, name = "d20", description = "20面ダイスを召喚します")
async def d20(ctx):
    dice_button = Button(label ="🎲", style = discord.ButtonStyle.green)
    async def dice_button_callback(interaction):
        dice_result = dice20(1)
        await ctx.send(interaction.user.name + "　1d20　=>　"+ str(dice_result))
    dice_button.callback = dice_button_callback
    view_diceb = View(timeout=None)
    view_diceb.add_item(dice_button)
    await ctx.respond("1d20ダイス", view=view_diceb)

@bot.slash_command(guild_ids = server, name = "d100", description = "100面ダイスを召喚します")
async def d100(ctx):
    dice_button = Button(label ="🎲", style = discord.ButtonStyle.green)
    async def dice_button_callback(interaction):
        dice_result = dice100(1)
        await ctx.send(interaction.user.name + "　1d100　=>　"+ str(dice_result))
    dice_button.callback = dice_button_callback
    view_diceb = View(timeout=None)
    view_diceb.add_item(dice_button)
    await ctx.respond("1d100ダイス", view=view_diceb)

@bot.slash_command(guild_ids = server, name = "tweet", description = "ツイート担当者にツイートを要請します")
async def tweet(ctx,*,contents):
    await ctx.respond(f"{member_mention} ツイートお願いします：{contents}")

@bot.slash_command(guild_ids = server, name = "buget_application", description = "予算を申請します")
async def buget_application(ctx, contents, price, discription):
    message_buget = await ctx.respond(f"""

予算申請

申請する物：{contents} 
値段：{price}
説明：{discription}

------------------------------------------------
承認：:thumbsup:
審議が必要：:thinking:
否認：:thumbsdown:
   
リアクションお願いします！
""")

@bot.slash_command(guild_ids = server, name = "room_open", description = "部室が開いていることをお知らせします")
async def room_open(ctx):
    rand = dice(1)-1
    random_message = message_list[rand]
    await ctx.respond(f"部室を開きました！ {random_message}")

@bot.slash_command(guild_ids = server, name = "room_close", description = "部室が閉まったことをお知らせします")
async def room_close(ctx):
    await ctx.respond("部室を閉じました！")


bot.run(TOKEN)
