import ast

def string_to_minutes(time_frame):
    minute_frame = []
    for time_string in time_frame:
        time_split = time_string.split(':')
        time = int(time_split[0]) * 60 + int(time_split[1])

        minute_frame.append(time)

    return minute_frame

def available_schedule_algo(input):
    entire_schedule = []
    last_login = 0
    first_logout = 1500

    for i in range(len(input) - 1):
        if i % 2 == 0:
            for time_frame in input[i]:
                minute_frame = string_to_minutes(time_frame)
                entire_schedule.append(minute_frame)

        else:
            minute_frame = string_to_minutes(input[i])

            if last_login < minute_frame[0]:
                last_login = minute_frame[0]

            if first_logout > minute_frame[1]:
                first_logout = minute_frame[1]

    meeting_length = input[len(input) - 1]

    for i in range(len(entire_schedule)):
        swapped = False

        for j in range(len(entire_schedule) - i - 1):
            if entire_schedule[j][0] > entire_schedule[j+1][0]:
                entire_schedule[j], entire_schedule[j+1] = entire_schedule[j+1], entire_schedule[j]
                swapped = True

        if swapped == False: 
            break

    entire_schedule.append([first_logout, 1500])

    available_time = []
    end_of_frame = last_login
    
    for i in range(len(entire_schedule)):
        begin_of_frame = entire_schedule[i][0]

        if begin_of_frame - end_of_frame >= meeting_length:
            start_string = (str(int(end_of_frame/60))) + ":" + (str(end_of_frame%60)).zfill(2)
            end_string = (str(int(begin_of_frame/60))) + ":" + (str(begin_of_frame%60)).zfill(2)
            
            available_time.append([start_string, end_string])

        if end_of_frame < entire_schedule[i][1]:
            end_of_frame = entire_schedule[i][1]

        if end_of_frame >= first_logout:
            break

    print(available_time)
    return available_time

inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")

lines = inputFile.readlines()
inputFile.close()

problem_list = []
for line in lines:
    if line is not "\n":
        problem_list.append(ast.literal_eval(line))

    else:
        output = available_schedule_algo(problem_list)
        outputFile.write("%s\n" % output)
        outputFile.write("\n")

        problem_list = []

output = available_schedule_algo(problem_list)
outputFile.write("%s\n" % output)        

outputFile.close()