from models.camera import Camera
from models.object_3d import Object3D

from math_functions import plane_from_points,line_plane_intersection,line_from_points,is_inside_polygon

def render(camera:Camera,object:Object3D,screenDim:tuple)->str:
    pixels_vertical,pixels_horizontal = screenDim

    pixels = []
    for _ in range(pixels_vertical):
        pixels.append(([' ']*pixels_horizontal))

    world_vertices = object.get_world_vertices()  
    
    for i in range(pixels_vertical):
        for j in range(pixels_horizontal):
            pixel_coord = camera.get_pixel_coord(
                matrix_height=pixels_vertical,
                matrix_width=pixels_horizontal,
                pixel_x=j,
                pixel_z=i
            )
            for f in object.faces:
                curr_face = [world_vertices[x] for x in f]
                plane = plane_from_points(curr_face[0],curr_face[1],curr_face[2])
    
                line = line_from_points((0,0,0),pixel_coord)
                intersection = line_plane_intersection(
                    n = plane[0],
                    D = plane[1],
                    A = line[0],
                    d = line[1]
                )
                if intersection is None:          # луч параллелен плоскости
                    continue
    
                inside = is_inside_polygon(intersection,curr_face)
    
                if inside:
                    pixels[i][j] = '0'
                    # Если пиксель уже закрашен дальше можно не итерироваться
                    break

    image = '\n'.join([''.join(s) for s in pixels][::-1])
    return image

