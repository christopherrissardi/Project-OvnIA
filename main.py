import discord
from discord.ext import commands
from g4f.client import Client
import nest_asyncio
nest_asyncio.apply()
from g4f.cookies import set_cookies

client_gpt3 = Client()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!!!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


from g4f.cookies import set_cookies

set_cookies(".bing.com", {
  "_U": "cookie value"
})
set_cookies("chat.openai.com", {
  "access_token": "token value"
})
set_cookies(".google.com", {
  "__Secure-1PSID": ""
})

...

@bot.command()
async def projectovnia(ctx):

    embed = discord.Embed(title='')
    
    embed.add_field(name="", value=f"O Project OVNIA é um projeto em colaboração com a Google integrando o motor de inteligência artificial `Gemini-Pro` para oferecer uma boa experiência aos usuários do Bot Whois Alien, criado e interpretado por offalien. Todos os usuários estão autorizados a usarem! esperamos que você tenha uma ótima experiência ao usar a ia. Quaisquer dúvidas ou sugestões, entre em contato com o <@{589502565243289612}>.", inline=False)
    embed.add_field(name="", value="Para usar a ferramenta de inteligência articial, é importante antes saber como de fato funciona uma inteligência artificial! use a opção `./ovnia` e insira o seu parâmetro/busca/dúvida que deseja.", inline=False)
    embed.add_field(name="", value="", inline=False)
    embed.add_field(name="Exemplo:", value="", inline=False)
    embed.add_field(name="", value="`./ovnia` Sabendo que pedro alvares cabral descobriu o brasil no ano de 1500, em que dia foi descoberto a américa e quem encontrou inicialmente?", inline=False)
    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤProject OVNIAㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')
    embed.set_image(url='https://i.imgur.com/jQIkv9s.jpeg')

    await ctx.send(embed=embed)

@bot.command()
async def ia(ctx):

    embed = discord.Embed(title='')
    embed.add_field(name="Project OVNIA", value="Para visualizar a opção personalizada do Project OVNIA, digite: `./projectovnia` ou o parâmetro `./ovnia` + o que você deseja perguntar", inline=False)
    embed.add_field(name="", value="Exemplo: `./ovnia` que dia George Washington morreu?", inline=False)    
    embed.add_field(name="", value="", inline=False)    
    embed.add_field(name="OpenAI ChatGPT-4", value="O motor de inteligência usa o ChatGPT-4 como referência, use o parâmetro `./gpt4` e o que você deseja pedir.", inline=False)
    embed.add_field(name="", value="Exemplo: `./gpt4` que dia nasceu pelé?", inline=False)    
    embed.add_field(name="", value="", inline=False)    
    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤInteligências artificais disponíveisㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')

    await ctx.send(embed=embed)

@bot.command()
async def gpt4(ctx, *, question):
    response = client_gpt3.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}],
    )
    answer = response.choices[0].message.content
    embed = discord.Embed(title="", description=answer)
    embed.set_author(name='ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤOpenAI GPT-4ㅤㅤㅤㅤㅤㅤㅤㅤ', icon_url='')
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')
    await ctx.send(embed=embed, reference=ctx.message)

@bot.command()
async def ovnia(ctx, *, question):
    response = client_gpt3.chat.completions.create(
        model="gemini",
        messages=[{"role": "user", "content": question}],
    )
    answer = response.choices[0].message.content
    embed = discord.Embed(title="", description=answer)
    embed.set_footer(text='Whois Alien © All Rights Reserved', icon_url='')
    await ctx.send(embed=embed, reference=ctx.message)

TOKEN = ''
bot.run(TOKEN)
