# Setting the weight of the package
weight = 4.8

#Ground Shipping is dependent on the weight of the package and flat charge
if weight <= 2:
  cost_ground = weight * 1.5 + 20 # weight*num1 + num2, weight*num1 - price per pound , num2 - flat charge
elif weight <=6:
  cost_ground = weight * 3.0 + 20
elif weight <=10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $",cost_ground)

#Ground Shipping Premium is flat charge
cost_ground_premium = 125.00

print("Ground Shipping premium $",cost_ground_premium)

#Drone Shipping is dependent on the weight of the package and flat charge,

if weight <= 2:
  cost_drone = weight * 4.50 # weight*num1 + num2,  where weight*num1 is price per pound , num2 - flat charge
elif weight <=6:
  cost_drone = weight * 9.00
elif weight <=10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25 + 20

print("Drone Shipping: $",cost_drone)
