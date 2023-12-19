# author : Mofazzal Hossain
# description : Question 1
Beginner = 10000
Advanced = 15000
Professional = 22000

Type_name = ''
Goal_step_calculation = 0
Goal_steps_in_percentage = 0

goal_steps = 0

walker_name = input("Enter Name : ")
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
else:
    Goal_step_calculation = goal_steps - steps
    Goal_steps_in_percentage = (Goal_step_calculation / steps) * 100
    print(f"{Type_name} goal of {goal_steps} steps.")
    print(f"You were  {Goal_step_calculation:,} steps short of your goal. (- {Goal_steps_in_percentage:,.2f}%)")
    print("Nearly there.")
