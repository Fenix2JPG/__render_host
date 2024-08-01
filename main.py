from discord_bot import DiscordBot
from ia import Ia
from module_akinator import ModuleAkinator
from runear import return_eval

ia = Ia()
akinator = ModuleAkinator()
tmp_akinator =False

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')

if __name__ == "__main__":

    bot = DiscordBot(BOT_TOKEN)
    bot.run()
    
    while True:
        if bot.get_message("content") !=None:
            if bot.get_message("content") == "Hola":
                bot.send_message(f"Hola {bot.get_message('author_name')}")
            elif bot.get_message("content").startswith("IA"):
                result = ia.send_message(bot.get_message("content"))
                bot.send_message(result)
            elif "(chiste)" in bot.get_message("content"):
                bot.send_video("assets/vid/gato_riendose_meme.mp4")
            elif "(img)" in bot.get_message("content"):
                bot.send_image(img_path="image.png")
            elif bot.get_message("content") == "Akinator start":
                tmp_akinator = True
                bot.send_message(akinator.get_question())
            elif bot.get_message("content").startswith("AK") and tmp_akinator:
                if akinator.get_answer_name() != None:
                    bot.send_message(akinator.get_answer_name())
                    tmp_akinator = False
                else:
                    akinator.post_answer(bot.get_message("content"))
                    bot.send_message(akinator.get_question())

            elif bot.get_message("content").startswith("RUN"):

                code= bot.get_message("content")
                code = code.replace("RUN","")
                bot.send_message(return_eval(code))
        
            elif bot.get_message("content") == "SO":
                bot.send_message("borren el sv")
            
   
            bot.reset_message()

        