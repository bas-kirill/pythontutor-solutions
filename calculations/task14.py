alpha = float(input())

secondsNumber = alpha * 120

hours = int(secondsNumber // 3600)
minutes = int(secondsNumber // 60 % 60)
seconds = int(secondsNumber % 60)
print(hours, minutes, seconds)