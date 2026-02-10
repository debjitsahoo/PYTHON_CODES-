str=input("Enter String:")

str.split()

count = 0
for i in str:
    if i in ['a','e','i','o','u']:
        count +=1

print(f"Number of value in {str} are :{count}")