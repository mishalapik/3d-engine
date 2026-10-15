'''В этом файле описан класс, для хранения производльного 3d-объекта(3d-модели)'''
import math 
from math_functions import sub

class Object3D:
    def __init__(
            self,
            vertices:list[tuple],
            faces:list[list[tuple]],
            center_coord:tuple = (0,0,0),
            rotation_angle:list[float] = [0,0,0]
    ):
        self.vertices = vertices        # локальные координаты, список tuple(x,y,z)
        self.faces = faces              # список tuple из 4 индексов
        self.center_coord = center_coord
        self.rotation_angle = rotation_angle

    def rotate_object(self,angle_xyz:tuple):
        self.rotation_angle[0]+=angle_xyz[0]
        self.rotation_angle[1]+=angle_xyz[1]
        self.rotation_angle[2]+=angle_xyz[2]


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

    def get_world_vertices(self):
        cx,cy,cz = self.center_coord
        world = []
        for v in self.vertices:
            rx,ry,rz = self.rotate_point(v)
            world.append((cx+rx,cy+ry,cz+rz))
        return world
