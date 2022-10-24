vel = int(input())
time = int(input())

dist = vel * time
dist_final = (dist * 60 / 1000)

print(round(dist_final, 1))