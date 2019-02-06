step = 0
tired = 0
badweather = 0
while step < 10000:
    print((step))
    if tired == True:
        break
    elif badweather == True:
        break
    else:
        step = step + 1


for x in range(0, 100):
    print('ya age is ' + str(x))
    if x >= 25:
        break
