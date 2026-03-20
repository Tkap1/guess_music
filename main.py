from pydub import AudioSegment
from pydub.playback import play
import random
import re

base_path = "D:/music/"

data = [
	{ "file": "Main Theme - Bloons TD 5 [K-4SthopN2U]", },
	{ "file": "GTA San Andreas Theme Song ♫ [BEST QUALITY!] [6VewzN781wQ]", },
	{ "file": "Vampire Survivors Soundtrack - Mad Forest [Ut7sjdIoPk8]", },
	{ "file": "Overworld Day [3-PA9bexwrA]", "tags": ["terraria"], },
	{ "file": "Overworld Night [dgqRkPTKdI0]", "tags": ["terraria"], },
	{ "file": "Underground [p9kZJwdZoXM]", "tags": ["terraria"], },
	{ "file": "Ragnarok Online OST 01： Title [a9OdzOz-9-I]", },
	{ "file": "Ragnarok Online OST 11： Theme of Morroc [3-mLZN830y8]", },
	{ "file": "Naruto Akatsuki Theme song FULL   YouTube [9alCtTJu5_Y]", },
	{ "file": "Dancing Christmas and the 13th Month [xWzSm0ZvwjE]", "tags": ["ragnarok"], },
	{ "file": "Path of Exile (Original Game Soundtrack) - The Cleansing Fire (Siege of the Atlas) [FcluS8Y2mBw]", "tags": ["exarch"], },
	{ "file": "Path of Exile (Original Game Soundtrack) - Maven (Echoes of the Atlas) [HR1vy3NAOdY]", },
	{ "file": "Path of Exile (Original Game Soundtrack) - Orion (Conquerors of the Atlas) [SRq4T1r2Qlg]", },
	{ "file": "Original Tetris theme (Tetris Soundtrack) [NmCCQxVBfyM]", },
	{ "file": "Mozart - Lacrimosa [k1-TrAvp_xs]", "tags": ["hunter"], },
	{ "file": "Diablo 2 - Wilderness (HQ) [Uxg5W5wKvLE]", },
	{ "file": "Inspector Gadget Theme (The Go Go Gadget Extended Version) [rIc13VjeAw8]", },
	{ "file": "Path of Exile - Fall of Oriath - High Templar Avarius [PoE Soundtrack] [9U577pfFeFI]", },
	{ "file": "C418 - Haggstrom - Minecraft Volume Alpha [laZusNy8QiY]", },
	{ "file": "Ramsey - Goodbye  ｜ Arcane League of Legends ｜ Riot Games Music [omgSWqwVTjY]", },
	{ "file": "Woodkid - Guns for Hire ｜ Arcane League of Legends ｜ Riot Games Music [pKNEx-9OqRM]", },
	{ "file": "Pokémon Red, Blue & Yellow - Champion Battle Music (HQ) [nXgAj5KdAC0]", "tags": ["pokemon"], },
	{ "file": "Bea Miller - Playground  ｜ Arcane League of Legends ｜ Riot Games Music [3jfI-z__GY0]", },
	{ "file": "XI - Freedom Dive ↓ [OI3C9qQlb1U]", },
]


index = 0
second_arr = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]

song = None
base_audio = None
pick_song = True

while True:
	if pick_song:
		index = 0
		pick_song = False
		song = random.choice(data)
		base_audio = AudioSegment.from_mp3(f"{base_path}{song['file']}.mp3")
		data.remove(song)

	seconds = second_arr[index]
	start_time = song.get("start", 5000)
	segment = base_audio[start_time:round(start_time+seconds * 1000)]

	print(f"Guess with {seconds} second")

	while True:
		play(segment)
		guess = input()
		if guess == "":
			pass
		else:
			modified_guess = f"\\b{guess}\\b"
			matches_tag = False
			for tag in song.get("tags", []):
				if re.search(modified_guess, tag, re.IGNORECASE):
					matches_tag = True
			if matches_tag or re.search(modified_guess, song["file"], re.IGNORECASE):
				print("--------------")
				print("Correct!")
				print(song["file"])
				print("--------------")
				pick_song = True
			index += 1
			break
