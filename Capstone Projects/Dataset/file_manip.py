from random import randint

"""
        - read in asset list
        - select Value
        - rewrite asset list without value
        - write value to attempted list
"""


def get_one_id():
    asset_list = []
    source_file = "asset_list.csv"
    verification_file = "real_assets_used.txt"
    # Read in the whole list of available IDs
    with open(source_file, "r") as file:
        data = file.readlines()
        for item in data:
            asset_list.append(item.strip())
    id_to_get = randint(0, len(asset_list) - 2)

    # the chosen one!
    picked_id = asset_list.pop(id_to_get)

    # write back the whole list, minus the chosen ID
    with open(source_file, "w") as file:
        for asset in asset_list:
            file.writelines(f"{asset}\n")

    # make note of the picked_id so we can verify they are in the other lists
    with open(verification_file, "a") as file:
        file.write(picked_id + "\n")

    return picked_id


def subimages(x, y):
    scale = [0, 0.33, 0.67, 1]
    crop_matrix = [
        (int(scale[i] * x), int(scale[j] * y))
        for i in range(len(scale))
        for j in range(len(scale))
    ]
    cropping_point_pairs = [
        (0, 5),
        (1, 6),
        (2, 7),
        (4, 9),
        (5, 10),
        (6, 11),
        (8, 13),
        (9, 14),
        (10, 15),
    ]
    crop_coords = [
        (
            crop_matrix[p[0]][0],
            crop_matrix[p[0]][1],
            crop_matrix[p[1]][0],
            crop_matrix[p[1]][1],
        )
        for p in cropping_point_pairs
    ]
    return crop_coords
