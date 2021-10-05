def oil(n, distance):
    i = 0
    count = 0
    for one in distance:
        count += one
        if count > n:
            print('%dkm start fuel filling' % (one))
            count = one
            i += 1
    return i


n = 300
dis = [150, 180, 120, 100, 280, 160, 50, 60, 20, 140, 130]  # dis<300
num = oil(n, dis)
print('the minimum filling times:%d' % (num))
