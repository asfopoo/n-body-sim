import math

# constants
t = 157788000  # total time of simulation
dt = 25000  # time delta
G = 6.67E-11
t_total = 0.0

# planet  x pos         y pos      vel x        vel y       mass
earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]

# place the constants into a list
planets = [earth, mars, mercury, sun, venus]

while t_total < t:
    # for each list in the planets list
    for i in range(len(planets)):
        # skip the sun
        if i == 3:
            continue

        delta_x = planets[i][0] - planets[3][0]
        delta_y = planets[i][1] - planets[3][1]

        # calculate the radius
        # r = sqrt(delta x^2 + delta y^2)
        # since the sun is 0 the deltas are just the x and y position of the ith planet
        r = math.sqrt(math.pow(planets[i][0], 2) + math.pow(planets[i][1], 2))

        # calculate the pair-wise force between i'th planet and the sun
        # F = G * (mass of ith planet * mass of sun) / r
        F = (G * (planets[i][4] * planets[3][4])) / math.pow(r, 2)
        #################################
        # x and y components of the force
        # Fx = F * (delta x/r)
        Fx = F * (planets[i][0] / r)

        # Fy = F * (delta y/r)
        Fy = F * (planets[i][1] / r)
        #################################
        # x and y acceleration
        # Ax = Fx / mass of the planet
        Ax = Fx / planets[i][4]

        # Ay = Fy / mass of the planet
        Ay = Fy / planets[i][4]
        #################################
        # x and y components of velocity
        # Vx = Vx + Ax * dt
        planets[i][2] = planets[i][2] + Ax * dt

        # Vy = Vy + Ay * dt
        planets[i][3] = planets[i][3] + Ay * dt
        #################################
        # calculate the x and y components of the resulting position
        # Px = Px + Vx * dt
        planets[i][0] = planets[i][0] + planets[i][2] * dt

        planets[i][1] = planets[i][1] + planets[i][3] * dt

    # update the time by delta_t
    t_total += dt
# output the formatted values for the x and y components of position/velocity and mass
for i in range(len(planets)):
    pretty_list = []
    for j in range(len(planets[i])):
        pretty_list.append(f'{planets[i][j]:.4e}')
    print(pretty_list)
