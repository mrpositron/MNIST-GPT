import numpy as np
import itertools

def distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def k_farthest_apart(coordinates, k):
    n = len(coordinates)
    farthest_coords = []
    max_distance = 0

    for pair in itertools.combinations(coordinates, 2):
        d = distance(pair[0], pair[1])
        if d > max_distance:
            max_distance = d
            farthest_coords = list(pair)

    # If k is greater than 1, find remaining k-1 coordinates
    for _ in range(k - 1):
        max_distance = 0
        next_coord = None

        for coord in coordinates:
            d = min(distance(coord, fc) for fc in farthest_coords)
            if d > max_distance:
                max_distance = d
                next_coord = coord

        farthest_coords.append(next_coord)

    return farthest_coords

def get_data(data):
    img, val = data
    img = (img*256).numpy().astype(np.uint8).reshape(28, 28)

    # coordinates where the value is not zero
    coords = np.column_stack(np.where(img > 0))


    # sort by x and y
    coords = coords[np.lexsort((coords[:, 1], coords[:, 0]))]
    # sample k coordinates that are most far apart
    k = min(10, len(coords) - 1)
    coords = k_farthest_apart(coords, k)

    coords_str = ''.join([f'({x},{y});' for x, y in coords])
    return img, val, coords, coords_str