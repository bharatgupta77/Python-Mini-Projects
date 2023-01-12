import pyscreenshot as p


try :
    # capture screenshot
    screenshot = p.grab()

    # display screenshot
    screenshot.show()

    # Save screenshot
    screenshot.save("miscellaneous_files/screenshot.png")

    print("Screenshot is taken and save. please check.")

except Exception as e:
    print(e)

