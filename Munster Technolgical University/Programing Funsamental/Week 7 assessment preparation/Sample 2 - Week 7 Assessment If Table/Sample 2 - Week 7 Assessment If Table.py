# author Mofazzal Hossain
# purpose : Sample 2 - Week 7 Assessment If Table.docx
name = input("Enter your name: ").upper()
kilometer = float(input("Enter the number of km per year: "))
code = input("Enter Code ")
print(f"Name{' ' * 5} {name}")
print(f"KM per Year{' ' * 5} {kilometer:,.0f}")
if 0 <= kilometer <= 2000:
    re = "Rent"
    cost_per_km = "N/A"
    print(f"Recommendation:{' ' * 5}{re}")
    print(f"Annual Fuel Cost:{' ' * 5} {cost_per_km}Euro")
elif 2001 <= kilometer <= 10000:
    re = "Buy Petrol"
    cost_per_km = 0.16 * kilometer
    print(f"Recommendation:{' ' * 5}{re}")
    print(f"Annual Fuel Cost:{' ' * 5} {cost_per_km}Euro")
elif kilometer > 10000:
    re = "Buy Electric"
    cost_per_km = 0.04 * kilometer
    print(f"Recommendation:{' ' * 5}{re}")
    print(f"Annual Fuel Cost:{' ' * 5} {cost_per_km:,.2f}Euro")
if code == "Blue":
    print("You have won a months free petrol.")
elif code.startswith("B") and code.endswith("e"):
    print("You were close but not correct.")