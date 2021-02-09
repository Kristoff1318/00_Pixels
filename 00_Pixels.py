import math

image = open("image.ppm", 'w')
image.write("P3 500 500 255\n")

for i in range(500):
    for j in range(500):
        if (math.cos(i)**2 > 0.5 and math.cos(j)**2 < 0.5):
            r = 255
            g = 0
            b = 0
        else:
            r = 222
            g = 222
            b = 222
        image.write(f'{r} {g} {b} ')
    image.write('\n')
