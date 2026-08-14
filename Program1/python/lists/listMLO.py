probabilities=[]

while True:
    try:
        prob=float(input("Enter the Probabilities: "))
        if(prob <0 or prob >1):
            raise ValueError
            
        probabilities.append(prob)
        

    except ValueError:
        print("please enter a valid value for probability")
    except EOFError:
        break  

n = len(probabilities)
if(n==0):
    print("No Probabilities entered")
    exit()


print(f"Model Prediction Probabilities: {probabilities}")




print(f"The lowest predicted Probability: {min(probabilities)} \n The Highest probability predicted: {max(probabilities)}")

avg_prob=sum(probabilities) / n
print(f"Average Probalities of the Model = {avg_prob:.2f}" )


new_list = [prob for prob in probabilities if prob>=0.80]

print("Probabilities .=0.80:",new_list)

new_list.sort(reverse=True)

print("Sorted:",new_list)


#find min max and sum without using 
total = 0.0 # some of elements
count=0 # total size of the list
for prob in probabilities:
    total+=prob
    count+=1 

if(count==0):
    exit()
average_probability = total / count

print(f"Average Probability: {average_probability:.2f}")

max_probability=0.0 
for prob in probabilities:
    if prob > max_probability:
        max_probability=prob

print("Highest Probability: ",max_probability)

min_probability=1.0 # to calculate min we consider the highest probability

for prob in probabilities:
    if prob <min_probability:
        min_probability=prob

print("Lowest Probability: ",min_probability)

