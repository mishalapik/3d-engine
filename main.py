
import os
from core import render
from object_storage import cube,polygonObject,pyramid,prism
from models.camera import Camera
from keyboard_reader import get_keys
import time

# Выбор модели. Доступные: cube,polygonObject,pyramid,prism
curr_object = cube

# Задаем вращение за один кадр по осям x,y,z
rotation_per_frame = (0.1,0.1,0)

camera = Camera(
    direction_vector=(0,7,0),
    coord=[0,0,0]
    )
MOVE_STEP = 0.5
TURN_STEP = 0.1

curr_seconds = int(time.time())
fps = 0
while True:
    if int(time.time()) == curr_seconds:
        fps+=1
    else:
        fps = 0
        curr_seconds+=1
    for key in get_keys():
        if   key == 'w': camera.move(( 0,  MOVE_STEP, 0))   # вперёд (Y это глубина)
        elif key == 's': camera.move(( 0, -MOVE_STEP, 0))
        elif key == 'a': camera.move((MOVE_STEP, 0, 0))
        elif key == 'd': camera.move((- MOVE_STEP, 0, 0))
        elif key == 'left':  camera.rotate(( 0, 0, TURN_STEP))   # поворот влево-вправо
        elif key == 'right': camera.rotate(( 0, 0, -TURN_STEP))
        elif key == 'up':    camera.rotate(( TURN_STEP, 0, 0))    # наклон вверх-вниз
        elif key == 'down':  camera.rotate((-TURN_STEP, 0, 0))

    # получаем разрешение экрана
    size = os.get_terminal_size()
    pixels_vertical = size.lines
    pixels_horizontal = size.columns
    
    # применяем вращение|+перемещение 
    curr_object.rotate_object(rotation_per_frame)

    # рендерим
    image = render(camera=camera,object=curr_object,screenDim=(pixels_vertical,pixels_horizontal))

    # os.system("cls")

    print(image)
    print("FPS: ",fps) # Внести в функцию рендеринга позже
    # camera.rotation_angle[0]+=0.05
    # camera.coord[0]-=0.04
    