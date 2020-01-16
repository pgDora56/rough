import discord, wikipedia
wikipedia.set_lang("ja")

client = discord.Client()

watch_channel = ""
notify_channel = None

@client.event
async def on_ready():
    print("Login Complete")

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if str(before.channel) == watch_channel:
            await notify_channel.send(f"{member} leave {before.channel}")
        elif str(after.channel) == watch_channel:
            await notify_channel.send(f"{member} join {after.channel}")

@client.event
async def on_message(message):
    global watch_channel, notify_channel
    if message.author.bot: return
    print(f"Get message: {message.author} > {message.content} (on {message.channel})")
    msg = message.content
    if msg == ":bye":
        await message.channel.send("Bye!")
        exit(0)
    elif msg.startswith(":watch "):
        watch_channel = msg[7:]
        notify_channel = message.channel
        await message.channel.send(f"Start to watch \"{watch_channel}\"")
    elif msg.startswith(":wiki "):
        await message.channel.send(search_wikipedia(msg[5:].strip()))

bef_search_lis = []
def search_wikipedia(search_word):
    global bef_search_lis
    if search_word.isdecimal():
        n = int(search_word) - 1
        if n < len(bef_search_lis):
            return get_wiki_page(bef_search_lis[n])
        return "Search History is nothing"
    res_list = wikipedia.search(search_word)
    if len(res_list) < 1:
        return "no article"
    if res_list[0] == search_word:
        try:
            page_content = get_wiki_page(res_list[0])
            return page_content
        except:
            print("can't get page -> show list")
    if len(res_list) == 1:
        try:
            page_content = get_wiki_page(res_list[0])
            return page_content
        except:
            print("can't get solo page -> show list")
    res = ""
    bef_search_lis = res_list
    for idx, r in enumerate(res_list):
        res += f"{idx+1}. {r}\n"
    return res

def get_wiki_page(page_n):
    page = wikipedia.page(page_n)
    f100 = "> " + page.content[:300].replace("\n","\n> ") + "...\n"
    f100 += "Link: " + page.url
    return f100

with open("tamayura_discord_token.txt") as f:
    token = f.read().strip()

client.run(token)

