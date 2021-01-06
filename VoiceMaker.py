import os
from fifteen_api import FifteenAPI
import csv
import re

tts_api = FifteenAPI()

characters = [['c','Twilight Sparkle'],['i','Daring Do'],['a','Adagio Dazzle'],['h','Lyra'],['n','Maud Pie']]

previous_character = ''

def ChooseCharacter(char):
	global previous_character
	if char == 'extend':
		return previous_character
	else:
		for character in characters:
			if char[0] == character[0]:
				current_character = character[1]
				previous_character = current_character
				break			

	return current_character

def TextCorrector(txt):
	result = txt.replace("{w}","...")
	result = result.replace("{i}","")
	result = re.sub(r"\s*{.*}\s*", " ", result)
	result = re.sub(r"\s*\[.*\]\s*", " ", result)
	print(result)
	return result

with open('dialogue.tab', newline='') as dialogue:
	dialogue_reader = csv.reader(dialogue, delimiter='\t')

	firstline = True
	i = 0

	for line in dialogue_reader:

		if firstline:
			firstline = False
			continue

		#Get the character
		if line[1] != 'centered' and line[1] != '':

			final_character = ChooseCharacter(line[1])
		else: 

			continue

		#Correct the text

		if re.search('[a-zA-Z]',line[2]):

			final_text = TextCorrector(line[2])
		else:

			continue

		tts_api.save_to_file(final_character,"Neutral",final_text,line[0] + '.wav')

		os.system("ffmpeg -i " + line[0] + ".wav " + line[0] + ".ogg")
		os.remove(line[0] + ".wav")
		i = i + 1
		print(str(i) + '/' + str(3252))