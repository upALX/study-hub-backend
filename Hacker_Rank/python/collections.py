# Enter your code here. Read input from STDIN. Print output to STDOUT

def count_amout_shoes(shoes_values):
        
    total_amount = sum(shoes_values)
    
    return total_amount

if __name__ == '__main__': 
    shoes_values = []
    shoes_number = int(input())
    shoes_sizes = [input()]
    number_customers = int(input())
    print(shoes_sizes)
    if shoes_number <= 30 and shoes_number > 0:
        if number_customers <= 30 and number_customers > 0:
             
            for _ in range(number_customers):
                shoe_and_value = [input()]
                shoes_values.append(shoe_and_value.split()[1])
                
            list_prices_to_sum = []
            
            for item in shoes_values:
                
                if not item[1] in list_prices_to_sum:
                    list_prices_to_sum.append(int(item[1]))
            
            print(list_prices_to_sum)
            total_amount = count_amout_shoes(list_prices_to_sum)
            
            print(total_amount)
        