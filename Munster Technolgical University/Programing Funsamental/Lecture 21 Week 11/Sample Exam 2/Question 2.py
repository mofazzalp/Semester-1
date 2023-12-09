# author : Mofazzal
# description : Question 2
Beginner = 10000
Advanced = 15000
Professional = 22000

Type_name = ''
Goal_step_calculation = 0
Goal_steps_in_percentage = 0

goal_steps = 0
Final_print = ''

loop_walkers = int(input("How many walkers are there ? "))
for number in range(loop_walkers):

    walker_name = input(f"Please enter the name of walker #{number+1} : ")
    type_walkers = int(input("Type of Walker (1. Beginner 2. Advanced 3. Professional): "))
    steps = int(input("No. of Steps today: "))

    if type_walkers == 1:
        Type_name = 'Beginner'
        goal_steps = Beginner
    elif type_walkers == 2:
        Type_name = 'Advanced'
        goal_steps = Advanced
    elif type_walkers == 3:
        Type_name = 'Professional'
        goal_steps = Professional
    if goal_steps < steps:
        Goal_step_calculation = steps - goal_steps
        Goal_steps_in_percentage = (Goal_step_calculation / steps) * 100
        print(f"{Type_name} goal of {goal_steps} steps.")
        print(f"You exceeded goal by {Goal_step_calculation:,} steps. (+ {Goal_steps_in_percentage:,.2f}%)")
        print("Well done")
        new_goal = goal_steps + goal_steps*0.1
        print(f"Your new goal is {new_goal:,.0f} steps \n")
        Final_print += f"{number + 1} {walker_name:6s} {Type_name:12s}  {new_goal:,.0f} * \n"
    else:
        Goal_step_calculation = goal_steps - steps
        Goal_steps_in_percentage = (Goal_step_calculation / steps) * 100
        print(f"{Type_name} goal of {goal_steps} steps.")
        print(f"You were  {Goal_step_calculation:,} steps short of your goal. (- {Goal_steps_in_percentage:,.2f}%)")
        print("Nearly there.\n")
        Final_print += f"{number + 1} {walker_name:6s} {Type_name:12s} {goal_steps:,.0f} \n"


print("Next Week Personal Goals")
print("-"*31)
print(Final_print)
