from helium import *
import time
import random


def browser_manager(url, helium):
    # helium.start_chrome(url, headless=True)
    helium.start_chrome(url)
    for i in range(3):
        helium.scroll_down(1000)
        time.sleep(random.randrange(2, 4))
    helium.kill_browser()
