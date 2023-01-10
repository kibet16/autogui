import time
import pyautogui
import  random, string

stri =  string.ascii_lowercase

message = "".join(random.sample(stri, 8))
number  =  input("Enter number: ")

time.sleep(.1)
for i in range(int(number)):
    stri = string.ascii_lowercase
    message = "".join(random.sample(stri, 5))
    pyautogui.typewrite(message)
    pyautogui.press('Enter: ')

