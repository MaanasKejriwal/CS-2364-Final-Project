import numpy as np
from numba import jit
from PIL import Image

# Fractal and rendering parameters
POWER = 8
MAX_ITER = 100
ESCAPE_RADIUS = 2
DELTA = 0.001
WIDTH, HEIGHT = 400, 300
FOV = np.pi / 4
ASPECT_RATIO = WIDTH / HEIGHT
CAMERA_DISTANCE = 3.0
FRAMES = 30

@jit(nopython=True)
def mandelbulb_distance(p, power=8, max_iterations=100, bailout=2.0):
    z = np.copy(p)
    dr = 1.0
    r = 0.0
    for i in range(max_iterations):
        r = np.linalg.norm(z)
        if r > bailout:
            break
        theta = np.arctan2(np.hypot(z[0], z[1]), z[2])
        phi = np.arctan2(z[1], z[0])
        zr = r**power
        dr = (power * zr / r) * dr + 1.0
        theta *= power
        phi *= power
        z = zr * np.array([np.sin(theta) * np.cos(phi), np.sin(theta) * np.sin(phi), np.cos(theta)]) + p
    return 0.5 * np.log(r) * r / dr, i

@jit(nopython=True)
def ray_march(origin, direction, max_dist=20, max_steps=200, eps=0.001):
    dist_traveled = 0.0
    for i in range(max_steps):
        p = origin + dist_traveled * direction
        dist, iterations = mandelbulb_distance(p)
        if dist < eps:
            return dist_traveled, p, iterations
        dist_traveled += dist
        if dist_traveled >= max_dist:
            return None, None, None
    return None, None, None

@jit(nopython=True)
def get_normal(p, delta=0.001):
    # Approximate the gradient (normal) at p
    grad = np.array([
        mandelbulb_distance(p + np.array([delta, 0, 0]))[0] - mandelbulb_distance(p - np.array([delta, 0, 0]))[0],
        mandelbulb_distance(p + np.array([0, delta, 0]))[0] - mandelbulb_distance(p - np.array([0, delta, 0]))[0],
        mandelbulb_distance(p + np.array([0, 0, delta]))[0] - mandelbulb_distance(p - np.array([0, 0, delta]))[0]
    ])
    return grad / np.linalg.norm(grad)

def normalize(v):
    return v / np.linalg.norm(v)

def simple_lighting(normal, light_dir, light_color=np.array([255, 200, 150])):
    # Lambertian reflectance model for diffuse lighting
    light_intensity = max(np.dot(normal, light_dir), 0)
    return (light_color * light_intensity).astype(int)

def render_frame(angle, filename):
    image = Image.new('RGB', (WIDTH, HEIGHT))
    camera_pos = np.array([CAMERA_DISTANCE * np.sin(angle), 0, CAMERA_DISTANCE * np.cos(angle)])
    look_at = np.array([0, 0, 0])
    up = np.array([0, 1, 0])
    forward = look_at - camera_pos
    right = np.cross(up, forward)
    up = np.cross(forward, right)
    forward = forward / np.linalg.norm(forward)
    right = right / np.linalg.norm(right)
    up = up / np.linalg.norm(up)
    light_dir = normalize(np.array([1, 1, -1]))  # Example light direction

    for y in range(HEIGHT):
        for x in range(WIDTH):
            u = (x / WIDTH - 0.5) * 2 * np.tan(FOV / 2) * ASPECT_RATIO
            v = (y / HEIGHT - 0.5) * 2 * np.tan(FOV / 2)
            direction = normalize(forward + u * right + v * up)
            dist, hit_point, _ = ray_march(camera_pos, direction)
            if hit_point is not None:
                normal = get_normal(hit_point)
                color = simple_lighting(normal, light_dir)
                image.putpixel((x, y), tuple(color))

    image.save(filename)

def create_animation():
    for i in range(FRAMES):
        angle = 2 * np.pi * i / FRAMES
        filename = f'animation3/frame_{i:03}.png'
        render_frame(angle, filename)
        print(f'Rendered frame {i+1}/{FRAMES}')

create_animation()
