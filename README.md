# 3D Fractal Visualisation using Ray Marching



Methodology:

1. Fractal Distance Estimation
mandelbulb_distance is a function that simulates the behavior of a point in a fractal space defined by the Mandelbulb equation. It iteratively transforms a point based on the fractal's rules and checks if the point escapes to a "safe" distance (defined by bailout). The function returns a distance estimate that informs the ray marching algorithm about how safely it can proceed along the ray towards the viewer, optimizing rendering by skipping over empty space

2. Ray Marching:
For every pixel in the image, a ray is computed from the camera position through the pixel's location in the image plane. The ray's direction is calculated based on the pixel's coordinates relative to the center of the image, adjusted for the camera's orientation and the field of view (FOV).

a. The loop iterates over each pixel, calculating the direction vector (direction) for the ray that passes through the pixel.
b. ray_march function is called with this direction and the camera position. It returns whether the ray hits the fractal and, if so, the point of contact (hit_point).
c. If a hit is detected, the surface normal at that point is computed using get_normal.
d. Lighting is calculated based on this normal and a predefined light direction, using simple_lighting.
e. The pixel's color is set based on the lighting calculation.

3. Normalisation
a. get_normal: Computes the surface normal at a point p on the fractal, used for lighting calculations.
b. normalize: Normalizes a vector v, making it unit length. This is  necessary for proper geometric calculations, ensuring directions are consistent regardless of original vector length.

4. Simple Lighting
   a. simple_lighting: Computes simple lighting based on a light direction, a normal at a surface, and a light color. It simulates how light might reflect off the fractal surface to give visual depth and realism.

5. Advanced Lighting
a. Ambient Light:
Ambient lighting is a simple model used to simulate indirect light in a scene that is scattered and comes from no specific direction. It ensures that no areas of the scene are completely black, simulating the effect of light bouncing off other surfaces in the environment.
In the function, ambient is computed as a fraction of the light color, making it a constant color added to every point, regardless of its orientation relative to light sources.
b. Diffuse Lighting:
Diffuse lighting simulates the direct illumination received from a light source. It depends on the angle of the light hitting the surface, which is calculated using the dot product between the surface normal and the light direction.
This implementation mirrors the simpler model but is explicitly scaled by a diffuse factor and can be adjusted for intensity through this parameter.
c. Specular Reflection:
Specular reflections represent the bright highlights that appear on shiny surfaces when viewed from specific angles. It is calculated based on the angle between the viewer's direction and the direction of the reflected light ray.
The specular component uses the reflection of the light direction off the surface normal, and the intensity of the specular highlight is controlled by the shininess parameter, which affects how sharp or broad the highlight appears. A higher shininess value results in a smaller, more focused highlight.

6. Final Rendering
a. Initializing the Image Canvas: Image.new('RGB', (WIDTH, HEIGHT))
b. Setting Camera and Viewing Geometry: camera_pos,look_at, up, forward, right, and up vectors
c. Calculating Ray Directions for Each Pixel:
d. Ray Marching to Determine Surface Interaction:
ray_march(camera_pos, direction)
e. Surface Normal Calculation and Lighting:
get_normal(hit_point)
simple_lighting(normal, light_dir)
f. Setting the Pixel Color:
image.putpixel((x, y), tuple(color))
g. Saving the Image:
image.save(filename)



