def dot(a,b):
    '''Скалярное произведение векторов'''
    return a[0]*b[0]+a[1]*b[1]+a[2]*b[2]

def sub(A,B):
    '''функция для нахождения вектора AB по координатам точек A и B'''
    return (B[0]-A[0],B[1]-A[1],B[2]-A[2])

def cross(a, b):
    '''Функция бля нахождения векторного произведения'''
    return (a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])

def plane_from_points(A,B,C):
    u = sub(A,B)
    v = sub(A,C)
    n = cross(u,v)

    if dot(n,n) < 1e-12:
        return None
    d = -dot(n,A)
    
    return n, d

def line_from_points(A,B):
    d = sub(A,B)
    if dot(d,d) < 1e-12:
        return None
    return (A,d)
def point_on_line(A, d, t):
    return (A[0] + t*d[0], A[1] + t*d[1], A[2] + t*d[2])

def line_plane_intersection(
        n:tuple,D,
        A,d:tuple
    ):
    denom = dot(n, d)
    if abs(denom) < 1e-9:
        return None
    t = -(dot(n,A)+D)/(dot(n,d))
    P = point_on_line(A,d,t)
    return P

def decompose(w,u,v):
    n = cross(u,v)
    nn = dot(n,n)

    if nn < 1e-12:
        return None

    a = dot(cross(w,v),n)/nn
    b = dot(cross(u,w),n)/nn

    return a,b

def is_inside_polygon(P:tuple,polygon:list[tuple])->bool:
    n = len(polygon)
    for i in range(len(polygon)):
        ancor = polygon[i]
        prv = polygon[(i - 1) % n]
        nxt = polygon[(i + 1) % n]

        u = sub(ancor,prv)
        v = sub(ancor,nxt) 
        w = sub(ancor, P)

        a,b = decompose(w,u,v)
        if a < 0 or b < 0:
            return False
    return True

# n, d = plane_from_points((1,0,0), (0,2,0), (0,0,3))
# print(n, d)   # (6, 3, 2) -6