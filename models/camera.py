import math
from math_functions import add
import numpy as np 
class Camera:
    def __init__(
            self,
            screen_height:float = 9,
            screen_width:float = 16,
            coord:list[float] = [0,0,0],
            rotation_angle:list[float] = [0,0,0],
            direction_vector:tuple[float] = (0,4,0)
            ):
        self.coord=coord
        self.rotation_angle = rotation_angle
        self.direction_vector = direction_vector
        self.screen_height = screen_height
        self.screen_width = screen_width

    def move(self,direction:tuple):
        self.coord[0]+=direction[0]
        self.coord[1]+=direction[1]
        self.coord[2]+=direction[2]

    def rotate(self,rotation_angle:tuple): 
        self.rotation_angle[0]+=rotation_angle[0]
        self.rotation_angle[1]+=rotation_angle[1]
        self.rotation_angle[2]+=rotation_angle[2]

    def rotate_point(
                self,
                point:tuple,
            ):
            x_angle = self.rotation_angle[0]
            y_angle = self.rotation_angle[1]
            z_angle = self.rotation_angle[2]
    
            x,y,z = point
            # lx,ly,lz = sub(self.center_coord,point)
            # поворот вокруг оси z
            new_z = z 
            new_x = x*math.cos(z_angle)-y*math.sin(z_angle)
            new_y = x*math.sin(z_angle)+y*math.cos(z_angle)
    
            x,y,z = new_x,new_y,new_z
            # поворот вокруг оси y
            new_y = y
            new_x = x*math.cos(y_angle)-z*math.sin(y_angle)
            new_z = x*math.sin(y_angle) + z*math.cos(y_angle)
    
            x,y,z = new_x,new_y,new_z
            # поворот по оси x
            new_x = x
            new_y = y*math.cos(x_angle)+z*math.sin(x_angle)
            new_z = -y*math.sin(x_angle)+z*math.cos(x_angle)
    
            return (new_x,new_y,new_z)
    
    def get_pixel_coord_matrix_np(self, H, W):
        d = self.direction_vector[1]

        # левый НИЖНИЙ угол экрана, как в твоей функции
        corner = np.array(self.rotate_point((-self.screen_width/2, d, -self.screen_height/2)))

        dx = np.array(self.rotate_point((self.screen_width/W, 0, 0)))    # шаг вправо
        dz = np.array(self.rotate_point((0, 0, self.screen_height/H)))   # шаг ВВЕРХ (плюс)

        i = np.arange(H) + 0.5   # строки: 0 - низ экрана
        j = np.arange(W) + 0.5

        return corner + i[:, None, None]*dz + j[None, :, None]*dx


    def get_pixel_coord_matrix(
        self,
        matrix_height,
        matrix_width
    ):
        screen_height =  self.screen_height
        screen_width = self.screen_width
        # Алгоритм:
        # найти угол
        # найти векторы смещения для каждого нового пикселя
        # пройтись по всем 
        #
        # 
        # Локальные координаты угла
        screen_corner_y = self.direction_vector[1]
        screen_corner_x = -screen_width/2
        screen_corner_z = -screen_height/2

        # Находим глобальные координаты угла
        world_corner_coord =  self.rotate_point(
            (screen_corner_x,
            screen_corner_y,
            screen_corner_z)
        )
        # найти векторы смещения по осям x и z

        local_x_shift_vector = ((screen_width/matrix_width),0,0)
        local_z_shift_vector = (0,0,(screen_height/matrix_height))

        world_x_shift_vector = self.rotate_point(local_x_shift_vector) 
        world_z_shift_vector = self.rotate_point(local_z_shift_vector)

        pixel_coord_matrix = [[] for i in range(matrix_height)]
        # тут нужно будет прибавлять векторы для каждого пикселя.
        curr_string_start = world_corner_coord
        curr_pixel_coord = curr_string_start
        for i in range(matrix_height):
            for j in range(matrix_width):
                pixel_coord_matrix[i].append(add(curr_pixel_coord,self.coord))
                curr_pixel_coord = add(curr_pixel_coord,world_x_shift_vector)
            curr_string_start = add(curr_string_start,world_z_shift_vector)
            curr_pixel_coord = curr_string_start
        return pixel_coord_matrix
    


    def get_pixel_coord(
        self,
        matrix_height,
        matrix_width,
        pixel_x,
        pixel_z
    ):
        
        screen_distance = self.direction_vector[1] # должна вычисляться длина вектора. Пока камера статична так.
        # screen_distance = self.direction_vector[1]-self.coord[1]
        
        screen_height =  self.screen_height
        screen_width = self.screen_width
        # считаем координаты от угла экрана
        relational_x = (screen_width/matrix_width)*pixel_x
        relational_z = (screen_height/matrix_height)*pixel_z

        screen_corner_x = -screen_width/2
        screen_corner_z = -screen_height/2

        local_x = screen_corner_x+relational_x
        local_z = screen_corner_z+relational_z
        local_y = screen_distance

        rotated_x,rotated_y,rotated_z = self.rotate_point((local_x,local_y,local_z))

        world_x = rotated_x+self.coord[0]
        world_y = rotated_y+self.coord[1]
        world_z = rotated_z+self.coord[2]

        # Тут надо научиться вычислять глобальные координаты

        return(world_x,world_y,world_z)
    
            