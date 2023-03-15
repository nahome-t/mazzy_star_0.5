# mazzy_star_0.5

This program is effectively looking at 3d projections from scratch, dots in 3d objects represented as star objects are projected onto a screen which allows you to traverse the environment.
Featurse include different configuration of stars, including distributing them randomly within a sphere, torus, or a hyperbolic cone <img width="1037" alt="Screenshot 2023-01-30 at 22 37 32" src="https://user-images.githubusercontent.com/53130019/225406746-c720bb42-b00b-45cc-a9c5-66a9b720b12e.png">

Currently also features the ability to rotate the camera although done rather crudely (by effectively rotating the world around the camera which eventually leads to a drift of the points
![Screenshot 2023-01-30 at 22 40 26](https://user-images.githubusercontent.com/53130019/225407319-1b9c8dc9-5fb2-4f57-a461-022ec0695a29.png)
Furthermore the program has the ability to change the field of view of the camera,

# Improvements for the future
- Change the way which rotations are done fundementally to avoid points drifting
- Implement rotation and projection operations via numpy completely in order to improve performance, currently running quite slow once patricle number increases to over 10k
