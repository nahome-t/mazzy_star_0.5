import math
import numpy as np
import random


# Generates different distributions of stars
class Generators:
    draw_radius = None

    def cone_generator(a=20, width=400):
        x = draw_radius / 2
        y = random.randint(-width / 2, width / 2)
        y*=4*abs(y)/width
        # r_norm = width/5*math.cos(10*y/width)**2
        r_norm = y*(random.random())
        r_norm = math.sqrt(r_norm*r_norm+a*a)
        ang = 2 * math.pi * random.random()
        x += r_norm * math.cos(ang)
        z = r_norm * math.sin(ang)
        return np.array([x, y, z])




    def sphere_generator(r=100, scale1=40):
        theta_interval = 100
        phi_interval = 200
        phi = random.randint(0, phi_interval)/phi_interval*2*math.pi
        # phi = random.random()*math.pi*2
        theta_space = np.linspace(0, math.pi, theta_interval)
        p_space = np.array([math.sin(val) for val in theta_space])
        p_space[0] = 1/theta_interval
        p_space[-1] = 1/theta_interval
        p_space /= np.sum(p_space)
        theta = float(np.random.choice(theta_space, 1, p=p_space))
        ef1 = r*math.sin(theta)
        res = np.array([ef1*math.cos(phi)+scale1, ef1*math.sin(phi), r*math.cos(
            theta)])
        # print(theta)
        return res

    def torus_generator(r_big=100, r_small=60):
        phi_interval = 150
        phi = random.randint(0, phi_interval) / phi_interval * 2 * math.pi
        theta_interval = 90
        theta = random.randint(0, theta_interval) / theta_interval * 2 * math.pi

        circle_big = np.array([math.cos(phi), math.sin(phi), 0])*(r_big
                                                                  +r_small*math.cos(theta))


        circle_small = np.array([0, 0, r_small*math.sin(theta)])
        circle = circle_small+circle_big
        return circle

    def gaussian_clust_generator(radius=100):
        return np.random.normal(0, radius, 3)

    def tunnel_generator(r=30, l=500):
        theta_interval = 50
        x = random.randint(0, l)
        theta = random.randint(0, theta_interval)/theta_interval*2*math.pi + x/100
        y, z = r*math.cos(theta), r*math.sin(theta)
        r = r*x/l
        return np.array([x, y, z])