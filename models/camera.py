
class Camera:
    def __init__(
            self,
            screen_height:float = 9,
            screen_width:float = 16,
            coord:tuple[float] = (0,0,0),
            rotation_angle:tuple[float] = (0,0,0),
            direction_vector:tuple[float] = (0,4,0)
            ):
        self.coord=coord
        self.rotation_angle = rotation_angle
        self.direction_vector = direction_vector
        self.screen_height = screen_height
        self.screen_width = screen_width

    def get_pixel_coord(
        self,
        matrix_height,
        matrix_width,
        pixel_x,
        pixel_z
    ):
        
        screen_distance = self.direction_vector[1] # должна вычисляться длина вектора. Пока камера статична так.

        screen_height =  self.screen_height
        screen_width = self.screen_width
        # считаем координаты от угла экрана
        relational_x = (screen_width/matrix_width)*pixel_x
        relational_z = (screen_height/matrix_height)*pixel_z

        screen_corner_x = -screen_width/2
        screen_corner_z = -screen_height/2

        world_x = screen_corner_x+relational_x
        world_z = screen_corner_z+relational_z
        world_y = screen_distance

        return(world_x,world_y,world_z)
            