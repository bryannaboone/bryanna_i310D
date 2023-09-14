def calculate_volume_of_sphere(radius):
    pi = 3.14

    volume = 4*pi*(radius**3)/3

    return volume



radius1 = 30

volume1 = calculate_volume_of_sphere(radius1)


print("The volume of sphere with", radius1, "is:", volume1)

radius2 = 40

volume2 = calculate_volume_of_sphere(radius2)

print("The volume of sphere with", radius2, "is:", volume2)
