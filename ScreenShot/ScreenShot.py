import pyscreenshot

image = pyscreenshot.grab()
image2 = pyscreenshot.grab(bbox=(10,10, 500,500))

image.show()
image2.show()

image.save("ScreenShotpy.png")
image.save("ScreenShot2.png")