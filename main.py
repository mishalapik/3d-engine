
import os
from core import render
from object_storage import cube,polygonObject,pyramid,prism
from models.camera import Camera

# Выбор модели. Доступные: cube,polygonObject,pyramid,prism
curr_object = cube

# Задаем вращение за один кадр по осям x,y,z
rotation_per_frame = (0,0.1,0.1)

camera = Camera()

while True:
    # получаем разрешение экрана
    size = os.get_terminal_size()
    pixels_vertical = size.lines
    pixels_horizontal = size.columns
    
    # применяем вращение|+перемещение 
    curr_object.rotate_object(rotation_per_frame)

    # рендерим
    image = render(camera=camera,object=curr_object,screenDim=(pixels_vertical,pixels_horizontal))

    print(image)
    