import pyautogui, random, time
print("Starting in: 3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Started")
walk_keys = ["w", "s", "a", "d"]
special_keys = ["space", "strg", "shift", "y", "z", "f5", "m", "b"]
skill = ["c", "e", "q", "x"]
def slow_walk():
    random_slow = random.randint(1, 2)
    r = random.choice(walk_keys)
    pyautogui.keyDown(special_keys[random_slow])
    pyautogui.keyDown(r)
    time.sleep(random.uniform(0.75, 4))
    pyautogui.keyUp(special_keys[random_slow])
    pyautogui.keyUp(r)


def speacial_key_ping():
    random_ping = random.randint(1, 2)
    ping_times = random.randint(1, 3)
    if random_ping == 1:
        count = int(0)
        while count != ping_times:
            pyautogui.press(special_keys[4])
            count += 1
        if ping_times == 1:
            pyautogui.keyDown(special_keys[4])
            time.sleep(random.uniform(0.7, 1.5))
            pyautogui.keyUp(special_keys[4])
            count += 1
        else:
            count += 1
    else:
        pyautogui.press(special_keys[6])
        pyautogui.leftClick()
        time.sleep(random.uniform(0.5, 1))
        pyautogui.press(special_keys[6])
        pyautogui.keyDown(walk_keys[1])
        time.sleep(random.uniform(1, 2))
        pyautogui.keyUp(walk_keys[1])




def scroll():
    random_scroll = random.randint(1, 2)
    random_inspect = random.randint(1, 4)
    if random_scroll == 1:
        pyautogui.scroll(1)
        if random_inspect == 4:
            pyautogui.press(special_keys[3])
            time.sleep(random.uniform(1.5, 3))
            pyautogui.scroll(-1)
    else:
        pyautogui.scroll(1)
        pyautogui.scroll(-1)
        pyautogui.scroll(1)
        pyautogui.scroll(-1)
        pyautogui.scroll(1)
        pyautogui.scroll(-1)
        if random.randint(1, 3) == 3:
            pyautogui.leftClick()

def hopping():
    ra = random.randint(0, 5)
    count = int(0)
    if ra != 3:
        while count != ra:
            pyautogui.press(special_keys[0])
            time.sleep(random.uniform(0.3, 0.8))
            count += 1
    else:
        pyautogui.press(skill[3])
        pyautogui.leftClick()
        pyautogui.keyDown(walk_keys[0])
        time.sleep(random.uniform(1, 2))
        pyautogui.keyUp(walk_keys[0])


def skill_use():
    counter = random.randint(1, 5)
    if counter != 4 or 5:
        pyautogui.press(skill[1])
        time.sleep(random.uniform(0.6, 1))
        pyautogui.leftClick()
        time.sleep(random.uniform(0.2, 0.5))
        pyautogui.rightClick()
    else:
        if counter == 5:
            pyautogui.press(skill[2])
            time.sleep(random.uniform(0.6, 1))
            pyautogui.leftClick()
        else:
            pyautogui.press(skill[0])
            time.sleep(random.uniform(0.6, 1))
            pyautogui.leftClick()

def shoot():
    ra = random.randint(1, 3)
    if ra == 1 or 3:
        pyautogui.leftClick()
    else:
        pyautogui.rightClick()

count_end = int(0)
while True:
    end = [shoot, skill_use, hopping, scroll, speacial_key_ping, slow_walk]
    random.shuffle(end)
    for func in end:
        func()
        time.sleep(random.uniform(0.2, 1))
        count_end += 1
        if count_end >= 20:
            pyautogui.press(special_keys[5])
            pyautogui.press(special_keys[7])
            pyautogui.rightClick()
            time.sleep(random.uniform(0.5, 2))
            pyautogui.leftClick()
            pyautogui.press(special_keys[7])
            pyautogui.keyDown("tab")
            time.sleep(2)
            pyautogui.keyUp("tab")
            count_end = int(0)



