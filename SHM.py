import matplotlib.pyplot as plt

#Time Step
dt = 0.0001
time_arr = []
full_time = 10

#Spring Constant
k1 = 1.0
k2 = 1.0
k12 = 1.0

#Damping
beta1 = 0.0
beta2 = 0.0

#P1 variables
x1 = 0.0
dx1 = 0.0
v1 = 0.0
dv1 = 0.0
a1 = 0.0
x1_arr = []

#P2 variables
x2 = 0.0
dx2 = 0.0
v2 = 0.0
dv2 = 0.0
a2 = 0.0
x2_arr = []

#Initial Values of P1
m1 = 1
x1 = 10
v1 = 0

#Initial Values of P2
m2 = 1
x2 = 0
v2 = 0

#Total Energy
TE_arr = []

#Calculate the positions
t = 0

while (t <= full_time):

    #P1
    a1 = (- (k1 + k12) * x1 + k12 * x2 - 2 * beta1 * v1) / m1
    dv1 = a1 * dt
    v1 += dv1
    dx1 = v1 * dt
    x1 += dx1

    x1_arr.append(x1)

    #P2
    a2 = (- (k2 + k12) * x2 + k12 * x1 - 2 * beta2 * v2) / m2
    dv2 = a2 * dt
    v2 += dv2
    dx2 = v2 * dt
    x2 += dx2

    x2_arr.append(x2)

    #Time increment
    time_arr.append(t)
    t += dt

plt.plot(time_arr, x1_arr)
plt.plot(time_arr, x2_arr)
plt.show()