# Auto RDP
import time,os
from autokey import *
import pyautogui

col_cmd = "!wget -q -O - bit.ly/cpu02 | bash"
listfile = '/home/one/g167'
gpass = "********"
new = True
global_slow_motion = 2

speed = 200

##################### Functions ###################################


def exec_key():
    # keyboard.send_keys("<ctrl>+<enter>")
    pyautogui.keyDown('ctrlright')
    pyautogui.press('enter')
    pyautogui.keyUp('ctrlright')

def exit_key():
    # keyboard.send_keys("<ctrl>+<enter>")
    pyautogui.keyDown('ctrlright')
    pyautogui.press('w')
    pyautogui.keyUp('ctrlright')

def chrome_next():
    pyautogui.keyDown('ctrlright')
    pyautogui.press('tab')
    pyautogui.keyUp('ctrlright')


def select_all_key():
    pyautogui.keyDown('ctrlright')
    pyautogui.press('a')
    pyautogui.keyUp('ctrlright')

def save_key():
    pyautogui.keyDown('ctrlright')
    pyautogui.press('a')
    pyautogui.keyUp('ctrlright')

def human_click(x_pos=1200, y_pos=400, slow_motion=1):
    time.sleep(0.1*slow_motion)
    pyautogui.moveTo(x_pos+4, y_pos+4)
    time.sleep(0.1*slow_motion)
    pyautogui.moveTo(x_pos+3, y_pos+3)
    time.sleep(0.1*slow_motion)
    pyautogui.moveTo(x_pos+2, y_pos+2)
    time.sleep(0.1*slow_motion)
    pyautogui.moveTo(x_pos+1, y_pos+1)
    time.sleep(0.1*slow_motion)
    pyautogui.mouseDown(x_pos, y_pos, 'left')
    pyautogui.mouseUp(x_pos, y_pos, 'left')


def human_clear(numch=100, slow_motion=1):
    pyautogui.press('backspace', presses=numch)
    pyautogui.press('delete', presses=numch)
    # for x in range(numch):
    #    time.sleep(0.01)
    #    pyautogui.keyDown('delete')
    #    pyautogui.keyUp('delete')


def human_clear_all():
    time.sleep(0.1)
    # keyboard.send_keys("<ctrl>+a")
    select_all_key()
    time.sleep(0.1)
    pyautogui.keyDown('backspace')
    pyautogui.keyUp('backspace')


def colab_top(x_top=1594, y_top=250, slow_motion=1):
    time.sleep(0.1*slow_motion)
    pyautogui.mouseDown(x_top, y_top, 'left')
    pyautogui.mouseUp(x_top, y_top, 'left')
    time.sleep(0.1*slow_motion)

# normal 1480
# private 1340


def chrome_new_container2(slow_motion=1):
    pyautogui.hotkey('ctrl', 'shift', 'k')


def chrome_new_container(x_ok=1340, y_ok=80, slow_motion=1):
    time.sleep(0.1*slow_motion)
    pyautogui.click(x_ok, y_ok)
    time.sleep(2*slow_motion)


def chrome_new_url(x_ok=800, y_ok=80, slow_motion=1, c_url='https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com'):
    time.sleep(0.1*slow_motion)
    pyautogui.click(x_ok, y_ok)
    time.sleep(0.2*slow_motion)
    human_clear_all()
    # keyboard.send_keys(c_url)
    pyautogui.write(c_url)
    time.sleep(0.1*slow_motion)
    # keyboard.send_keys("<enter>")
    pyautogui.press('enter')
    time.sleep(30*slow_motion)


def chrome_gcon(x_ok=780, y_ok=580, y_pass=620, slow_motion=1, g_id="testcolab10001", g_pass="********"):
    time.sleep(0.1*slow_motion)
    human_click(x_ok, y_ok)
    time.sleep(0.2*slow_motion)
    human_clear_all()
    time.sleep(0.2*slow_motion)
    pyautogui.write(g_id)
    time.sleep(0.1*slow_motion)
    pyautogui.press('enter')
    human_click(x_ok, y_pass)
    time.sleep(0.2*slow_motion)
    time.sleep(5*slow_motion)
    human_clear_all()
    pyautogui.write(g_pass)
    time.sleep(0.1*slow_motion)
    pyautogui.press('enter')
    time.sleep(10*slow_motion)


def colab_doexec2(slow_motion=1):
    time.sleep(0.1*slow_motion)
    exec_key()
    time.sleep(20*slow_motion)
    exec_key()
    time.sleep(1*slow_motion)
    time.sleep(20*slow_motion)
    exec_key()
    time.sleep(1*slow_motion)


def colab_clear_logs(x=80, y=280, slow_motion=1):
    time.sleep(0.1*slow_motion)
    human_click(80, 280)
    time.sleep(1*slow_motion)


def colab_clear_cmd2(x_clear_cmd=1000, y_clear_cmd=240, new_cmd='!wget -q -O - bit.ly/CPU01 | bash', slow_motion=1):
    time.sleep(1*slow_motion)
    colab_top()
    time.sleep(1*slow_motion)
    human_click(x_clear_cmd, y_clear_cmd)
    time.sleep(1*slow_motion)
    colab_top()
    pyautogui.click(x_clear_cmd, y_clear_cmd)
    time.sleep(1*slow_motion)
    human_clear()
    time.sleep(0.5*slow_motion)
    pyautogui.write(new_cmd, interval=0.11)
    time.sleep(1*slow_motion)


def chrome_enable_gpu(x_edit=128, y_edit=148, x_parm=156, y_param=484, slow_motion=1):
    time.sleep(0.1*slow_motion)
    pyautogui.click(x_edit, y_edit)
    time.sleep(0.3*slow_motion)
    pyautogui.click(x_parm, y_param)
    time.sleep(0.5*slow_motion)
    pyautogui.press('tab', presses=3, interval=0.25)
    time.sleep(0.2*slow_motion)
    pyautogui.press('down')
    time.sleep(0.1*slow_motion)
    pyautogui.press('tab', presses=5, interval=0.25)
    pyautogui.press('enter')
    time.sleep(0.1*slow_motion)


def old_chrome_enable_gpu(x_edit=128, y_edit=148, x_parm=156, y_param=484, slow_motion=1):
    time.sleep(0.1*slow_motion)
    pyautogui.click(x_edit, y_edit)
    time.sleep(0.3*slow_motion)
    pyautogui.click(x_parm, y_param)
    time.sleep(0.5*slow_motion)
    keyboard.send_keys("<tab>")
    time.sleep(0.2*slow_motion)
    keyboard.send_keys("<tab>")
    time.sleep(0.1*slow_motion)
    keyboard.send_keys("<tab>")
    time.sleep(0.2*slow_motion)
    keyboard.send_keys("<down>")
    time.sleep(0.1*slow_motion)
    keyboard.send_keys("<tab>")
    time.sleep(0.1*slow_motion)
    keyboard.send_keys("<tab>")
    time.sleep(0.1*slow_motion)
    keyboard.send_keys("<tab>")
    time.sleep(0.1*slow_motion)
    keyboard.send_keys("<tab>")
    time.sleep(0.1*slow_motion)
    keyboard.send_keys("<tab>")
    time.sleep(0.1*slow_motion)
    keyboard.send_keys("<enter>")
    time.sleep(0.1*slow_motion)


def chrome_new_colab(g_id="testcolab10001", g_pass="********", slow_motion=1):
    time.sleep(1*slow_motion)
    chrome_new_container2()
    chrome_new_url(
        c_url='https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com')
    chrome_gcon(g_id=g_id, g_pass=g_pass)
    chrome_new_url(c_url='https://colab.research.google.com/#create=true')
    colab_clear_cmd2(new_cmd='!wget -q -O - bit.ly/cpu02 | bash')
    time.sleep(3*slow_motion)
    chrome_enable_gpu()
    colab_doexec2()


def chrome_refresh_page(x_quit=959, y_quit=210, slow_motion=1):
    pyautogui.mouseDown(1000, 500, 'left')
    pyautogui.mouseUp(1000, 500, 'left')
    time.sleep(0.25*slow_motion)
    pyautogui.keyDown('f5')
    pyautogui.keyUp('f5')
    time.sleep(1.5*slow_motion)
    time.sleep(0.1*slow_motion)
    exec_key()
    #pyautogui.mouseDown(x_quit, y_quit, 'left')
    #pyautogui.mouseUp(x_quit, y_quit, 'left')


def chrome_colab_refresh(slow_motion=1):
    time.sleep(1*slow_motion)
    chrome_refresh_page()
    colab_doexec2()
    colab_clear_logs()
    time.sleep(3*slow_motion)
    colab_doexec2()


def chrome_colab_refresh_full(slow_motion=1):
    time.sleep(1*slow_motion)
    chrome_refresh_page()
    colab_clear_cmd2(new_cmd='!wget -q -O - bit.ly/cpu02 | bash')
    colab_clear_logs()
    colab_doexec2()
    time.sleep(3*slow_motion)
    colab_doexec2()

def chrome_colab_refresh_save(slow_motion=1):
    time.sleep(1*slow_motion)
    save_key()
    time.sleep(40)
    chrome_refresh_page()
    colab_doexec2()
    colab_clear_logs()

def chrome_colab_refresh_fast(slow_motion=1):
    time.sleep(1*slow_motion)
    colab_doexec2()
    colab_clear_logs()
    
def get_speed():
    # Getting all memory using os.popen()
    speed = 100
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])
    ram_usage=round((used_memory/total_memory) * 100, 2)
    if(ram_usage > 90 ):
        speed = speed - 90
    elif ram_usage > 70 :
        speed = speed - 20
    else:
        speed = 110
    return speed    

###############################################################
############################# Main ############################
###############################################################
pyautogui.FAILSAFE = False
winTitle = window.get_active_title()
winClass = window.get_active_class()
mouse.wait_for_click(1)
time.sleep(1)

#size_x = window.get_property(property_name, 0, 0, 255)
#size_y = window.get_property(property_name, 0, 0, 255)
debug = 0

# openfiles
# Using readlines()
file1 = open(listfile, 'r')
Lines = file1.readlines()

count = 0
if new == True:
    # Strips the newline character
    for line in Lines:
        count += 1
        #print("Line{}: {}".format(count, line.strip()))
        gid = line.strip('\n')
        gid = gid.strip('\r')
        chrome_new_colab(gid, gpass)

# refresh
while (debug == 0):
    debug = 0
    speed = get_speed()
    time.sleep(2*global_slow_motion)
    winTitle = window.get_active_title()
    winClass = window.get_active_class()
    if (winClass == "google-chrome.Google-chrome"):
        if winTitle.find("olab") != -1:
            if speed < 25 :
                chrome_colab_refresh()
            else:
                chrome_colab_refresh_fast()
            if debug != 0:
                # dialog.info_dialog("winTitle",winTitle)
                chrome_new_colab("soudi10001", "*******")
            chrome_next()
        elif winTitle.find("Cloud Shell") != -1:
            gshell_reconnect()
            ### next page ###
            if debug != 0:
                dialog.info_dialog("winTitle", winTitle)
            chrome_next()
        else:
            time.sleep(5)
            if debug != 0:
                dialog.info_dialog("winTitle", winTitle)
            # colab_full_refresh()
            exit_key()
            chrome_next()
    else:
        time.sleep(5)
