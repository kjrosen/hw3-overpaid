from isort import file

def check_paid(customer_orders,melon_cost):
    '''takes a file of customer orders and the current cost of melons
    and prints a list of price discrepancies'''
    customers = open(customer_orders) #open the file and attach it to a variable

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

        ##if the amount paid is different than the amount owed print an error
        if expected != paid:
            print(f"{name} paid ${paid}. Expected ${expected}")

    customers.close()# close file when done

##customer orders is a list of orders arranged like <2|Andrea Cruz|12|12.00>
##second argument is the current cost of mellons
check_paid("customer-orders.txt", 1.00)