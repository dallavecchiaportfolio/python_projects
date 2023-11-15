# FUNCTION TO PRINT PRIME NUMBERS WITHIN A RANGE
# USING FACTORIZATION

def factor_of_number(num):
    
    num_factors = 0

    for i in range(1, num + 1):
        if num % i == 0:
            num_factors = num_factors + 1

    if num_factors == 2:
        print(num, end=' ')
    


for i in range(1,100): # CHECK PRIME NUMBER WITHIN THE RANGE 100-150
    factor_of_number(i)