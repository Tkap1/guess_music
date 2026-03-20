

import glob
import re
import os

files = glob.glob("D:/music/*")

with open("index.html", "w", encoding="utf8") as out_file:
	fr = open("template.html", "r")
	template = fr.read()
	fr.close()

	text = ""
	for i, f in enumerate(files):
		match = re.search(r"\[([\d\w_]+)\]\.mp3", f)
		if match and match.re.groups == 1:
			url = match[1]
			index = f.find(match[0])
			name = f[0:f.find(match[0])]
			text += f"""
			<button onclick="toggle_video('{i}')">{os.path.basename(name)}</button>
			<div id="{i}" class="video">
			<iframe width="560" height="315"
			src="https://www.youtu.be/{url}"
			frameborder="0" allowfullscreen>
			</iframe>
			</div>
			<br>
			"""

	out_file.write(template.replace("{}", text))