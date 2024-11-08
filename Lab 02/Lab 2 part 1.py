height = float(input("Enter your height in cm "))
weight = float(input("Enter your weight in kg "))
age = int(input("Enter your age in years "))

BMR_Female= 66.5 + ( 13.75 * weight ) + ( 5.003 * height ) - ( 6.755 * age)
print ("Your Female BMR is ", BMR_Female)

Male_BMR = 655.1 + ( 9.563 * weight) + ( 1.850 * height ) - ( 4.676 * age )
print("Your Male 115BMR is ",Male_BMR)

#Candy bars
Candy_bars_F = BMR_Female//214
Candy_bars_M = Male_BMR//214
print("in order to maintain weight you must consume",Candy_bars_F,"candy bars as a female, or",Candy_bars_M,"as a male")
