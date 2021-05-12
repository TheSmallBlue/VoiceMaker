# Ren-Py-15.ai-Dubber
A python script that uses wafflecomposite/15.ai-Python-API to dub your Ren'Py game.

# Requirements

* csv
* re
* [wafflecomposite's 15.ai-Python-API](https://github.com/wafflecomposite/15.ai-Python-API)

# Installation
Open your project in the Ren'Py launcher. Click on "Extract Dialogue", then on "Tab-delimited Spreadsheet (dialogue.tab)", then on Continue.

Still on the launcher, click on "base". The root folder of your project will open. Inside the "game" folder, create a new folder named "voice"

Move the "dialogue.tab" file, located at the root of your game, into the "voice" folder you just created.

Back to the launcher, open your "options.rpy" file. Find the "init python:" header, and in it type ``config.auto_voice = "voice/{id}.ogg"``, like so:

**``options.rpy``**
```py
init python:

    #Enables automatic voice 
    config.auto_voice = "voice/{id}.ogg"
    
    
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
```

Download both the ``VoiceMaker.py`` script from this repo, and [wafflecomposite's 15.ai-Python-API](https://github.com/wafflecomposite/15.ai-Python-API) ``fifteen_api.py``

Place them both on the "voice" folder.

Open ``VoiceMaker.py`` and edit the "characters" list to the character call and the voice you want them to have. For example, I have a character who's identifier is "a", and nother who's identifier is "b". I want a to have Twilight's voice, and I want b to have Rise's. So I edit it like so: ``characters = [['a','Twilight Sparkle'],['b','Rise Kujikawa']]``. You can add as meny as you want.

Save and run ``VoiceMaker.py``. It will take a while. Like, a LONG while.

Once the script ends, launch your game and enjoy!

# To-Do's

If you wanna help out, look no further! 

* Once all the voices have been created, it'd be nice to have some sort of check to make sure that all voices are there, since 15.ai's servers like to return a 502 error from time to time


# Extra Notes:

This code can also be used with [My uberduck.ai API](https://github.com/TheSmallBlue/Uberduck.ai-Python-API) just change the following lines in ``VoiceMaker.py``:
* ``from fifteen_api import FifteenAPI`` to ``from uberduck_api import UberduckAPI``
* ``tts_api = FifteenAPI()`` to ``tts_api = UberduckAPI()``
* ``tts_api.save_to_file(final_character,"Neutral",final_text,line[0] + '.wav')`` to ``tts_api.save_to_file(final_character,final_text,line[0] + '.wav')``
