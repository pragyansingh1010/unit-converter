def hours_to_minutes(hours):
    return hours * 60

def minutes_to_hours(minutes):
    return minutes / 60

assert hours_to_minutes(1) == 60
assert hours_to_minutes(2.5) == 150
assert minutes_to_hours(60) == 1
assert minutes_to_hours(90) == 1.5
print('Time conversion rules passed')
