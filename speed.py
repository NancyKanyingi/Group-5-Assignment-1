def check_speed(speed):
    if speed < 70:
        print("OK")
    elif speed >= 70 and speed <= 130:
        demerit_points = (speed - 70) // 5
        print(f"Demerit points: {demerit_points}")
    else:
        print(f"License Suspended")

check_speed(90)
check_speed(150)
check_speed(60)
    