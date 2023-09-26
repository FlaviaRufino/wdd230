from math import pi

def main():

    name = "#1 Picnic"
    radius = 6.83
    height = 10.16
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    storage_efficiency = compute_storage_efficiency(volume, surface_area)
    print(f"{name} {storage_efficiency:.1f}")

def compute_storage_efficiency(volume, surface_area):
    return volume / surface_area

def compute_volume(radius, height):
    return pi * radius **2 * height
def compute_surface_area(radius, height):
    return 2 * pi * radius * (radius + height)

main()
