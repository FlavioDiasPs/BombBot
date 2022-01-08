import mss
import yaml
import time
import pyautogui
import numpy as np
from cv2 import cv2
from os import system
from colorama import init, Fore

init(autoreset=True, convert=True)

''' Templates for cv2.matchTemplate() '''
btn_back_img = cv2.imread('templates/btn_back.png')
btn_ok_img = cv2.imread('templates/btn_ok.png')
btn_heroes_img = cv2.imread('templates/btn_heroes.png')
btn_treasure_hunt_img = cv2.imread('templates/btn_treasure_hunt.png')
btn_go_work_img = cv2.imread('templates/btn_go_work.png')
btn_x_img = cv2.imread('templates/btn_x.png')
btn_connect_wallet_img = cv2.imread('templates/btn_connect_wallet.png')
btn_metamask_login = cv2.imread('templates/btn_metamask_login.png')
green_bar_img = cv2.imread('templates/green_bar.png')
character_bar_img = cv2.imread('templates/character_bar.png')
text_error_img = cv2.imread('templates/text_error.png')

def banner():
    ''' Show banner '''
    clear()
    print(r'''     
 ''' + Fore.LIGHTBLUE_EX + '''88888888ba                                    88           88888888ba                         
 88      "8b                                   88           88      "8b                 ,d     
 88      ,8P                                   88           88      ,8P                 88     
 88aaaaaa8P'   ,adPPYba,   88,dPYba,,adPYba,   88,dPPYba,   88aaaaaa8P'   ,adPPYba,   MM88MMM  
 88""""""8b,  a8"     "8a  88P'   "88"    "8a  88P'    "8a  88""""""8b,  a8"     "8a    88     
 88      `8b  8b       d8  88      88      88  88       d8  88      `8b  8b       d8    88     
 88      a8P  "8a,   ,a8"  88      88      88  88b,   ,a8"  88      a8P  "8a,   ,a8"    88,    
 88888888P"    `"YbbdP"'   88      88      88  8Y"Ybbd8"'   88888888P"    `"YbbdP"'     "Y888 ''' + Fore.RESET + '''

       Instagram: ''' + Fore.LIGHTBLUE_EX + '''@carlospereira305''' + Fore.RESET + '''
       GitHub: ''' + Fore.LIGHTBLUE_EX + '''https://github.com/devcarlosalberto/BombBot\n''' + Fore.RESET)

def await_time(sleeping):
    ''' Wait for a certain amount of seconds to be passed while displaying a regressive counter of seconds to the user '''
    sleeping = sleeping
    # while sleeping >= 1:
    #     sleeping -= 1
    #     print(f'\033[K [*] BombBot entrará em ação daqui {sleeping} segundo(s)..', end='\r')
    #     time.sleep(1)

def printscreen():
    ''' Capture screen '''
    with mss.mss() as screen:
        screenshot = np.array(screen.grab(screen.monitors[1]))
        return screenshot[:,:,:3]

def positions(target, trashhold=0.9):
    ''' Identify templates on the monitor 
        target = template
        trashhold = how reliable the program is identifying the template by the robot (can go from 0.1 to 1)
    '''
    img = printscreen()
    result = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)
    w = target.shape[1]
    h = target.shape[0]
    yloc, xloc = np.where(result >= trashhold)
    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    return rectangles

def scroll():
    ''' Scroll the mouse '''
    x = 0
    while x < 20:
        pyautogui.scroll(-1)
        x += 1
    time.sleep(3)

def click(target, max_attemps = 10):
    ''' Click on an identified image
        target = template
        max_attemps = maximum attempts to click this template
     '''
    attemps = 0
    while attemps < max_attemps:
        try:
            matches = positions(target)
            x,y,w,h = matches[0]
            pyautogui.moveTo(x+w/2,y+h/2,1)
            pyautogui.click()
            return True
        except:
            attemps += 1
            time.sleep(1)
            continue
    else:
        return False

def check_target(target):
    ''' Check for an identified template on the monitor
        target = template
    '''
    try:
        positions(target)[0]
        return True
    except:
        return False

def check_wallet():
    ''' Check if you are connected to your wallet or have been disconnected from any errors '''
    global btn_connect_wallet_img, btn_ok_img, text_error_img
    print('\033[K [*] Verificando se está conectado ao jogo..')
    if check_target(btn_connect_wallet_img) == True:
        return False
    elif check_target(text_error_img) == True:
        click(btn_ok_img)
        return False
    else:
        return True

def click_go_work():
    ''' Activate heroes that are being displayed on the monitor with green stamina '''
    global green_bar_img
    offset = 170
    not_working_green_bars = []
    green_bars = positions(green_bar_img, trashhold=0.9)
    for bar in green_bars:
        not_working_green_bars.append(bar)
    if len(not_working_green_bars) > 0:
        for (x, y, w, h) in not_working_green_bars:
            pyautogui.moveTo(x+offset+(w/2),y+(h/2),1)
            pyautogui.click()
    return len(not_working_green_bars)

def send_heroes_go_work():
    ''' Send heroes to work '''
    global btn_back_img, btn_heroes_img, btn_x_img, character_bar_img, btn_treasure_hunt_img
    print(' [*] Colocando heróis com estamina para trabalhar!')
    heroes_go_work = 0
    click(btn_back_img)
    click(btn_heroes_img)
    time.sleep(4)
    scrolls = 0
    while scrolls <= 2:
        heroes_go_work += click_go_work()
        if scrolls != 2:
            click(character_bar_img)
            scroll()
        scrolls += 1
    if heroes_go_work != 0:
        print(' [*] Herói(s) colocado(s) para trabalhar.')
    else:
        print(' [*] Sem heróis com estamina suficiente ou todos os heróis aptos já estão trabalhando.')
    print(' [*] Voltando para o modo Treasure Hunt..')
    click(btn_x_img)
    click(btn_treasure_hunt_img)

def refresh_page():
    pyautogui.press('f5')
    pyautogui.press('enter')

def connect_wallet():
    ''' Sign in, connect, or reconnect the game with metamask '''
    global btn_connect_wallet_img, btn_metamask_login, btn_ok_img, btn_treasure_hunt_img, text_error_img
    print(' [*] Conectando Wallet..')
    refresh_page()
    while check_target(btn_connect_wallet_img) == False:
        pass
    else:
        click(btn_connect_wallet_img)

    print(' [*] Assinando metamask..')
    point = 1
    while check_target(btn_metamask_login) == False:
        if check_target(text_error_img) == True:
            click(btn_ok_img)
            return False
        else:
            print(f'\033[K [*] Aguardando metamask..{"."*point}', end='\r')
            point += 1
            time.sleep(1)
    else:
        click(btn_metamask_login)
        print(f'\033[K [*] Conectado com sucesso!')

    print(' [*] Aguardando carregamento do jogo..')
    while check_target(btn_treasure_hunt_img) == False:
        if check_target(text_error_img) == True:
            click(btn_ok_img)
            return False
    
    print(' [*] Jogo carregado com sucesso!')
    return True

def refresh_heroes():
    ''' Update heroes' position by preventing them from jamming, exiting the map, or the user being kicked out of absence in the game '''
    global btn_back_img, btn_treasure_hunt_img
    print(' [*] Atualizando posição dos heróis..')
    click(btn_back_img)
    click(btn_treasure_hunt_img)

def clear():
    ''' Clear console '''
    system('cls')

def main():

    banner()
    await_time(10)

    intervals = yaml.safe_load(open('config.yaml', 'r'))

    last = {
        'check_wallet': 0,
        'refresh_heroes': 0,
        'send_heroes': 0
    }

    while True:
        now = time.time()        

        if now - last['check_wallet'] > intervals['check_for_login_wallet'] * 60:
            last['check_wallet'] = now
            if check_wallet() == False:
                while connect_wallet() == False:
                    print('\033[K [*] Ocorreu um erro ao tentar se conectar, tentando novamente.')
                send_heroes_go_work()
                last['send_heroes'] = now
                last['refresh_heroes'] = now

        if now - last['send_heroes'] > intervals['send_heroes_go_work'] * 60:
            last['send_heroes'] = now
            last['refresh_heroes'] = now
            send_heroes_go_work()
        
        if now - last['refresh_heroes'] > intervals['refresh_heroes_positions'] * 60:
            last['refresh_heroes'] = now
            refresh_heroes()


main()