import numpy as np
import matplotlib.pyplot as plt


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, p):
        return Vector(self.x + p.x, self.y + p.y, self.z + p.z)

    def __sub__(self, p):
        return Vector(self.x - p.x, self.y - p.y, self.z - p.z)

    def __mul__(self, a):
        return Vector(a*self.x, a*self.y, a*self.z)

    def __truediv__(self, a):
        return Vector(self.x/a, self.y/a, self.z/a)

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"

    def magnitude(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance(self, p):
        return (self - p).magnitude()

    def unit_vector(self, p):
        return (p - self)/self.distance(p)


def sample(low, high, dim, n, z=1):
    points = np.linspace(low, high, n)
    if dim == 3:
        x, y, z = np.meshgrid(points, points, points)
        shape = (1, n**3)
    elif dim == 2:
        x, y, z = np.meshgrid(points, points, z)
        shape = (1, n**2)

    x = np.reshape(x, shape)
    y = np.reshape(y, shape)
    z = np.reshape(z, shape)
    return np.vstack((x, y, z))


def calculate_field(point, charge):
    r = point - charge
    m = np.dot(r, r.T)
    return r/m**3


space_sample = 10
plate_sample = 25
space = sample(-4, 4, 3, space_sample)
plate1 = sample(-2, 2, 2, plate_sample, 0.5)
plate2 = sample(-2, 2, 2, plate_sample, -0.5)

field = np.zeros_like(space)
for i in range(space.shape[1]):
    point = space[:, i]
    point_field1 = np.array([calculate_field(point, plate1[:, j])  for j in range(plate1.shape[1])])
    point_field1 = np.sum(point_field1, axis=0)
    point_field2 = np.array([calculate_field(point, plate2[:, j]) for j in range(plate1.shape[1])])
    point_field2 = np.sum(point_field2, axis=0)
    field[:, i] = point_field1.T - point_field2.T

ax = plt.axes(projection="3d")
x, y, z = space[0, :], space[1, :], space[2, :]
u, v, w = field[0, :], field[1, :], field[2, :]
ax.scatter(plate1[0, :], plate1[1, :], plate1[2, :])
ax.scatter(plate2[0, :], plate2[1, :], plate2[2, :])
ax.quiver(x, y, z, u, v , w, length = 3e-6, color="black")
plt.show()
