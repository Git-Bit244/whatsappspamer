from termcolor import colored
import subprocess
import time
import pyautogui
import pyperclip
import keyboard
subprocess.call('', shell=True)

def SendMessage():
    time.sleep(2)
    print(colored("После того как написал зайди в Whatsapp у тебя 6 секунд :)",'yellow'))
    message = input(colored("Сообщение для спама:",'green'))
    
    iterations = 1000

    for i in range(iterations):
        pass

    while iterations > 0:
        iterations -= 1

        pyautogui.typewrite(message.strip())
        ('ctrl + v')
        pyautogui.press('enter')

    
def SendScript():
    time.sleep(6)
    print(colored("Пример: text.txt",'magenta'))
    print(colored("После того как написал зайди в Whatsapp у тебя 6 секунд :)",'yellow'))
    file = input(colored("Напиши названия файла:",'magenta'))   
    with open(file) as f:
        lines = f.readlines()
    for line in lines:
        pyautogui.typewrite(line.strip())
        ('ctrl + v')
        pyautogui.press('enter')

    

print(colored('-'*50, 'red'))
print(colored('Даров братиш', 'green'))
print(colored('-'*50, 'red'))


print(colored("\t[1] ===> Одно сообщение много раз", 'magenta' ))
print(colored("\t[2] ===> Текст по одному сообщению", 'magenta'))

print(colored('-'*50, 'red'))
print('\n')
option = input(colored('[Выбери]==> ', 'cyan'))

if option == "1":
    SendMessage()
elif option == "2":
    SendScript()
else:
    print(colored('1 или 2', 'red'))