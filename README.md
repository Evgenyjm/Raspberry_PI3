# Raspberry_Pi

# GUI_ekran
Графический интерфейс реализовано с помощью библиотеки python tkinter.
Данной интерфейс сделан как четыре вкладки, которые отвечают за свою переферию,
в связи с тем, что он разрабатывался исключительно под небольшой экран (3.2 дюйма). 
Используя библиотеку tkinter, что не имеет возможности проскролить экран.
В проекте используется: лампочка, сервопривод, шаговый двигатель, Picamera.


# controlCam
В проекте используется веб-фреймворк Python под названием Flask для того,
чтобы превратить Raspberry Pi в динамический веб-сервер. 
Flask позволяет взять ваши существующие программы Python и добавить шаблон HTML,
чтобы предоставить конечному пользователю интерфейс веб-страницы.
Для поворота камеры вверх / вниз был взят сервопривод.
Для поворота камеры влево / вправо взят шаговый двигатель.
Драйвером для двигателя использован ULN2003.
В программе  применяется JavaScript. Главная задача его состоит в том, 
чтобы при нажатии на кнопки управления веб страница не перезагружалась.
Вся разметка страницы веб-страницы написана на HTML. Стили прописаны на СSS.
Стили, скрипты, и сама разметка находится в файле index.html.