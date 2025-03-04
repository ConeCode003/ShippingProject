# Setting the weight of the package
weight = 4.8

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <=6:
  cost_ground = weight * 3.0 + 20
elif weight <=10:
  cost_ground = weight * 4.0 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Ground Shipping $", cost_ground)

#Ground Shipping Premium
cost_ground_premium = 125.00
print("Ground Shipping premium $",cost_ground_premium)

#Drone Shipping
if weight <= 2:
  cost_ground = weight * 4.50
elif weight <=6:
  cost_ground = weight * 9.00
elif weight <=10:
  cost_ground = weight * 12.00
else:
  cost_ground = weight * 14.25 + 20

print("Drone Shipping: $",cost_ground)