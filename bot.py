import discord
from discord.ext import commands
import requests

# Beállítjuk a bot jogosultságait (Intents)
intents = discord.Intents.default()
intents.message_content = True  # Szükséges, hogy olvassa a szöveges üzeneteket

# Létrehozzuk a botot egy előtaggal (prefix), ami a ! jel lesz
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Siker! A bot bejelentkezett mint {bot.user}")

# /hello vagy !hello parancs
@bot.command(name="kosz")
async def hello(ctx):
    await ctx.send(f"Szia {ctx.author.name}! Én vagyok a te saját Discord botod. 🚀 Írd be, hogy `!teny`!")

# Külső API-ból adatot lekérdező parancs (!teny)
@bot.command(name="teny")
async def send_fact(ctx):
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            fact = response.json().get("text", "Nem találtam tényt.")
            await ctx.send(f"📖 Íme egy érdekesség a botodtól:\n> {fact}")
        else:
            await ctx.send("Hiba történt az API elérése közben.")
    except Exception as e:
        await ctx.send("Hálózati hiba lépett fel.")

if __name__ == "__main__":
    # IDE ÍRD BE A SAJÁT DISCORD TOKENEDET A IDÉZETJELEK KÖZÉ:
    DISCORD_TOKEN = "sajat repo"
    
    bot.run(DISCORD_TOKEN)