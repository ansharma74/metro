#!/usr/bin/python3
import numpy as np
import matplotlib.pylab as plot
import math as m

#initialize variables
#gravity(g), ARM_lever_length, Body_height, Body_mass
#Inc_ball_speed, Km/h_m/s, l_pitch, ball_weight

# Batting arm level move in meters
g = 9.8
ARM_lever_length = 1.52
Body_height = 1.75

# Weight in kg 
Body_mass = 90


# Km/h to m/s
Inc_ball_speed = 120
KMH_MS = 1000/3600

# Pitch length
l_pitch = 20

# cricket ball weight in kg
ball_weight = .16

# terminal and average speeds m/s
t_Ball_speed = Inc_ball_speed * KMH_MS
ave_Ball_speed = (0 + t_Ball_speed)/2
t_in_flight = l_pitch / ave_Ball_speed

ball_aclr = t_Ball_speed / t_in_flight

# Weight to force conversion (arm movement(bowling speed)* human body lever) 
# body's time/meter movement speed * lever in body weight_height (mass to force conversion)
Conversion = t_in_flight/l_pitch * ARM_lever_length/Body_height

print("Ball stats:",  t_Ball_speed, ave_Ball_speed, t_in_flight, ball_aclr, Conversion)

#F1: Force of incoming ball F=ma in newtons (kg m/s^2)
Force_inc_ball = ball_weight * ball_aclr

print("Force of incoming cricket ball:",  Force_inc_ball)

#F2: Your batting force = TF = Body mass * Force conversion factor

Batting_trq = Body_mass * Conversion 
print("Human body's reactive force on incoming cricket ball:", Batting_trq)

# Reversing the ball
Ball_inclined = Batting_trq/Force_inc_ball
print("Ball reversal factor:",  Ball_inclined)

v = t_Ball_speed * Ball_inclined

print("Ball velocity after shot:",  v)

#change angle increment theta 25 to 60 then find  t, x, y
#define x and y as arrays

theta = np.arange(m.pi/6, m.pi/3, m.pi/36)

t = np.linspace(0, 8, num=100, endpoint=True) # Set time as 'continous' parameter.

for i in theta: # Calculate trajectory for every angle
    x1 = []
    y1 = []
    for k in t:
        x = ((v*k)*np.cos(i)) # get positions at every point in time
        y = ((v*k)*np.sin(i))-((0.5*g)*(k**2))
        x1.append(x)
        y1.append(y)
    p = [i for i, j in enumerate(y1) if j < 0] # Don't fall through the floor                          
    for i in sorted(p, reverse = True):
        del x1[i]
        del y1[i]

    plot.plot(x1, y1) # Plot for every angle

plot.savefig('cricket_ball_speed_hit_length.png', dpi=600)
plot.show() # And show on one graphic
