def print_formatted(number):
    # your code goes here
    for i in range(number):
        print(str(i+1).rjust(2), format(i+1, 'o').rjust(4),format(i+1,'X').rjust(4),format(i+1,'b').rjust(7),
              sep=" ")
        
if __name__ == '__main__':
    n = int(input("Ingresa el numero a analizar: "))
    print_formatted(n)

"""
If you want to get a correct answer with the correct spaces between numbers, just change rjust(10) by rjust(2)

1. Create a function in order to add the number to analize
2. Inside this function, we have to create a for in range(number), until the number. Consider that this range covers since i=0 until i=number-1, So we have to add +1 in the operation later
3. create a print where we put 4 variables, the first one is in decimal, the second one is in octal, the third one is in Upper Hexa, and the last one is in Binary. All of these are separated by a space sep=" "
4. The function format(), converts an element, for example if we want to transform a number in another system like octal, we have tu add "o". rjust() is used to adjust the position to the right, and the number 10 indicates the spaces.
"""