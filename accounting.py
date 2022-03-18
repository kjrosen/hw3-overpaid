melon_cost = 1.00 ##sets the melon cost

'''list of clients, how much they bought, and what they paid
All information is already in the customer-orders.txt
Listed as <2|Andrea Cruz|12|12.00>'''
customers = open("customer-orders.txt")
##clean up the file into lists with [0] = name, [1] = number, [2] = paid
for line in customers:
    line = line.strip() #removes white space
    customer = line.split("|")#splits the line into a list

    ##splits the list further into variables for clarity
    ##make sure the number and paid are int and float respectively
    order, name, number, paid = customer
    number = int(number)
    paid = float(paid)

    ##confirms the amount we SHOULD have recieved for total order
    expected = number * melon_cost

    if expected != paid:
        print(f"{name} paid ${paid} \n\texpected ${expected}")



# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

##establishes the correct cost of the number of melons a customer bought
# customer1_expected = customer1_melons * melon_cost

# '''checks the amount paid against the amount expected
# only prints an alert if there is a disparity'''
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
