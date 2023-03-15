# mazzy_star_0.5

This program is effectively looking at 3d projections from scratch, dots in 3d objects represented as star objects are projected onto a screen which allows you to traverse the environment. Features include different configuration of stars, including distributing them randomly within a sphere, torus, or a hyperbolic cone.

Currently also features the ability to rotate the camera although done rather crudely (by effectively rotating the world around the camera which eventually leads to a drift of the points. Furthermore the program has the ability to change the field of view of the camera.

<img width="400" alt="Screenshot 2023-01-30 at 22 37 32" src="https://user-images.githubusercontent.com/53130019/225406746-c720bb42-b00b-45cc-a9c5-66a9b720b12e.png">



<img width="400" alt="Screenshot 2023-01-30 at 22 39 49" src="https://user-images.githubusercontent.com/53130019/225408901-61e61e6b-807d-4ec4-9a27-eeafd8a7f698.png">
amera,

# Improvements for the future
- Change the way which rotations are done fundementally to avoid points drifting
- Implement rotation and projection operations via numpy completely in order to improve performance, currently running quite slow once patricle number increases to over 10k
