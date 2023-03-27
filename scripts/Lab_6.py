from PIL import Image, ImageFilter

photo = Image.open('gerald_lilia.jpg')

zatenenie = ImageFilter.Kernel((3, 3), [-1, -1, -1,-1, 9, -1, -1, -1, -1], scale=9, offset=5) # Делает небольшое размытие с затенением, повышает резкость
kontyr = ImageFilter.Kernel((3, 3), [-1, 0, 0, 0, 1, 0, 0, 0, 0], scale=9, offset=2) # Выводит черный контур фотографии

photo_filtered1 = photo.filter(zatenenie)
photo_filtered2 = photo.filter(kontyr)

photo_filtered1.show()
photo_filtered2.show()