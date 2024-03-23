# Project Proposals
Below, I have described two project ideas that I would like to be considered for my final project for this course. The first is an unconventional idea, and second conventional.


# Option 1: Generative Art: Fractal Generation and Visualisation with Parameter Tuning

My first idea is a fractal generator, and visualiser. I will be generating fractals such as the Mandelbrot set, the Julia Set, Fractal trees, the Markus-Lyapunov Fractal, Buddhabrot, "random walk" etc. I will be generating these with random or set dimensions, and I am planning on letting the user play around with sliders to make various adjustments to paramaeters that will influence the output 3d generated fractal. These parameters include size, iterations, colours etc. I am also planning on adding a "randomise" button which the user can click to see a randomly generated fractal by picking random variables.

Since this is just a proposal, I would also want to share my backup idea if in case I am unable to generate a 3d model of these fractals, due to any unforseen hurdles. If this happens, I should still be able to generate images of these fractals and also possibly animations of these fractals being generated. 

For visualisation, I plan to use a combination of plotly and matplotlib depending on what generates better looking models. I will also be researching other packages. For the UI sliders I plan to use Streamlit.

A few examples of what I am talking about are attached below:

Mandelbrot Set:
![Let's draw the Mandelbrot set! – The Mindful Programmer](https://jonisalonen.com/wp-content/uploads/mandelbrot1.png)

Julia set:
![An example of a fractal known as the Julia set [47] for a given... |  Download Scientific Diagram](https://www.researchgate.net/publication/326965061/figure/fig1/AS:658393085784064@1533984552077/An-example-of-a-fractal-known-as-the-Julia-set-47-for-a-given-constant-offset-c.png)

Fractal tree:
![turtle graphics - Drawing a fractal tree in Python, not sure how to proceed  - Stack Overflow](https://i.stack.imgur.com/dgkgO.png)

Markus-Lyapunov Fractal:
![How does the Lyapunov fractile work? - Quora](https://qph.cf2.quoracdn.net/main-qimg-be031b80fc9a5e92474bbc8767aac760-pjlq)

# Option 2: CycleGAN to transfer artistic style of a painter to images

This project is a competition on Kaggle, where one has to use a dataset supplied by them of images of Monet's art, to convert other images to Monet's artistic style using CycleGANs. 

This uses the CycleGAN architecture to transfer distinct characteristic of Monet's images (any such category of images can be used) and uses these characteristics translating them to another set of images. 

I will be using data from Kaggle for the Artist images. Since this has been done with Monet already as a competition, I aim to, if feasible, do this project with another artist (perhaps Van Gogh). If I am able to find a good dataset that collects a variety of input images to transform into Van Gogh's style I will use the same, else I will use the images from this competition especially if I do not go with Monet.

The official challenge requires generation of 7000-10,000 Monet-style images, I will be aiming to generate fewer images in Van Gogh's style. I also plan on writing a report on the analysis of these newly generated images. I will mostly be using a jupyter notebook/google colab file as opposed to streamlit as discussed in the previous proposal (option 1).

![Make-A-Monet: Image Style Transfer With Cycle GANs | by DataRes at UCLA |  Medium](https://miro.medium.com/v2/resize:fit:1400/0*vEJOv0dMLr5Wv3Bg)

