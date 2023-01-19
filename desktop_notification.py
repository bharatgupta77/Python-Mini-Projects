import os
import platform


def display_notification(text, title, sound):
    operating_system = platform.system()
    # Darwin -> MacOS
    if operating_system == 'Darwin':
        cmd = """osascript -e 'display notification "{}" with title "{}" sound name "{}"'""".format(
            text, title, sound)
    else:
        return

    os.system(cmd)


# Sound is taken from given mac sounds. Path of that sound is passed here.
display_notification("Developed a demo notification by using python",
                     "Notification", "default")
