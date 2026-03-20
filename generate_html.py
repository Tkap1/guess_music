

import glob
import re
import os

files = glob.glob("D:/music/*")

with open("index.html", "w", encoding="utf8") as out_file:
	fr = open("template.html", "r")
	template = fr.read()
	fr.close()

	text = ""
	url_text = ""
	count = 0
	for i, f in enumerate(files):
		f = f.replace("\\", "/")
		match = re.search(r"\[([\d\w_\-]+)\]\.mp3", f)
		if match and match.re.groups == 1:
			url = match[1]
			index = f.find(match[0])
			name = f[0:f.find(match[0])]
			text += f"""
			<button onclick="toggle_video(this, '{count}')">{os.path.basename(name)}</button>
			<br>
			"""
			if count > 0:
				url_text += ", "
			url_text += f"'{url}'"

			count += 1

	final_text = template.replace("{1}", text)
	final_text = final_text.replace("{2}", f"const url_arr = [{url_text}]")
	out_file.write(final_text)