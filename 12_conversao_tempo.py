time_seconds = int(input())

hours = time_seconds/60/60
minutes = (hours - int(hours))*60
seconds = (minutes - int(minutes))*60

print(f"{int(hours)}:{int(minutes)}:{int(seconds)}")

