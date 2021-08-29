import webbrowser
import time
import pyautogui


#1 bis 80 fertig

for i in range(51,80,1):
    for j in range(1,22,1):
        webbrowser.open('http://www.ergebnisdienst-classic.de/extern/download_spielbericht.php?seiten_id=1&staffel_id='+str(i)+'&spieltag='+str(j))
        time.sleep(0.8)
        #pyautogui.hotkey('ctrl', 'w')