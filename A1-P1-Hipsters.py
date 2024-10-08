#Program 1 – Hipster's Local Vinyl Records

#Program by Alex Barr W0487099

#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
 
    #Create "Constants" for delivery rate and tax rate (perhaps there is a way I don't know of yet to create actual constants, these are just going to look like them for my purposes)
    DELIVERY_RATE = 15.00 #Identifying as float
    TAX_RATE = 14 #this is just to show the user BUT CHANGE TAX RATE HERE NOT BELOW IF YOU NEED TO CHANGE THE RATE LIKE AN EMPOYEE MIGHT (AND MAKE SURE THE NUMBER IS BETWEEN 0-99)
    TAX = float(str("1.")+str(TAX_RATE)) #1 being total price .14 being percentage above that... this doesn't really need to be stated but oh well, my biggest obstacle is commenting my code
    
    #Display the name of the shop and customer order details
    print("Hiptster's Local Vinyl Records - Customer Order Details")

    #Display delivery charge rate
    print("\nDelivery rate is ${0:.2f} per kilometer".format(DELIVERY_RATE))

    #Display Sales tax
    print("All purchases are subject to a {0}% tax rate".format(TAX_RATE))
    
    #Input the customer's first name
    print("")
    first_name = input("Enter the customer's first name: ")

    #Input the customer's last name
    last_name = input("Enter the customer's last name: ")

    #Input the distance in kilometers for the delivery
    kilometers = input("Enter the distance in Kilometers for delivery: ")
    
    #Input the cost of records purchased
    cost = float(input("Enter the cost of records purchased: ")) * TAX
    print("")

    #Display purchase summary for customer
    print("Purchase summary for {0} {1}".format(first_name, last_name))

    #Display delivery cost...but first:
        #Calculate delivery cost
    delivery_cost = float(kilometers) * DELIVERY_RATE #turned kilometers into a float just in case it wasnt although it probably doesn't matter in python
    print("Delivery Cost: ${0:.2f}".format(delivery_cost))

    #Display purchase cost
    print("Purchase Cost: ${0:.2f}".format(cost))
    #Display total cost
        #calculate total cost
    total_cost = (cost + delivery_cost) #Changed line where tax was calculated, mine originally was here, but assignment example shows tax being calculated before the delivery cost is added
    print("Total Cost   : ${0:.2f}".format(total_cost))
    
    # YOUR CODE ENDS HERE

main()