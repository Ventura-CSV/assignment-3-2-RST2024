def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """
   
    #Algorithm to find the min value
    minval = num1
    maxval = num1
    if num1 > num2:
        minval = num2
        if num2 > num3:
            minval = num3
    elif num1 > num3:
        minval = num3
    #Algorithm to find the max value
    if num1 < num2:
        maxval = num2
        if num2 < num3:
            maxval = num3
    elif num1 < num3:
        maxval = num3
        
    #Algorithm to find the median
    if num1 < num3 < num2 or num2 < num3 < num1:
        median = num3
    if num3 < num1 < num2 or num2 < num1 < num3:
        median = num1
    if num1 < num2 < num3 or num3 < num2 < num1:
        median = num2
    
    
    

    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
