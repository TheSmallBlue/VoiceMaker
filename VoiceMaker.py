import subprocess
from fifteen_api import FifteenAPI
import csv
import re

tts_api = FifteenAPI()

characters = [['c', 'Twilight Sparkle'], ['i', 'Daring Do'],
              ['a', 'Adagio Dazzle'], ['h', 'Lyra'], ['n', 'Maud Pie']]

previous_character = ''


def ChooseCharacter(char):
    global previous_character
    if char == 'extend':
        return previous_character
    else:
        for character in characters:
            if char == character[0]:
                current_character = character[1]
                previous_character = current_character
                break

    return current_character


def TextCorrector(txt):
    result = txt.replace("{w}", "...")
    result = result.replace("{i}", "")
    result = re.sub(r"\s*{.*}\s*", " ", result)
    result = re.sub(r"\s*\[.*\]\s*", " ", result)
    print(result)
    return result


firstline = True
i = 0
full_length = 0

with open('dialogue.tab', newline='') as dialogue:
    full_length = len(dialogue.readlines())

with open('dialogue.tab', newline='') as dialogue:
    dialogue_reader = csv.reader(dialogue, delimiter='\t')
    for line in dialogue_reader:
        id = line[0]
        speaker = line[1]
        dialogue = line[2]

        if firstline:
            firstline = False
            continue

        # Get the character
        if speaker != '':
            final_character = ChooseCharacter(speaker)
        else:
            continue

        # Correct the text
        if re.search('[a-zA-Z]', dialogue):
            final_text = TextCorrector(dialogue)
        else:
            continue

        tts_api.save_to_file(final_character,
                             final_text, f"{id}.wav")

        subprocess.call(
            f"ffmpeg -i {id}.wav -acodec libvorbis {id}.ogg", shell=True)
        subprocess.call(f"del {id}.wav", shell=True)
        i = i + 1
        print(f"{i} / {full_length}")
