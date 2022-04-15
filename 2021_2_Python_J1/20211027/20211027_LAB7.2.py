Seoul = 9765
Busan = 3441
Incheon = 2954
city_pop = [ Seoul, Busan, Incheon ]
print(city_pop)

Daejeon = 1531
city_pop.append(Daejeon)

max_pop = 0
min_pop = 1000000
pop_sum = 0
n = 0

for pop in city_pop :
    if pop > max_pop :
        max_pop = pop
    if pop < min_pop :
        min_pop = pop
    pop_sum += pop
    n += 1

print('최대 인구:', max_pop)
print('최소 인구:', min_pop)
print('평균 인구:', pop_sum / n)