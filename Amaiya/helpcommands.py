def allcommands(category):
	if category == "osu":
		message = '''
		Osu help:
		/linkosu - Link your osu account to this bot
		/mapinspiration - Receive a randomly generated map idea
		/osupfp - Get the PFP of any osu user
		/osubanner - Get the banner of any osu user
		/kudosuleaderboard - Get the kudosu leaderboard for this server (CURRENTLY DISABLED)
		/mqf_add - Add your map to the Moddinq Quickfire Queue when it is happening
		'''
	elif category == "pattern":
		message = '''
		Pattern help:\nUsed in /pattern\n\nList of available patterns, slash indicates you can use either or. All patterns can be entered plural or singular:
		anchor
		long note / ln
		grace
		chord
		jack
		trill
		chordstream
		bracket
		stream
		staircase / stair
		roll
		burst
		shield
		'''
	elif category == "games":
		message = '''
		Games help:
		/wordle - Start a wordle game
			/guess - Guess the word, can only be used once /wordle is used
		'''
	elif category == "other":
		message = '''
		Other help:
		/owo - Owofy your text
		/lore - ...
		'''
	elif category == "categories":
		message = '''
		Available /help categories:
		osu
		pattern
		games
		other
		'''
	else:
		message = '''
		Available /help categories:
		osu
		pattern
		games
		other
		'''
	
	return message

def pattern_lookup(pattern):
	
	pattern = pattern.lower()
	if 'anchor' in pattern:
		message = '''Anchors are generally many notes repeated consistently along one lane, giving it the name anchor. In general, something is considered an anchor when the repetition is in 1/2 snap or above. These are usually found in streams, either intentionally or unintentionally. Unintentional anchors can create small difficulty spikes, while intentional anchors can create some pretty awesome gameplay.
		
Now, what's the difference between an anchor and longjack? I have no idea :3

Here is an example of an anchor:
https://media.discordapp.net/attachments/617755138253389836/1167659521070616710/image.png?ex=656163ab&is=654eeeab&hm=c1ad2e1d958c69aab57ff5ab54dcd8a09dcd24d5a94c416b32c579e8f775de59&=&width=474&height=988

Image credit: forest13
		'''
	elif 'long note' in pattern or 'ln' in pattern:
		message = '''Long notes, or LNs, are the sliders of osu mania. How heavy of an LN map usually depends on the speed and the gaps between releases. 
		
Most LN maps are inverse maps - Generally these are LN patterns where the entire pattern is purely LNs, and usually the you are releasing an LN while simultaneously holding down another LN in a different lane. They are quite known for boosting Star Rating of maps to... quite high.

Here is an example of Inverse LN: https://media.discordapp.net/attachments/617755138253389836/1150147783190380725/image.png?ex=656b8298&is=65590d98&hm=a65988cebf55361562f935233cd5c6868b1592051c23f2b6d67acdf83ad25a50&=&width=770&height=988
And another example of full LN map with short releases https://media.discordapp.net/attachments/627298345823633418/1165689440983846982/image.png?ex=656cade4&is=655a38e4&hm=48450759621b00b025952d02e1e3bb34d24b74f4e3834efdc1c82d9daf4e5b61&=&width=344&height=986

Image credit: Zembonics
		'''
	elif 'grace' in pattern:
		message = '''Graces are two or more notes hit one after the other, but the distance between those two notes are incredibly close.

These are usually used to represent small sound effects or things that are too boring to be a chord :D (if you know the intro to the Intense Voice of Hatsune Miku, that)

Here's an example of graces used within a pattern: https://media.discordapp.net/attachments/617755138253389836/1173432426433892472/image.png?ex=656d299b&is=655ab49b&hm=1be9628e4cea5982ece41dcb8eb029e5b35d50eec11ba6da5e6cb651d2d29e37&=&width=658&height=808
		'''
	elif 'chord' in pattern:
		message = '''Just like a musical chord, an osu mania chord is when you hit more than one note at the same timestamp. This is also referred to as emphasis.
		
These are used to represent more impactful / prominent sounds, and can create some very cool patterns!
Each number of chord has a corresponding name:
	2 - Jump / Double
	3 - Hand / Triple
	4 - Quad
	5 - I'm ngl i'm not an expert in anything more than 4k so yeah sorry i can't do this

Here are some chords: https://media.discordapp.net/attachments/652559574229843989/804201449248522321/unknown.png?ex=65680af6&is=655595f6&hm=3abd5efdfaba000c639bfb0edade9c62ebe745f99c287ddc3e9b3ee4771b4a16&=&width=418&height=986

Image credit: my waifu sofia
		'''
	elif pattern in 'jacks':
		message = '''A jack is 2-3 or more consecutive notes in a column... isn't that the same definition as an anchor??
		
Though jacks can be dominant in one lane, the main difference between this and an anchor is that an anchor *usually* occupies one lane way more than the others. However for jacks, they can equally occupy lanes through different types of jacks. Here are some common examples, though there are way more:
	Minijack - Usually only two notes long, and having no emphasis
	Chordjack - Having many anchors on multiple lanes at the same time, these are created when you put chords every certain snap, usually 1/2, 1/3, or 1/4

Here's an example of a minijack: https://media.discordapp.net/attachments/617755138253389836/1171682031881687154/image.png?ex=6566cb6d&is=6554566d&hm=e463f201e8b85456f9b0c01cc20945173d38628239bc94f4b6c82be0974c1eb6&=&width=330&height=988
Here's an example of a chordjack: https://media.discordapp.net/attachments/617755138253389836/718492580698128495/unknown.png?ex=656a015c&is=65578c5c&hm=8e908bac8fcbaa23d22f7466dc550fefc65bd4a16ac3dce71c52250ba0ea53ab&=&width=474&height=884

Image credit: snomi and epic man 2
		'''
	elif 'trill' in pattern:
		message = '''A trill is usually when there are multiple notes alternating on two lanes. One handed trills are played by one hand (usually index and middle), and two handed trills are played with either both index or both middle. This can vary as you go up keymodes.\nThere are also commonly jumptrills or split trills, which is notes alternating between lane (1,2) and (3,4), (1,3) and (2,4), or lane (1,4) and (2,3) (for 4k, they can vary for higher keymodes, such as 7k chordtrills)
		
Trills are great for many types of sounds, but are commonly used for piano trills, and a long repeated sound where a jack will be too difficult to hit.
Jumptrills are usually used for 1/4 or faster kicks lasting for at least 1-2 bars. They can boost Star Rating a lot if used in high density snaps

Here's an example of a trill: https://media.discordapp.net/attachments/617755138253389836/1151707641853255731/image.png?ex=6567f4d3&is=65557fd3&hm=204868ee9d429396e5076efafd5ff3a85956fe43559b964612fb90ffbf432149&=&width=460&height=988

Image credit: snomi
		'''
	elif 'chordstream' in pattern:
		message = '''Chordstreams are streams with a certain type of chord in it. They can be broken down into things like jumpstreams (doubles appearing occasionally), handstream (triples appearing occasionally), quadstream, and more.
		
They're quite stamina based, especially if they go on for a long time.
Here's an example of a jumpstream: https://media.discordapp.net/attachments/617755138253389836/1172749967975268414/image.png?ex=656aae05&is=65583905&hm=e140adbb830584783723a453a4339cdada52203fd943f3b7b7ffc6c5373da1fd&=&width=522&height=986

Image credit: snomi
		'''
	elif 'bracket' in pattern:
		message = '''"Defining brackets as split trills but doubled and given to the next person is the only way I will ever describe brackets from now on" - Protastic101
		
Here's an example of a bracket: https://media.discordapp.net/attachments/617755138253389836/1163560201182511186/image.png?ex=6564eee1&is=655279e1&hm=8576deda3227b44db4624eb8a16b9dbbb2660ff68918bccb1e4fa1c5724bec37&=&width=634&height=988

Image credit: forest13
		'''
	elif 'stream' in pattern:
		message = '''A stream is a long continuous pattern of notes, usually 1/4 or higher, but can be 1/2 at fast BPM
		
They're pretty stamina based depending how long they go on for, but they're fun!
Here's an example of a stream: https://media.discordapp.net/attachments/617759068672622593/1148761412844404907/image.png?ex=6566776f&is=6554026f&hm=0dfa0c4420f22c1623c97af7a927b5c4e4a52a86b9cbcaf718d5731f0358de4b&=&width=1756&height=988

Image credit: Alumence
		'''
	elif 'staircase' in pattern or 'stair' in pattern:
		message = '''A staircase, or stairs, are patterns that go from one side of the lanes to the other, creating something that literally looks like stairs.
		
Watch out for the little anchors they create :3 but they can be pretty cool if used properly!

Here's an example of a staircase: https://media.discordapp.net/attachments/617759068672622593/1116523977519677600/image.png?ex=6569287c&is=6556b37c&hm=9c2ffe1241ddf5557a73973259c369c5add2d09af69cd7f92733c369969e3acf&=&width=1756&height=988

Image credit: Ryu Sei
		'''
	elif 'roll' in pattern:
		message = '''A roll is usually a pattern going from one end of the lanes to the other, but usually go in one direction instead of both ways like a stair.
		
People use it for drumrolls and heavy intense rhythm game music at 1/8 snap or higher.

Here's an example of a roll: https://media.discordapp.net/attachments/617755138253389836/1149769295413387366/image.png?ex=656a2219&is=6557ad19&hm=21a725842449c2cdffbba3fa1235340ae7f378aa4d6d3ac4d8a74d940fd5efdb&=&width=476&height=988

Image credit: forest13
		'''
	elif 'burst' in pattern:
		message = '''Bursts are a large cluster of fast notes in a small timeline. The name kinda says it all!
		
Here's an example of a burst: https://media.discordapp.net/attachments/652559574229843989/1121258653262037093/image.png?ex=6567ecfe&is=655577fe&hm=2d05c0ee8e8583a5574a84f7d7c88473176ef55ea72cd1c1908ab76cfba07a99&=&width=444&height=818

Image credit: Ryu Sei
		'''
	elif 'shield' in pattern:
		message = '''A shield is an LN that immediately follows a rice note on the same lane. Inverse shields are when a rice note immediately follows an LN.
		
Shield's can be fun, but if used incorrectly, can create awkward patterns and difficulty spikes.

Here's an example of an inverse shield: https://media.discordapp.net/attachments/617755138253389836/1124279680070078494/image.png?ex=6569b00b&is=65573b0b&hm=52da29ebd9af006ec8e2ee167cd525466063b01472943c5395d64cafec648546&=&width=980&height=988 
Here's an example of both types of shields: https://images-ext-1.discordapp.net/external/kqBoXXi7_qU8fi1GMWf0e3vJymMYTNMuBDWQu7Zi8UA/https/i.imgur.com/v4BPqOC.png?width=890&height=988

Image credit: Furryswan and Kurisu Makise
		'''
	else:
		message = 'Pattern not recognized, please try again, or try `/help pattern` for a full list of available ptterns'

	return message
