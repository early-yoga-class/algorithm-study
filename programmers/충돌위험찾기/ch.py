from collections import defaultdict
def solution(points, routes):
    answer = 0
    robot_routes = defaultdict(set)
    
    # row 같을때까지 이동하면서 (x, y, time)으로 넘어가기
    for x, route in enumerate(routes):
        curX, curY = points[route[0] - 1]
        time = 0
        robot_routes[(curX, curY, time)].add(x)
        # 다음 목적지까지의 거리중 row값부터 양, 음수로 올라갈지 내려갈지 판단하여 이동.
        for i in range(1, len(route)):
            nextX, nextY = points[route[i] - 1]

            if curX != nextX:
                step = 1 if nextX > curX else -1
                for row in range(curX + step, nextX + step, step):
                    curX = row
                    time += 1
                    robot_routes[(curX, curY, time)].add(x)

            if curY != nextY:
                step = 1 if nextY > curY else -1
                for col in range(curY + step, nextY + step, step):
                    curY = col
                    time += 1
                    robot_routes[(curX, curY, time)].add(x)
        
    for key, robots in robot_routes.items():
        if len(robots) > 1:
            answer += 1

    return answer