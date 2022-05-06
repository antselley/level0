def num_to_duration(input_number):
    hours = input_number // 60
    minutes = input_number % 60
    
    if hours == 1:
        hours_wording = "hour"
    else:
        hours_wording = "hours"

    if minutes == 1:
        minutes_wording = "minute"
    else: 
        minutes_wording = "minutes"
    
    print(hours, hours_wording, ",", minutes, minutes_wording)

num_to_duration(71)
num_to_duration(133)
num_to_duration(61)
num_to_duration(121)
