for i in range(10,0,-1):
    print(i)
n = int(input("Enter the number whose sum you want to find"))
sum = 0
for i in range (1, n+1):
 sum=sum+i
print ("\nSum =", sum)
#reversing a string
string = input("Please enter your own string")
string2= ('')
#loop for printing in reverse
for i in string:
   string2 = i + string2
print ("\nThe Original String=", string)
print ("The Reversed String=", string2)