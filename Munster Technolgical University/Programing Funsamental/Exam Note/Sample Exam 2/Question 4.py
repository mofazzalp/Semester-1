# author : Mofazzal Hossain
# description : Question 3
Beginner = 10000
Advanced = 15000
Professional = 22000

Type_name = ''
Goal_step_calculation = 0
Goal_steps_in_percentage = 0

goal_steps = 0
Final_print = ''

Beginner_count = 0
Advanced_count = 0
Pro_count = 0
Classification = ''
Total_steps = 0

activity = open("statistics.txt", "a")

loop_walkers = int(input("How many walkers are there ? "))
for number in range(loop_walkers):
    walker_name = input(f"Please enter the name of walker #{number + 1} : ")
    while not walker_name[0].isupper() or len(walker_name) <= 1:
        walker_name = input(f"Please enter a name with uppercase letter and at least 1 letter #{number + 1} : ")
    type_walkers = int(input("Type of Walker (1. Beginner 2. Advanced 3. Professional): "))
    steps = -1
    while steps < 0:
        steps = int(input("No. of Steps today: "))

    if type_walkers == 1:
        Classification = ''
        Type_name = 'Beginner'
        goal_steps = Beginner
        Beginner_count += 1
        Total_steps += steps

    elif type_walkers == 2:
        Classification = ''
        Type_name = 'Advanced'
        goal_steps = Advanced
        Advanced_count += 1
    elif type_walkers == 3:
        Classification = ''
        Type_name = 'Professional'
        goal_steps = Professional
        Pro_count += 1

    if goal_steps < steps:
        Goal_step_calculation = steps - goal_steps
        Goal_steps_in_percentage = (Goal_step_calculation / steps) * 100
        print(f"{Type_name} goal of {goal_steps} steps.")
        print(f"You exceeded goal by {Goal_step_calculation:,} steps. (+ {Goal_steps_in_percentage:,.2f}%)")
        print("Well done")
        new_goal = goal_steps + goal_steps * 0.1
        print(f"Your new goal is {new_goal:,.0f} steps \n")
        Final_print += f"{number + 1}. {walker_name:6s} {Type_name:12s}  {new_goal:,.0f} * \n"
    else:
        Goal_step_calculation = goal_steps - steps
        Goal_steps_in_percentage = (Goal_step_calculation / steps) * 100
        print(f"{Type_name} goal of {goal_steps} steps.")
        print(f"You were  {Goal_step_calculation:,} steps short of your goal. (- {Goal_steps_in_percentage:,.2f}%)")
        print("Nearly there.\n")
        Final_print += f"{number + 1}. {walker_name:6s} {Type_name:12s} {goal_steps:,.0f} \n"

print("Next Week Personal Goals")
print("-" * 31)
print(Final_print)

print("Numbers per Classification", file=activity)
print("-"*26, file=activity)
Classification += f"Beginner{'':1s} {Beginner_count:>3d} \n"
Classification += f"Advanced{'':1s} {Advanced_count:>3d} \n"
Classification += f"Pro{'':6s} {Pro_count:>3d} \n"
print(Classification, file=activity)

if Beginner_count > 0:
    Beginner_Average_steps = Total_steps / Beginner_count
else:
    Beginner_Average_steps = 0
if Advanced_count > 0:
    Advanced_Average_steps = Total_steps / Advanced_count
else:
    Advanced_Average_steps = 0
if Pro_count > 0:
    Pro_Average_steps = Total_steps / Pro_count
else:
    Pro_Average_steps = 0
print(f"The average number of steps per participants {Beginner_Average_steps:,.2f} steps.")
print(f"The average number of steps per participants {Advanced_Average_steps:,.2f} steps.")
print(f"The average number of steps per participants {Pro_Average_steps:,.2f} steps.")

activity.close()
