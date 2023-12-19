MATH_MIN = 65
PHY_MIN = 55
CHEM_MIN = 50
TOTAL_MIN = 190
MATH_PHY_TOTAL_MIN = 140

math = int(input("Enter your maths grade: "))
physics = int(input("Enter your physics grade: "))
chemistry = int(input("Enter your chemistry grade: "))

if math >= MATH_MIN and physics >= PHY_MIN and chemistry >= CHEM_MIN:
    if (math + physics + chemistry) >= TOTAL_MIN or (math + physics) >= MATH_PHY_TOTAL_MIN:
        print("You have qualified for this course.")
    else:
        print("Your individual grades were enough, but the total wasn't high enough")
else:
    print("One of your individual grades was not high enough")