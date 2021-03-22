import pyautogui, time

time.sleep(5)

f = open('rick.txt' 'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
else:
    print("Finished Spamming")