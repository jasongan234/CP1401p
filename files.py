#Question 1

out_file = open("name.txt", 'w')
name= str(input("Enter name:"))
print(name, file= out_file)
out_file.close()

#Question 2
open_file= open("name.txt", 'r')
name= open_file.read().strip()
print("Your name is ",name)

#Question 3

read_file= open("numbers.txt", 'r')
number1= int(read_file.readline())
number2= int(read_file.readline())
read_file.close()
print(number1+number2)

#Question 4

read_file= open("numbers.txt", 'r')
sum=0
for line in read_file:
    number= int(line)
    sum= sum+number
read_file.close()
print(sum)






