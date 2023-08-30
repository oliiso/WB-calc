print("Hello, welcome to the Weight and Balance calculator for a Cessna 172.")
print("You will need to gather the following in lbs: \n(a) basic empty weight \n(b) moment \n(c) front passenger weight \n(d) rear passenger weight \n(e) baggage area weight \n(f) fuel amount")

def int_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error, please enter only integers.")

BEW = int_input("Basic empty weight: ")
moment = int_input("Moment: ")
FP = int_input("Sum of front passengers: ")
RP = int_input("Sum of rear passengers: ")
Bag = int_input("Baggage area: ")
fuel = int_input("Fuel amount (gallons): ")

fuel_weight = 6 * fuel
FP_moment = 37 * FP
RP_moment = 73 * RP
Bag_moment = 95 * Bag
fuel_weight_moment = 47.8 * fuel_weight 

total_weight = BEW + FP + RP + Bag + fuel_weight

total_moment = moment + FP_moment + RP_moment + Bag_moment + fuel_weight_moment

cg = total_moment / total_weight

print("\nWeight and Balance Calculation:")
print(f"Your total weight is: {total_weight}")
print(f"Total Moment: {total_moment} lb-in")
print(f"Center of Gravity (CG): {cg:.2f} inches from the reference point")