import Catalog

import time
import ast
import sys

'''
This method parses the catalog file generated and cached by the connect.py to check for prices. 
'''
def parse_data(amount, no_of_items, no_of_results_to_show):
    time1 = time.time()
    native_string = open('Catalog.txt', 'r').read()
    product_map = ast.literal_eval(native_string)
    all_prices = product_map.keys()
    all_possibilities = (find_combinations(all_prices, amount, no_of_items, no_of_results_to_show))
    visual_output(all_possibilities, product_map, amount)
    #print(all_possibilities)
    #print(product_map)
    time2 = time.time()
    print("Total time taken is %f second" % (time2 - time1) )
    
'''
Method that displays the output on the screen/console.
Outputs in the below format:
Amount you entered:
Combination number:
Price --> <price> Product is <actual product url>
'''
def visual_output(all_possibilities, product_map, amount):
    print("\n Amount you entered is " + str(amount) + "\n")
    for i in range(0,len(all_possibilities)):
        print("Combination number -> "+str(i + 1)+"\n")
        price_combination = all_possibilities[i].split()
        for k in range(0, len(price_combination)):
            product_url = product_map.get(int(price_combination[k]), 'Product not present')
            print("Price = " + price_combination[k] + " \t Product is " + product_url)
        print("================\n")
            
'''
Just acts as a wrapper for find_numbers function
'''
def find_combinations(all_prices, amount, no_of_items, no_of_results_to_show):
    all_possibilities = []
    all_possibilities = find_numbers(all_prices, 0, 0, amount, "", no_of_items, all_possibilities, no_of_results_to_show)
    return(all_possibilities)
    
'''
The actual code for "Subset Sum with given number of elements problem.
Typically optimized to suit the problem stated in this project.
'''
def find_numbers(list, index, current, goal, result, no_of_items, all_possibilities, no_of_results_to_show):
    if(len(all_possibilities) > no_of_results_to_show):
        return
    if(len(list) < index or current > goal):
        return
    if(len(result.split())==no_of_items):
        return
    for i in range(index, len(list)):
        if(current + list[i] == goal):
            if((len(result.split()) + 1) == no_of_items):
                #print(result + " " + str(list[i]))
                all_possibilities.append(result + " " + str(list[i]))
        elif(current + list[i] < goal):
            find_numbers(list, i+1, current + list[i], goal, result +" " + str(list[i]), no_of_items, all_possibilities, no_of_results_to_show)
    return all_possibilities
            
''' Main function.
    Takes 4 arguments:
    1. Name of the file: Display.py
    2. The amount
    3. Number of items
    4. Number of possible combinations you would like to see 
    So, the usage format is $ python Display.py <amount> <no_of_items> <no_of_combinations_to_show>
'''
def main():
    if(len(sys.argv) != 4):
        print("Usage Error: Please use the format $ python Display.py <amount> <no_of_items> <no_of_combinations_to_show>")
    amount = int(sys.argv[1])
    no_of_items = int(sys.argv[2])
    no_of_results_to_show = int(sys.argv[3]) - 1
    parse_data(amount, no_of_items, no_of_results_to_show)
    

if __name__ == "__main__":
    main()