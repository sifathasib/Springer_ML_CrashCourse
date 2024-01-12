

def calculate_mean(list):
    
    a = len(list)
    sum =0 
    for l in list:
        sum += l
    result = sum/a
    
    print("The mean calculated form the first function: ",result)
    
list_numbers= [1,78.90,4,56,71,6,8,12]
calculate_mean(list_numbers)


