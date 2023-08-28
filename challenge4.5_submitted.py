from math import atan2, sqrt

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def normalize_direction(dx, dy):
    gcd_val = gcd(abs(dx), abs(dy))
    return dx // gcd_val, dy // gcd_val

def mirrored_positions_within_distance_extended(dimensions, position, target_position, distance):
    width, height = dimensions
    pos_x, pos_y = position
    mirrored_positions_self = []
    mirrored_positions_target = []

    # Calculate mirrored positions for yourself and target within the given distance
    for i in range(-(distance // width + 1), (distance // width + 2)):
        for j in range(-(distance // height + 1), (distance // height + 2)):
            x_mirror_self = (width * i) + (width - pos_x if i % 2 != 0 else pos_x)
            y_mirror_self = (height * j) + (height - pos_y if j % 2 != 0 else pos_y)
            x_mirror_target = (width * i) + (width - target_position[0] if i % 2 != 0 else target_position[0])
            y_mirror_target = (height * j) + (height - target_position[1] if j % 2 != 0 else target_position[1])

            # Distance to mirrored positions
            distance_mirror_self = sqrt((x_mirror_self - pos_x) ** 2 + (y_mirror_self - pos_y) ** 2)
            distance_mirror_target = sqrt((x_mirror_target - pos_x) ** 2 + (y_mirror_target - pos_y) ** 2)

            # Check if within range
            if distance_mirror_self <= distance:
                mirrored_positions_self.append((x_mirror_self, y_mirror_self))
            if distance_mirror_target <= distance:
                mirrored_positions_target.append((x_mirror_target, y_mirror_target))

    return mirrored_positions_self, mirrored_positions_target

def solution(dimensions, your_position, trainer_position, distance):
    # Extended Mirrored Positions within Distance
    your_mirrored_positions, trainer_mirrored_positions = mirrored_positions_within_distance_extended(
        dimensions, your_position, trainer_position, distance
    )

    # Angles, Distances, and Normalized Directions
    angles_directions = {}
    for pos in trainer_mirrored_positions:
        dx = pos[0] - your_position[0]
        dy = pos[1] - your_position[1]
        if dx == 0 and dy == 0:
            continue
        angle = atan2(dy, dx)
        distance_pos = sqrt(dx ** 2 + dy ** 2)
        direction = normalize_direction(dx, dy)
        key = (angle, direction)
        # Store only the closest mirrored target for the given angle and direction
        if key not in angles_directions or distance_pos < angles_directions[key][1]:
            angles_directions[key] = (pos, distance_pos)

    # Exclude Yourself
    for pos in your_mirrored_positions:
        dx = pos[0] - your_position[0]
        dy = pos[1] - your_position[1]
        if dx == 0 and dy == 0:
            continue
        angle = atan2(dy, dx)
        distance_pos = sqrt(dx ** 2 + dy ** 2)
        direction = normalize_direction(dx, dy)
        key = (angle, direction)
        if key in angles_directions and distance_pos < angles_directions[key][1]:
            del angles_directions[key]

    # Resulting Valid Directions
    valid_directions_count = len(angles_directions)

    return valid_directions_count
