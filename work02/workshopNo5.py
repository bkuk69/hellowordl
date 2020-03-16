distance =[]
distance.append(int(input("마일수 입력:")))

distance.append(int(input("야드수 입력:")))

distance.append(int(input("피트수 입력:")))

distance.append(int(input("인치수 입력:")))

metric_distance = (63360 * distance[0] + 36 * distance[1] + 12 * distance[2] + distance[3])/39.37

kilometer = metric_distance // 1000
meter = int(metric_distance % 1000)
cmeter = (metric_distance % 1) * 100

print("미터법의 길이")
print(kilometer, "km")
print(meter, "m")
print("{0:4,.1f}".format(cmeter), "cm")

