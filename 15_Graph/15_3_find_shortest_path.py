#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from collections import deque

# 지하철역 클래스
class Station:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

    # self의 neighbors에 another_station을 담고,
    # another_station의 neighbors에 self를 담는다.
    def add_connection(self, another_station):
        if another_station not in self.neighbors:
            self.neighbors.append(another_station)

        if self not in another_station.neighbors:
            another_station.neighbors.append(self)

# Breadth-First Search 알고리즘
def bfs(start, goal):
    previous = dict()
    queue = deque()
    current = None
    footprint = list()

    previous[start] = None
    queue.append(start)
    footprint.append(start)

    while goal not in footprint and queue:
        current = queue.popleft()
        footprint.append(current)
        print("current name : {}".format(current.name))
        for neighbor in current.neighbors:
            if neighbor not in footprint:
                footprint.append(neighbor)
                print(" neighbor name : {}".format(neighbor.name))
                queue.append(neighbor)
                previous[neighbor] = current

    if goal in footprint:
        path = list()
        path.append(goal)
        key = goal
        while key != start:
            path.append(previous[key])
            next_key = previous[key]
            key = next_key
        return path

    return None

# 파일 읽기
stations = dict()
in_file = open('stations.txt', 'r')

# 파일의 데이터를 정리하여 각 역에 해당하는 Station 인스턴스를 만들고,
# add_connection 메소드로 이웃 역들을 연결시킨다.
#
# 후에 각 역을 쉽게 찾아서 쓸 수 있도록 stations 사전의 
# key로 역 이름을 넣고, value로 해당 Station 인스턴스를 넣는다.
for line in in_file:    
    words = line.strip().split(" - ")
    for index in range(len(words)):
        if words[index] not in stations:
            stations[words[index]] = Station(words[index])
            
    for index in range(len(words)-1):
        stations[words[index]].add_connection(stations[words[index + 1]])

in_file.close()


# # 테스트
start_name = "잠실"
goal_name = "등촌"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)

if path == None:
    print("경로를 찾을 수 없습니다")
else:
    for station in path:
        print("{0}".format(station.name))