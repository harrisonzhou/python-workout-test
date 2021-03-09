def run_timing():
    number_run_of=0
    total_time=0

    while True:
        one_run=input('Enter 10KM run time :')

        if not one_run:
            break
        number_run_of+=1
        total_time+=float(one_run)
   
    average_time=total_time/number_run_of
    print(f'Average of {average_time},over {number_run_of} runs')

run_timing()