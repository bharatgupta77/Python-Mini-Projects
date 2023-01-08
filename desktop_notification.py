import os
import platform


def display_notification(text, title, sound):
    operating_system = platform.system()

    if operating_system == 'Darwin':
        cmd = """osascript -e 'display notification "{}" with title "{}"'""".format(
            text, title)
    else:
        return

    os.system(cmd)
    os.system(sound)


# Sound is taken from given mac sounds. Path of that sound is passed here.
display_notification("Developed a demo notification by using python",
                     "Notification", "afplay /System/Library/Sounds/blow.aiff")
