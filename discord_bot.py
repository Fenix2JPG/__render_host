import discord
from discord.ext import commands
import asyncio
import threading


class DiscordBot:
    def __init__(self, token):
        # Configura el bot
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix="!", intents=intents)
        self.message_content = None
        self.message = None
        self.channel_id = None
        self.token = token

        # Conecta eventos
        self.bot.event(self.on_ready)
        self.bot.event(self.on_message)

        # Inicia el bot
        self.loop = asyncio.get_event_loop()
        self.loop.create_task(self.main_loop())  # Inicia el bucle principal

        self.activ_send_message = False
        self.activ_send_image = False
        self.activ_send_video = False

        self.text = None
        self.video_path = None
        self.img_path = None

    async def on_ready(self):
        print(f'We have logged in as {self.bot.user}')

    async def on_message(self, message):

        # No responder al propio bot
        if message.author == self.bot.user:
            return

        self.message = message


    async def __send_message(self, message_content: str):
        try:
            # Espera a que el bot esté listo
            await self.bot.wait_until_ready()

            if self.message.channel.id is None:
                print("No se ha recibido ningún mensaje para obtener la ID del canal.")
                return

            # Obtén el canal usando fetch_channel
            channel = await self.bot.fetch_channel(self.message.channel.id)

            if channel is None:
                print("El canal no se pudo encontrar.")
                return

            # Envía el mensaje al canal
            await self.message.reply(message_content)
            
            print(f"Mensaje enviado a {channel.mention}")
        except discord.NotFound:
            print("El canal no se pudo encontrar.")
        except discord.Forbidden:
            print("No tengo permiso para acceder al canal.")
        except discord.HTTPException as e:
            print(f"Ocurrió un error HTTP: {e}")
        except:
            print("aazza")
    
    async def __send_image(self, image_path: str):

        try:
            # Espera a que el bot esté listo
            await self.bot.wait_until_ready()

            if self.message.channel.id is None:
                print("No se ha recibido ningún mensaje para obtener la ID del canal.")
                return

            # Obtén el canal usando fetch_channel
            if self.id == None:
            
                channel = await self.bot.fetch_channel(self.message.channel.id)
            else:
                channel = await self.bot.fetch_channel(self.id)

            if channel is None:
                print("El canal no se pudo encontrar.")
                return

            # Envía la imagen al canal
            await channel.send(file=discord.File(image_path))
            
            print(f"Imagen enviada a {channel.mention}")
        except discord.NotFound:
            print("El canal no se pudo encontrar.")
        except discord.Forbidden:
            print("No tengo permiso para acceder al canal.")
        except discord.HTTPException as e:
            print(f"Ocurrió un error HTTP: {e}")
        except Exception as e:
            print(e)

    async def __send_video(self, video_path: str):
        try:
            # Espera a que el bot esté listo
            await self.bot.wait_until_ready()

            if self.message.channel.id is None:
                print("No se ha recibido ningún mensaje para obtener la ID del canal.")
                return

            # Obtén el canal usando fetch_channel
            channel = await self.bot.fetch_channel(self.message.channel.id)

            if channel is None:
                print("El canal no se pudo encontrar.")
                return

            # Envía el mensaje al canal
            await channel.send(file=discord.File(video_path))
            
            print(f"Mensaje enviado a {channel.mention}")
        except discord.NotFound:
            print("El canal no se pudo encontrar.")
        except discord.Forbidden:
            print("No tengo permiso para acceder al canal.")
        except discord.HTTPException as e:
            print(f"Ocurrió un error HTTP: {e}")
        except Exception as e:
            print(e)

    async def main_loop(self):
        while True:
            if self.activ_send_message:
                await self.__send_message(self.text)
                self.activ_send_message = False

            if self.activ_send_video:
                await self.__send_video(self.video_path)
                self.activ_send_video = False
            if self.activ_send_image:
                await self.__send_image(self.img_path)
                self.activ_send_image = False
            await asyncio.sleep(0.5)  # Dormir un segundo para evitar el uso intensivo de CPU
            #if self.message_content is not None:
                #if self.message_content == "Hola":
                    #await self.send_message("h")
                    #self.message_content = None  # Limpiar el mensaje después de procesarlo

    def send_message(self,text):
        self.text = text
        self.activ_send_message = True
    def send_image(self,img_path,id=None):
        self.img_path = img_path
        if id != None:
            self.id = id
        self.activ_send_image = True

    def send_video(self,video_path):
        self.video_path = video_path
        self.activ_send_video = True
    def get_message(self,type):
        if self.message == None:
            return
    
        if type == "content" and not self.message.content == "":
            return self.message.content
        if type == "author_name":
            return self.message.author.name
        if type == "author_id":
            return self.message.author.id

    def reset_message(self):
        self.message.content = ""

    def run(self):
        h = threading.Thread(target=self.__run)
        h.start()
    def __run(self):    
        # Ejecuta el bot con tu token en un hilo separado
        self.loop.create_task(self.bot.start(self.token))
        self.loop.run_forever()

