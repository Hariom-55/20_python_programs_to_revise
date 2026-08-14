#part1: Customer registration and storing the data with proper validation

customer_records = [] #a list which will consist all customers data
while True:
    
    try:
        number_of_customers = int(input( "Enter the number of customers") )

        if number_of_customers > 0 :
            break
        else :
            print("Number of customer cannot be negative or zero")
            continue
            
    except ValueError :
        print("Enter a valid Integeral Value")
        continue

for customer in range(number_of_customers) :
    
    customer_name = input("Enter the Customer Name: ")
    customer_name = " ".join(customer_name.strip().title().split())

    while True : 
        
        customer_email = input("Enter the Customer Email: ")
        customer_email = customer_email.lower() 
    
        if customer_email.count("@") != 1 or customer_email[0]=="@" or customer_email.count(" ") > 0 or "." not in customer_email :
            print("You have a entered an invalid input for Email ID")
            continue 
        else:
            break 
         
    while True :
        
        try:
            purchase_amount = float(input("Enter the purchase amount"))
            if purchase_amount > 0:
                break 
            else : 
                print("Enter a Valid Amount")
                continue

        except ValueError :
            print("You have enter Invalid type for amount")
            continue 

    customer_ID = f"CUS{customer + 1:03d}"

    customer_records.append([customer_ID , customer_name , customer_email , purchase_amount]) 

    

#finding duplicate email and reporting the duplicate customer records
duplicate_email = []

for i in range(len(customer_records)) :
    for j in range(i + 1 , len(customer_records)) :
        if customer_records[i][2] == customer_records[j][2] :
            if customer_records[i][2] not in duplicate_email :
                duplicate_email.append(customer_records[i][2])
            break 


total_customers = len(customer_records)
total_revenue = 0
highest_purchase_amount = customer_records[0][3] 
lowest_purchase_amount = customer_records[0][3] 


for i in range(total_customers):
    total_revenue += customer_records[i][3]
    if customer_records[i][3] > highest_purchase_amount :
        highest_purchase_amount = customer_records[i][3]

    if customer_records[i][3] < lowest_purchase_amount :
        lowest_purchase_amount = customer_records[i][3] 


average_purchase_amount = total_revenue / total_customers 

#customer purchase Classification 

platinum_customer_list = [] #purchase amount >=10,000
gold_customer_list = [] #purchase amount >=5,000
silver_customer_list = [] #purchase amount >=2,500
bronze_customer_list = [] #purchase amount <2,500 


for i in range(total_customers) :
    if customer_records[i][3] >= 10000 :
        platinum_customer_list.append(customer_records[i])
        
    elif customer_records[i][3] >= 5000 : 
        gold_customer_list.append(customer_records[i])

    elif customer_records[i][3] >= 2500 : 
        silver_customer_list.append(customer_records[i])

    else :
        bronze_customer_list.append(customer_records[i])


#implementing Search Operation 

search_by_name = input("Enter the name of the customer to search: ")
name_to_search = " ".join(search_by_name.strip().title().split()) 
found = False 

for customer in customer_records :
    if customer[1] == name_to_search :
        
        print(f"""
        Customer Details
        Customer_ID = {customer[0]}
        Customer_Name = {customer[1]}
        Customer_Email = {customer[2]}
        Purchase_Amount = {customer[3]}
        """) 

        found = True 


if not found :
    print("customer not found")
    


#Ranking the customers on the basis of purchase amount 

ranked_customers = customer_records.copy() 

for i in range (len(ranked_customers)):
    for j in range (i+1 , len(ranked_customers) ):
        if ranked_customers[i][3] < ranked_customers[j][3] :
            temp = ranked_customers[i] 
            ranked_customers[i] = ranked_customers[j]
            ranked_customers[j] = temp



# Creating the Customer Analytical Report

print("================ CUSTOMER ANALYTICAL REPORT =====================")
print("Total Customer: ", total_customers)
print("Total Revenue: ", total_revenue)
print("Highest Purchase: " , highest_purchase_amount)
print("Lowest Purchase: " , lowest_purchase_amount)
print("Average Purchase: " , average_purchase_amount) 

print()

print("================ DUPLICATE EMAILS =====================")

if len(duplicate_email) > 0 :
    for email in duplicate_email :
        print(f"Duplicate Email : {email}")
else :
    print("No Duplicate Customers Found")

print()

print("================ PURCHASE CATEGORIES =====================")

print(f"PLATINUM CATEGORIES: {len(platinum_customer_list)}")
print(platinum_customer_list)
print(f"GOLD CATEGORIES: {len(gold_customer_list)}")
print(gold_customer_list)
print(f"SILVER CATEGORIES: {len(silver_customer_list)}")
print(silver_customer_list)
print(f"BRONZE CATEGORIES: {len(bronze_customer_list)}")
print(bronze_customer_list)


print()

print("================ CUSTOMER RANKING =====================")

for rank , customer in enumerate(ranked_customers, start=1):
    print(f"""
    Rank {rank}
    Customer ID : {customer[0]}
    Customer Name : {customer[1]}
    Purchase Amount : {customer[3]}
    """)


