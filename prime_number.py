# FUNCTION TO PRINT PRIME NUMBERS WITHIN A RANGE
# USING FACTORIZATION

def factor_of_number(num):
    
    total_factor = 0

    for i in range(1, num + 1):
        if num % i == 0:
            total_factor = total_factor + 1

    if total_factor == 2: # IF THE NUMBER OF FACTORS IS MORE THAN TWO, THE NUMBER IS NOT PRIME - DO NOTHING
        print(num, end=' ')
    


for i in range(1,1000): # CHECK PRIME NUMBER WITHIN THE RANGE 100-150
    factor_of_number(i)