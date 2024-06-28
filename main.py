def main():
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    """
    ########################################
    Code Your Program here
    ########################################
    """
   
    #Algorithm to find the max value
    maxval = num1
    if num1 < num2:
        maxval = num2
        if num2 < num3:
            maxval = num3
        else:
            maxval = num2
        if num1 > num3:
            minval = num3
    else:
        minval = num2
        if num2 > num3:
            minval = num3
    if num1 < num3:
        maxval = num3
        
        
    
    
        

    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
