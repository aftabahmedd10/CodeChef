import pyttsx3 as tts
import os

while True:
    
    tts.speak("\nHello! I am your Assistant. Tell me what to do")
    text = input("Hello! I am your Assistant. Tell me what to do\n").lower()
    
    if(('run' in text) or ('execute' in text) or ('open' in text)) and (('chrome' in text) or ('browser' in text)):
        if (('do not' in text) or ("don't" in text)):
            tts.speak('Cooool')
            print('Coooool')
        else:
            tts.speak('Opening Chrome')
            os.system('chrome')
            tts.speak('Chrome Closed')
        
    elif(('run' in text) or ('execute' in text) or ('open' in text)) and (('notepad' in text) or ('editor' in text)):
        if (('do not' in text) or ("don't" in text)):
            tts.speak('Coooool')
            print('Coooool')
        else:
            tts.speak('Opening notepad')
            os.system('notepad')
            tts.speak('notepad Closed')
        
    elif(('run' in text) or ('execute' in text) or ('open' in text)) and (('jupyter' in text) or ('python' in text)):
        if (('do not' in text) or ("don't" in text)):
            tts.speak('Coooool')
            print('Coooool')
        else:
            tts.speak('Opening Jupyter notebook')
            os.system('jupyter Notebook (Anaconda3)')
            tts.speak('Jupyter notebook closed')

    elif(('run' in text) or ('execute' in text) or ('open' in text)) and (('player' in text) or ('media' in text)):
        if (('do not' in text) or ("don't" in text)):
            tts.speak('Coooool')
            print('Coooool')
        else:
            tts.speak('Opening Windows Media Player')
            os.system('wmplayer')
            tts.speak('Windows Media Player Closed')
            
    if (('exit' in text) or ('close' in text)):
        tts.speak('Thank You! I see you later')
        break