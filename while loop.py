#Input the value of terms
n = int(input("Enter the value of terms: "))


sum = 0 #initialise
i = 1 #initialise
while i<=n: #loop will run from 1 to n
    sum = sum+i
    i = i+1
    
print("\nSum =",sum)    

#Activity 2 - infinate loop
#i = 0
#while i<=0:
    #print("I will run forever")
    
#Activity 3 - Armstrong numbers  
#Take input from the user
num = int(input("Enter a number: "))

#initialize sum
sum = 0

#find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
    
# display the result 
if num == sum:
    print(num,"is an Armstrong number")
    
else: 
    print( num," is not an Armstrong number")       
    
#Activity 4 - extra activity

fruits = ["Watermelon","Mango","Lichi","Orange"]

j = 0
while j <= 3: 
    print(fruits[j])      
    j = j+1
 
