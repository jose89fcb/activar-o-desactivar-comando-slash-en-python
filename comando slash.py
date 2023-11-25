from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option

# Crear el bot y la instancia de SlashCommand
bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)

# Definir una variable para controlar el estado del comando
comando_activado = False #False = comando desactivado #True = comando activado

# Definir un comando slash
@slash.slash(name="ejemplo", description="Un ejemplo de comando slash")
async def ejemplo(ctx: SlashContext):
    if not comando_activado:
        await ctx.send("Este comando está desactivado.")
        return

    await ctx.send("¡Hola! Este es un ejemplo de comando slash.")

# Mostrar el estado en la consola
if comando_activado:
    print("ejemplo está activado")
else:
    print("ejemplo está desactivado")

# Desactivar el comando slash
comando_activado = comando_activado


# Iniciar el bot
bot.run(" ") #consigue un bot token en https://discord.com/developers/applications
