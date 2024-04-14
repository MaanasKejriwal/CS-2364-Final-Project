import numpy as np
import streamlit as st
import plotly.graph_objects as go

def julia_quadratic(zx, zy, cx, cy, threshold):
    """Calculates whether the number z[0] = zx + i*zy with a constant c = x + i*y
    belongs to the Julia set. In order to belong, the sequence 
    z[i + 1] = z[i]**2 + c, must not diverge after 'threshold' number of steps.
    The sequence diverges if the absolute value of z[i+1] is greater than 4.
    
    :param float zx: the x component of z[0]
    :param float zy: the y component of z[0]
    :param float cx: the x component of the constant c
    :param float cy: the y component of the constant c
    :param int threshold: the number of iterations to considered it converged
    """
    # initial conditions
    z = complex(zx, zy)
    c = complex(cx, cy)
    
    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.:  # it diverged
            return i
        
    return threshold - 1  # it didn't diverge

# def mandelbrot(cx, cy, threshold):
#     """Calculates whether the number c = cx + i*cy belongs to the Mandelbrot set.
#     :param float cx: the x component of the constant c
#     :param float cy: the y component of the constant c
#     :param int threshold: the number of iterations to considered it converged
#     """
#     c = complex(cx, cy)
#     z = 0
#     for i in range(threshold):
#         z = z**2 + c
#         if abs(z) > 2:  # it diverged
#             return i
#     return threshold - 1  # it didn't diverge

# Create initial parameters
x_start, y_start = -2, -2
width, height = 4, 4
density_per_unit = 200
threshold = 20
frames = 100

# Function to compute Julia set
def compute_julia(r, a, threshold):
    re = np.linspace(x_start, x_start + width, width * density_per_unit )
    im = np.linspace(y_start, y_start + height, height * density_per_unit)
    cx, cy = r * np.cos(a), r * np.sin(a)
    julia_set = np.empty((len(re), len(im)))
    for i in range(len(re)):
        for j in range(len(im)):
            julia_set[i, j] = julia_quadratic(re[i], im[j], cx, cy, threshold)
    return julia_set

# Function to compute Mandelbrot set
# def compute_mandelbrot(threshold):
#     re = np.linspace(x_start, x_start + width, width * density_per_unit )
#     im = np.linspace(y_start, y_start + height, height * density_per_unit)
#     mandelbrot_set = np.empty((len(re), len(im)))
#     for i in range(len(re)):
#         for j in range(len(im)):
#             mandelbrot_set[i, j] = mandelbrot(re[i], im[j], threshold)
#     return mandelbrot_set

# Streamlit app
st.title('Fractal Visualization')

# Add sliders for parameters
r_julia = st.slider('r (Julia)', min_value=0.0, max_value=1.0, value=0.7885, step=0.01)
a_julia = st.slider('a (Julia)', min_value=0.0, max_value=2*np.pi, value=0.0, step=0.01)
threshold_julia = st.slider('Threshold (Julia)', min_value=1, max_value=100, value=20, step=1)

# threshold_mandelbrot = st.slider('Threshold (Mandelbrot)', min_value=1, max_value=100, value=20, step=1)

# Create Plotly figures
julia_set = compute_julia(r_julia, a_julia, threshold_julia)
# mandelbrot_set = compute_mandelbrot(threshold_mandelbrot)

fig_julia = go.Figure(data=[go.Surface(z=julia_set.T, contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))])
fig_julia.update_layout(title='Julia Set Visualization', scene=dict(
                    xaxis_title='Real',
                    yaxis_title='Imaginary',
                    zaxis_title='Iterations'))

# fig_mandelbrot = go.Figure(data=[go.Surface(z=mandelbrot_set.T, contours_z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project_z=True))])
# fig_mandelbrot.update_layout(title='Mandelbrot Set Visualization', scene=dict(
#                     xaxis_title='Real',
#                     yaxis_title='Imaginary',
#                     zaxis_title='Iterations'))

# Display plots
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig_julia)

# with col2:
#     st.plotly_chart(fig_mandelbrot)

import itertools as itt
import pyfracgen as pf
from matplotlib import pyplot as plt
from matplotlib import colormaps
from pathlib import Path

# Generate and display GIF
reals = itt.chain(np.linspace(-1, 2, 60)[0:-1],  np.linspace(2, 3, 40))
series = pf.julia(
    (complex(real, 0.75) for real in reals),
    xbound=(-1, 1),
    ybound=(-0.75, 1.25),
    update_func=pf.funcs.magnetic_2,
    maxiter=300,
    width=5,
    height=4,
    dpi=200,
)
# gif_path = "/Users/maanas/Desktop/Ashoka/Sem 6/Computer Graphics and Computational Imaging/Final Project/Saved Images/julia_animation_ex.gif"
# pf.images.save_animation(
#     list(series),
#     cmap=colormaps["ocean"],
#     gamma=0.6,
#     file=Path(gif_path)
# )

# Display generated GIF
st.markdown("## Julia Set GIF:")
st.image(gif_path)