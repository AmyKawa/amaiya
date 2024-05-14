# options [{},{}]
# each dict is a new paramter, name is the paramter name, description is for user experience
# type i suppose just add to all
# required is for mandatory parameters
# all paramters in the dict go into the function definition parameters too
# ----------------------------------
#@shad0wstar
#osu mania modding hub bot
#created november 12th, 2023

import discord, random, datetime, requests, json, os
from discord_slash import SlashCommand, SlashContext
from discord_slash.model import SlashCommandOptionType
from datetime import datetime as dt
from osucommands import *
from helpcommands import *

intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)
#TOKEN = (assume defined)
global mqf_queue
mqf_queue = []

# If logged in successfully, will trigger
@bot.event
async def on_ready():
	watching = discord.Activity(type=discord.ActivityType.watching, name="my Mania Modding Hub debut!")
	#game = discord.Game("Playing a game")
	#streaming = discord.Streaming(name="Streaming now!", url="http://twitch.tv/streamer_name")
	await bot.change_presence(activity=watching)
	print(f'{bot.user} succesfully logged in!')

#--------------------------------------------------------------------------------------------

@slash.slash(
	name="help",
	description="Lists all commands",
	options = [
		{
			"name" : "category",
			"description" : "Category of commands to look up. Type 'categories' for a full list",
			"type" : SlashCommandOptionType.STRING,
			"required" : True,
			
		}
	]
)
async def help(ctx, category: str):
	message = allcommands(category)
	
	await ctx.send(content=message, hidden=True)
			
#------------------------------------------Osu commands--------------------------------------------

@slash.slash(
	name="mqf_add",
	description="Add your map to the Modding Quickfire Queue",
	options = [
		{
			"name" : "link",
			"description" : "Map link",
			"type" : SlashCommandOptionType.STRING,
			"required" : True,
		}
	]
)
async def mqf_add(ctx, link: str):
	if len(mqf_queue) != 0:
		for x in mqf_queue:
			if x == link:
				await ctx.send("Error: Map already added to queue.")
				return None
	mqf_queue.append(link)
	await ctx.send("Map was added to the queue!")

@slash.slash(name="next", description="Grab the next map in the Modding Quickfire Queue")
async def mqf_next(ctx):
	role1 = discord.utils.get(ctx.guild.roles, name='Organizers')
	role2 = discord.utils.get(ctx.guild.roles, name='Beatmap Nominator')
	if role1 in ctx.author.roles or role2 in ctx.author.roles:
		if len(mqf_queue) != 0:
			await ctx.send(ctx.author.mention + ", the next map for you to mod is <" + mqf_queue[0] + "> !")
			mqf_queue.pop(0)
		else:
			await ctx.send("No maps to check right now! Users can add maps with /mqf_add")
	else:
		await ctx.send("You do not have permission to use this command")
		

@slash.slash(name="mqf_clear", description="Clear the Modding Quickfire Queue (use this when starting a new session)")
async def mqf_clear(ctx):
	role1 = discord.utils.get(ctx.guild.roles, name='Organizers')
	role2 = discord.utils.get(ctx.guild.roles, name='Beatmap Nominator')
	if role1 in ctx.author.roles or role2 in ctx.author.roles:
		mqf_queue = []
		await ctx.send("Queue cleared.")
	else:
		await ctx.send("You do not have permission to use this command")

@slash.slash(
	name="linkosu",
	description="Link your osu account to the bot (used for server-side leaderboards)",
	options = [
		{
			"name" : "username",
			"description" : "Your username",
			"type" : SlashCommandOptionType.STRING,
			"required" : True,
		}
	]
)
async def add_to_database(ctx, username: str):
	outfile = ctx.guild.name + "_user_database.txt"
	
	if os.path.exists(outfile):
		checkfile = open(outfile).read().split(',')
	
		for x in checkfile:
			y = x.lower()
			user = username.lower()
			if user == y:
				await ctx.send(f"This user is already added to the database")
				return None
			
	check = user_exists(token, username)
	if check == True:
		with open(outfile, "a") as file:
			file.write(username + ',')
		await ctx.send(f"Added **" + username + "** to the bot database")
	else:
		await ctx.send(f"Could not find user or an error occured")

# ~ @slash.slash(name="kudosuleaderboard", description="Kudosu leaderboard for this server")
# ~ async def kudosu_lb(ctx):
	# ~ kudosu_data = []
	database = ctx.guild.name + "_user_database.txt"
	checkfile = open(database).read().split(',')
	# ~ checkfile = ['icouldentthink','K0nomi','aaa_321','Gumi Fumo','lumpita','White Hare','doctormango','FerdiXIA-','[RUE]NeomiCryo','Raon2007','Ainer','nanonbandusty','harbyter','chocomilku-','A04360436','polarin','LN release','Vincus','Disguise']
	# ~ for username in checkfile:
		# ~ if username.strip():
			# ~ try:
				# ~ user_kudosu = get_user_kudosu(token, username)
				# ~ kudosu_count = user_kudosu['available']
				# ~ kudosu_data.append((username, kudosu_count))
			# ~ except Exception as e:
				# ~ print(f"Error retrieving kudosu for {username}: {e}")

	# ~ sorted_kudosu_data = sorted(kudosu_data, key=lambda x: x[1], reverse=True)

	# ~ message = '\n'.join([f"{user[0]}: {user[1]}" for user in sorted_kudosu_data])

	embed = discord.Embed(
		title=f"Kudosu Leaderboard (for {ctx.guild.name}):",
		description=message,
		color=discord.Color.blue()
	)

	embed.set_footer(text="If you do not see yourself here, you can use /linkosu <username>")
	
	# ~ #await ctx.send(embed=embed)
	# ~ await ctx.send(content=message)

	
@slash.slash(
	name="osupfp",
	description="Get the osu profile picture of any user",
	options=[
		{
			"name": "username",
			"description": "User you want to search",
			"type": SlashCommandOptionType.STRING,
			"required": True,
		}
	]
)
async def get_osu_profile_picture(ctx, username: str):
	try:
		pfp = get_user_pfp(token, username)
		if pfp:
			await ctx.send(pfp)
		else:
			await ctx.send("Profile picture not found or user does not exist.")
	except Exception as e:
		await ctx.send(f"An error occurred: {str(e)}")

@slash.slash(
	name="osubanner",
	description="Get the osu banner of any user",
	options=[
		{
			"name": "username",
			"description": "User you want to search",
			"type": SlashCommandOptionType.STRING,
			"required": True,
		}
	]
)
async def get_banner(ctx, username: str):
	try:
		pfp = get_user_banner(token, username)
		if pfp:
			await ctx.send(pfp)
		else:
			await ctx.send("Profile picture not found or user does not exist.")
	except Exception as e:
		await ctx.send(f"An error occurred: {str(e)}")

	
# Input: Pattern they want described
# Output: Description of pattern written by lovely community members
@slash.slash(
	name="pattern", 
	description="Gives a brief description of a mania pattern type",
	options = [
		{
			"name" : "pattern",
			"description" : "The pattern you want to know about",
			"type" : SlashCommandOptionType.STRING,
			"required" : True,
		}
	]
)
async def pattern_description(ctx, pattern: str):
	message = pattern_lookup(pattern)
	await ctx.send(content=message, hidden=True)

# Input: none
# Output: randomly generated map idea, gives song genre, patterns, spread/marathon, and keymode(s)
@slash.slash(name="mapinspiration", description="Get some inspiration on your next mapping project")
async def mapinspo(ctx):
	message = ctx.author.mention + ", I think... you should map "
	
	genres = ['a Camellia tiebreaker', 'an electronic', 'a ballad', 'a rock', 'a heavy metal', 'a Kpop', 'a Jpop', 'a pop', 'a video game ost', 'a novelty/meme', 'an anime', 'a hip hop', 'a classical', 'a folk', 'a jazz']
	length = ['marathon', 'spread']
	bpmtype = ['fast', 'slow', 'average'] 
	patterntype = ['jack', 'speed', 'stamina', 'tech/dump', 'inverse LN', 'LN heavy', 'hybrid']
	
	message += random.choice(genres) + ' song '
	
	lengthchoice = random.choice(length)
	
	if lengthchoice == 'marathon':
		message += 'as a marathon map. '
	else:
		message += 'with a '
		spread = random.randint(2, 10)
		if spread >= 10:
			message += '10+ '
		else:
			message += str(spread) + ' '
		message += 'difficulty spread. '
	
	key = random.randrange(4,11)
	message += 'If you can, map it in ' + str(key) + 'k. '
	
	patternchoice = random.choice(patterntype)
	message += 'The map will mainly focus on ' + patternchoice + ' patterns'
	
	
	if patternchoice == 'hybrid':
		message += '. Have fun mapping!'
	else:
		secondpatternchoice = secondpatternchoice = random.choice(patterntype)
		while secondpatternchoice == 'hybrid' or secondpatternchoice == patternchoice:
			secondpatternchoice = random.choice(patterntype)
	
		message += ', but also have ' + secondpatternchoice + ' patterns as a secondary pattern. Have fun mapping!'
	
	b = ['y', 'n']
	key2 = 0
	
	extra = random.choice(b)
	if extra == 'y':
		key2 = random.randrange(4, 11)
		while key2 == key:
			key2 = random.randrange(4,11)
			
		message += ' Oh, but as a bonus, how about try multi key? Maybe ' + str(key) + 'k and ' + str(key2) + 'k?'
	
	if key == 5 or key2 == 5:
		message += '\n\nUgh... 5k... I\'M KIDDING i love 5k i am changing my ways pls no attack'
		
	await ctx.send(content=message)
	


#------------------------------------------Shitpost commands--------------------------------------------

# Input: any string
# Output: owoify (chemistry = chemistwy, no = nowo)
@slash.slash(
	name="owo", 
	description="owo",
	options = [
		{
			"name" : "message",
			"description" : "owo",
			"type" : SlashCommandOptionType.STRING,
			"required" : True,
		}
	]
)
async def owo(ctx, message: str):
	owoify = ''
	emoticons = ['>.<', ':3', "'w'", '>w<', '0w0']
	for x in message:
		if x in {'a', 'o', 'u'}:
			owoify += x + 'w' + x
		elif x == 'r':
			owoify += 'w'
		else:
			owoify += x

	await ctx.send(content=owoify + ' ' + random.choice(emoticons))


#------------------------------------------Wordle commands--------------------------------------------

# Wordle game data
game_data = {}
word_list = ['mania', 'rice', 'jack', 'chordjacks', 'speed', 'tech', 'dump', 'inverse', 'note', 'beatmap', 'nominator', 'stream', 'osu', 'delay', 'patterns', 'grace', 'shield', 'bracket', 'stair', 'trill', 'minijack', 'hand', 'quad', 'single', 'jump', 'double', 'triple', 'roll', 'slider', 'vibro']  # Add more words as needed

# Check Guess Function
def check_guess(guess, word):
	
	# lmao guessing the wrong length removes an attempt
	if len(guess) != len(word):
		return "Invalid guess length.", False, False

	# Creates white yellow and green squares
	result = ""
	won = guess == word
	for i, letter in enumerate(guess):
		if letter == word[i]:
			result += "🟩"
		elif letter in word:
			result += "🟨"
		else:
			result += "⬜️"

	# Return squares
	return result, won or len(result) == len(word) * 6, won

# Wordle Command
@slash.slash(name="wordle", description="Play a Wordle with mania terms.")
async def wordle(ctx):
	user_id = ctx.author.id
	current_date = dt.now()
	
	# Start a new game for the user
	game_word = random.choice(word_list)
	game_data[user_id] = {"date": current_date, "word": game_word, "attempts": 0}

	await ctx.send(content="Game started! You have 6 attempts to guess a mania related word. Your word is **" + str(len(game_word)) + "** letters long. Use /guess to guess a word.", hidden=True)
	
# Guess Command
@slash.slash(
	name="guess",
	description="Make a guess in the Wordle game",
	options = [
		{
			'name' : 'word',
			'description' : 'word u want to guess',
			'type' : SlashCommandOptionType.STRING,
			'required' : True,
		}
	]
)
async def guess(ctx: SlashContext, *, word: str):
	user_id = ctx.author.id
	word = word.lower()

	# Check if the user is currently playing a game
	if user_id not in game_data or game_data[user_id]['attempts'] >= 6:
		await ctx.send(content="You are not currently playing a game or have exceeded your attempts. Use /wordle to start a new game.", hidden=True)
		return

	# Checks the guess and passes to check_guess function to return squares. Increases attempts by 1
	result, game_over, won = check_guess(word, game_data[user_id]['word'])
	game_data[user_id]['attempts'] += 1
	
	# Alright this was supposed to work for both winning and losing but man fuck this it doesn't work
	# Winning
	if game_over:
		game_result = "won" if won else "lost"
		await ctx.send(f"Congrats! You won! The word was " + game_data[user_id]['word'] + ". You won in " + str(game_data[user_id]['attempts']) + " attempts!", hidden=True)
		await ctx.send(f"{ctx.author.mention} has {game_result} a round of the Mania Wordle game!")
		del game_data[user_id]  # Remove user game data
	# Not winning, but not game over yet
	else:
		await ctx.send(content=result, hidden=True)
		await ctx.send(content="You guessed: " + word + ". You have " + str(6 - (game_data[user_id]['attempts'])) + " attempts left.", hidden=True)
		
	# Manual losing block
	if game_data[user_id]['attempts'] == 6:
		await ctx.send(content="You lost! The word was " + game_data[user_id]['word'], hidden=True)
		await ctx.send(f"{ctx.author.mention} lost the Wordle game XD")

@slash.slash(name="lore", description="bot lore")
async def lore(ctx):
	await ctx.send(f"My name is Amaiya, I am a Crypton Future Media employee. My pride and joys are Roka and Miko... well, they were. Until the *incident*. I witnessed the incident in 4K quality... no... worse than 4K quality, **5K.** It was practically real life. It caused our newest employee at the time to quit on the first day of the job.\n\nI've held onto Roka's memory since then, and Miko... well. She's alive and well. I've been playing osu!mania, but everytime I hear or see 5K, it reminds me of... that day.\n\nA fun fact about me, Hi! my full name is Inorday-Ritanmore-Parmy-Mayhop-Leatate-Icanwok-Bemoter-Amamiyama-Nowan Boblem, but you can just call me Amaiya.\n\nThat's all... I have to say for now. Roka and Miko's designs are found below.", hidden=True)
	await ctx.send('https://media.discordapp.net/attachments/804921694065786901/1176075976690630726/We_are_having_a_baby_girl_1.png?ex=656d8d1b&is=655b181b&hm=1e6e36d4b83675300c0416a67400a0170e856ccc1104ade96deedc2bfb148b70&=&width=1372&height=988', hidden=True)
	
#-------------------------------------Respond to messages on keyword trigger--------------------------------------------

@bot.event
async def on_message(message):
	
	#Make sure the Bot doesn't respond to it's own messages
	if message.author == bot.user: 
		return
		
	message.content = message.content.lower()
	namereplies = ['die', 'you\'re worse than 5k', 'play omori today https://omori-game.com/en', 'maybe one day i\'ll be friends with axer too', 'take water', 'this is not what i expected when i clicked on this link', 'what was that?', 'are you 1/cos(xy) cuz ur secxy', 'if me and you switched houses, what\'s my new address', 'the way that i know hundreds of digits of pi, but not the digits of your phone number.....', 'meow', 'ryu sei is now accepting bn requests', 'i may be stupid', 'who did this to me', 'you can bridge with gravel and sand in the end', 'map ln today', 'love me like this', 'fnf > 5k', 'in all seriousness, i don\'t really hate 5k...', '5k still traumatizes me, from that day...', 'why am i here', 'didn\'t mean to trauma dump you', 'please don\'t talk about zombies, i had a horrible experience with them once', 'literally why', 'https://media.discordapp.net/attachments/617755138253389836/1138103248344055808/prot.png?ex=65649b3f&is=6552263f&hm=fcfd806ba52e035cbfefb2529b34500d8c6109c99ade52808d0d613c1e67d5da&=&width=1656&height=956', 'https://media.discordapp.net/attachments/617755138253389836/1057678307656749056/NQEGAJ4F7M09QYNMWQ.png?ex=655e1b2f&is=654ba62f&hm=4046a5b2557157cc653c51ddc4f073583c4211c7512c53944e65c1d44d336e93&=&width=1606&height=362', 'ignore the last image i sent', 'i\'d consider geometry dash a rhythm game', 'add me on roblox', 'yes', '3k ranked maybe idk', '** **', 'by now, the quality was real life', 'miku was a japanese girl with silky sweaty black hair', 'hi there :3'] 
	protreplies = ["ily prot i swear i don\'t hate 5k will u marry me", "ily prot i love 5k", "i\'m sorry that we have beef will u forgive me protuwu"]
	
	# ~ if message.content in 'what is the meaning of life' or message.content in 'whats the meaning of life' or message.content in 'what\'s the meaning of life':
		# ~ await message.channel.send(f"to like subscribe and hit that bell")
	if 'big maxus' in message.content:
		await message.channel.send(f"BIG MAXUS")
	if 'what state do you live in' in message.content:
		await message.channel.send(f"constant despair")
	if 'owo' in message.content or 'uwu' in message.content:
		await message.channel.send(f"0w0? owo uwu :3")
	if 'k+1' in message.content:
		await message.channel.send(f"can you really call this a real keymode?")
	# ~ if 'star' in message.content or 'staring' in message.content:
		# ~ await message.channel.send(f"https://media.discordapp.net/attachments/1022746070146621462/1176115055700480010/staringustar.png?ex=656db180&is=655b3c80&hm=76fc7c3063215c4e79076b7c9711804fb1d32b10d69f658ad640903a8f976df6&=&width=656&height=374")
	if '5k' in message.content:
		if message.author.id == 888960254300274690:
			await message.channel.send(random.choice(protreplies))
		else:
			await message.channel.send(random.choice(namereplies))
	
	# ~ himitsu = ['smash or pass roka and miko', 'now, your character is real', 'new role', 'garlagan - do', 'i\'m gonna be the biggest menace and respond to himitsu everytime she chats so u have to endure this until amy gets back lol!']
	# ~ if message.author.id == 329108000197574657:
		# ~ await message.channel.send(random.choice(himitsu))
	# ~ emojis = [discord.utils.get(bot.emojis, name='hapyblob'), discord.utils.get(bot.emojis, name='sadeblob'), discord.utils.get(bot.emojis, name='wide_cat1'),discord.utils.get(bot.emojis, name='wide_cat2'),discord.utils.get(bot.emojis, name='blob_voring'),discord.utils.get(bot.emojis, name='redjunimo'),discord.utils.get(bot.emojis, name='yellowjunimo'),discord.utils.get(bot.emojis, name='greenjunimo'),discord.utils.get(bot.emojis, name='bluejunimo'),discord.utils.get(bot.emojis, name='purplejunimo'),discord.utils.get(bot.emojis, name='pinkjunimo')]
	
	# ~ for x in emojis:
		# ~ await message.add_reaction(x)
	
	
	
bot.run(TOKEN)

