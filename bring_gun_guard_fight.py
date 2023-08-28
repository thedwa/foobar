from math import ceil, sqrt, atan2

def solution(dimensions, your_position, guard_position, distance):
    locations = reflection_map(dimensions, your_position, guard_position, distance)
    angles = set()
    shoot_count = 0
    for point in locations:
        if dist(point, your_position) <= distance:
            angle = atan2(point[1]-your_position[1], point[0]-your_position[0])
            if angle not in angles:
                angles.add(angle)
                if point[2] == 1:
                    shoot_count += 1
        else:
            break
    return shoot_count

def reflection_map(dimensions, your_position, guard_position, distance):
    locations = []
    x_repls = int(ceil((your_position[0]+distance)/float(dimensions[0])))
    y_repls = int(ceil((your_position[1]+distance)/float(dimensions[1])))
    for i in range(x_repls):
        x_add = your_position[0] if i%2==0 else dimensions[0]-your_position[0]
        xg_add = guard_position[0] if i%2==0 else dimensions[0]-guard_position[0]
        for j in range(y_repls):
            y_add = your_position[1] if j%2==0 else dimensions[1]-your_position[1]
            yg_add = guard_position[1] if j%2==0 else dimensions[1]-guard_position[1]
            fq_point = [(dimensions[0]*i) + x_add, (dimensions[1]*j) + y_add, 0]
            fqg_point = [(dimensions[0]*i) + xg_add, (dimensions[1]*j) + yg_add, 1]
            locations.extend((fq_point, fqg_point,
                [-1*fq_point[0],fq_point[1],fq_point[2]],
                [-1*fqg_point[0],fqg_point[1],fqg_point[2]],
                [fq_point[0],-1*fq_point[1],fq_point[2]],
                [fqg_point[0],-1*fqg_point[1],fqg_point[2]],
                [-1*fq_point[0],-1*fq_point[1],fq_point[2]],
                [-1*fqg_point[0],-1*fqg_point[1],fqg_point[2]]))
    del locations[0]
    locations.sort(key=lambda x: dist(x,your_position))
    return locations

def dist(l1, l2):
    return sqrt(float((l1[0]-l2[0]))**2 + (l1[1]-l2[1])**2)

