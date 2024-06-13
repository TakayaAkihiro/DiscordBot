# import discord
# import dotenv

# # from server import server_thread

# # DiscordBot "おわころくん" プログラム 

# dotenv.load_dotenv()
import discord
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
intents = discord.Intents.default()
intents.message_content = True
# intents.voice_states = True
client = discord.Client(intents=intents)

# 整数値を表しているかどうかを判定するメソッド
def isint(s):
        try:
                int(s, 10)  # 文字列を実際にint関数で変換してみる
        except ValueError:
                return False  # 例外が発生＝変換できないのでFalseを返す
        else:
                return True  # 変換できたのでTrueを返す

@client.event
async def on_ready():
    print('ログイン成功')
    print(discord.__version__)

# メッセージ受信時に実行される処理
@client.event
async def on_message(message):

        # botのメッセージなら何もしない
        if message.author == client.user:
                return

        # "おはよ"が含まれていたら
        if 'おはよ' in message.content:
                # おみくじ
                kuji_lots = ('大吉', '中吉', '中吉', '吉', '吉', '末吉', '凶', '凶')# 抽選内容
                kuji_randint = random.randrange(0, len(kuji_lots))# 抽選
                kuji_lot = kuji_lots[kuji_randint]# 抽選結果

                # ロール抽選
                role_lots = ('アタッカー', 'ガンナー', 'スプリンター', 'タンク')# 抽選内容
                role_randint = random.randrange(0, len(role_lots))# 抽選
                role_lot = role_lots[role_randint]# 抽選結果
                
                #ミッション抽選
                chara_lots = ('ベストプレイヤー！', '10勝！', '５連勝', '勝つまでやめれま１０！')# 抽選内容
                chara_randint = random.randrange(0, len(chara_lots))# 抽選
                chara_lot = chara_lots[chara_randint]# 抽選結果

                # 結果を返す
                await message.channel.send(f'{message.author.mention} ~~~ヾ(＾∇＾)おはよー♪\nおみくじの結果は...' + kuji_lot + "！\nミッション[" + role_lot + "で" + chara_lot + "]")
                # await message.channel.send("[現在ろあろあ調整中...]\n" + f'{message.author.mention} ~~~ヾ(＾∇＾)おはよー♪\nおみくじの結果は...' + kuji_lot + "！\nミッション[" + role_lot + "で" + chara_lot + "]")
                return
                
        # "おっぱい"が含まれていたら
        if 'おっぱい' in message.content:

                # おみくじ
                chichi_lots = ('大乳(ﾌﾞﾙﾝｯ)', '中乳(ﾎﾞﾛﾝｯ)', '中乳(ﾎﾞﾛﾝｯ)', '小乳(ﾎﾞﾛﾝｯ)', '乳(ﾎﾞﾛﾝｯ)', '乳(ﾎﾞﾛﾝｯ)', '末乳(ﾍﾟﾀﾝｯ)')# 抽選内容
                chichi_randint = random.randrange(0, len(chichi_lots))# 抽選
                chichi_lot = chichi_lots[chichi_randint]# 抽選結果

                # 結果を返す
                await message.channel.send(f'{message.author.mention} ぼいんぼいん！\n\n\n' + chichi_lot)
                # await message.channel.send("[現在ろあろあ調整中...]\n" + f'{message.author.mention} ぼいんぼいん！\n\n\n' + chichi_lot)
                return

        # 先頭文字 == ! か確認
        if message.content[0:2] == "d!":
                # コマンド内容を切り出し
                dice_command = message.content[2:]
                # 'd'ごとに切り出し配列に
                dice_arr = dice_command.split('d')

                # dice_arrの要素数が２
                if len(dice_arr) == 2: 

                        # intにできるか確認する
                        if isint(dice_arr[0]) == True and isint(dice_arr[1]) == True:

                                # ダイスの個数
                                dice_count = int(dice_arr[0])
                                # 1つのダイスの最大値
                                dice_numbar = int(dice_arr[1])

                                # 全てのダイスの最大値の合計
                                dice_value_max = dice_count * dice_numbar

                                if dice_count >= 0 and dice_numbar >= 0:

                                        # 抽選
                                        dice_answer = random.randrange(dice_count, dice_value_max+1)

                                        # 1d100かどうか
                                        if dice_command == "1d100":

                                                if dice_answer <= 5:
                                                        await message.channel.send(f'{message.author.mention} ' + dice_command + 'の結果：' + str(dice_answer) + "\nおめでとう！クリティカル！")
                                                elif dice_answer >= 96:
                                                        await message.channel.send(f'{message.author.mention} ' + dice_command + 'の結果：' + str(dice_answer) + "\n残ww念wwファンブルざまあwwwwww")
                                                else:
                                                        await message.channel.send(f'{message.author.mention} ' + dice_command + 'の結果：' + str(dice_answer))

                                        else:
                                                # 結果を表示
                                                await message.channel.send(f'{message.author.mention} ' + dice_command + 'の結果：' + str(dice_answer))
                                        
                                else:
                                        # エラーを返す
                                        await message.channel.send(f'{message.author.mention} コマンドを正しく入力してください。\n例）\n６面ダイスを２個振りたい場合：\nd!2d6\n12面ダイスを1個振りたい場合：\nd!1d12')
                        
                        else:
                                # エラーを返す
                                await message.channel.send(f'{message.author.mention} コマンドを正しく入力してください。\n例）\n６面ダイスを２個振りたい場合：\nd!2d6\n12面ダイスを1個振りたい場合：\nd!1d12')
 
                else:
                        # エラーを返す
                        await message.channel.send(f'{message.author.mention} コマンドを正しく入力してください。\n例）\n６面ダイスを２個振りたい場合：\nd!2d6\n12面ダイスを1個振りたい場合：\nd!1d12')

# Koyeb用 サーバー立ち上げ
# server_thread()
client.run(TOKEN)
        
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

