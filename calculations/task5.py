x = int(input())

evenLessons = x // 2
oddLessons = x // 2

if x % 2 == 0:
    evenLessons -= 1

time = 45 * x + evenLessons * 15 + oddLessons * 5
print(9 + time // 60, time % 60)