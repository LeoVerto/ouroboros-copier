import time

import pyperclip

from key_manager import Circle, load_and_get_unjoined_circles


def generate_command(circle: Circle):
    return f"/join circle label:{circle.label} key:{circle.key}"


def paste_commands():
    unjoined = load_and_get_unjoined_circles()

    for circle in unjoined:
        cmd = generate_command(circle)
        # Uncommenting the following lines leads to The Danger Zone
        # pyperclip.copy(cmd)
        # print(".", end="", flush=True)
        # time.sleep(0.8)
        print(cmd)


time.sleep(2)
paste_commands()
