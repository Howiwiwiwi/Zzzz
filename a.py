from pyrogram import Client, filters

bot = Client(

"my first project in pyrogram",

 api_id = 9028013,

 api_hash = "cc894fc40424f9c8bbcf06b7355bd69d",

 bot_token = "5334586594:AAHN34STvQnny1CV1v9y-9a701olsgizFmo"

)

@bot.on_message(filters.command("start") & filters.private)

def start(bot, message):

 bot.send_message(message.chat.id , "hello")

 if message.text == "/about":

    bot.send_message(message.chat.id , "@XOne_Team") 

bot.run()
