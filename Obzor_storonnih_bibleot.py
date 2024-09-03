from PIL import Image, ImageOps
import os

# Открываем изображение и задаем размер для изменения
image_path = os.path.abspath('339975-svetik.jpg')
sample = Image.open(image_path)
size = (100, 150)

# Изменяем изображения с помощью различных режимов
with Image.open(r'C:\PytonUrbanzadanie1\Project_11_module\339975-svetik.jpg') as im:
    # Сохраняем изображение с режимом contain
    ImageOps.contain(im, size).save(r'C:\PytonUrbanzadanie1\Project_11_module\1.jpeg')
    # Сохраняем изображение с режимом cover
    ImageOps.cover(im, size).save(r'C:\PytonUrbanzadanie1\Project_11_module\2.png')
    # Сохраняем изображение с режимом fit
    ImageOps.fit(im, size).save(r'C:\PytonUrbanzadanie1\Project_11_module\3.jpg')
    # Сохраняем изображение с режимом pad, цвет заливки - красный
    ImageOps.pad(im, size, color="#f00").save(r'C:\PytonUrbanzadanie1\Project_11_module\4.jpeg')


# Функция для сдвига изображения
def roll(sample, delta):
    # Сдвигает изображение влево или вправо на заданное количество пикселей.

    xsize, ysize = sample.size
    delta = delta % xsize  # Ограничиваем сдвиг размером изображения

    part1 = sample.crop((0, 0, delta, ysize))  # Вырезаем часть изображения слева
    part2 = sample.crop((delta, 0, xsize, ysize))  # Вырезаем часть изображения справа

    # Вставляем части изображения, чтобы создать сдвиг
    sample.paste(part1, (xsize - delta, 0, xsize, ysize))
    sample.paste(part2, (0, 0, xsize - delta, ysize))
    return sample


# Пробуем сдвинуть исходное изображение

sample = roll(sample, 1500)  # Сдвиг на 1500 пикселей влево
print(sample.size)
sample.save("modified_image3.jpg")
sample.show()
