def ShortestPath(strArr):
    street_num = int(strArr[0])
    streets = strArr[1:street_num+1]
    paths = strArr[street_num+1:]
    possible_paths = {}
    start = streets[0]
    finish = streets[-1]

    for street in streets:
        connections = []
        for path in paths:
            if street in path:
                street1, street2 = tuple(path.split('-'))
                
                if street == street1:
                    connections.append(street2)
                    possible_paths[street] = connections

                else:
                    connections.append(street1)
                    possible_paths[street] = connections

    all_roads = [start]
    road = start
    for x in all_roads:
        for next_street in possible_paths[x[-1]]:
            road = x + next_street
            if road.count(next_street) > 1:
                continue
            
            all_roads.append(road)
            
            if next_street == finish:
                return '-'.join(road)

    return -1
