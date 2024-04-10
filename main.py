#1)create a string and demonstrate the following

#capitalize
txt = "I Am Batman"
x= txt.capitalize()
print(x)
# casefold
txt = "I Am Batman"
x = txt.casefold()
print(x)
# center
txt = "ironman"
x = txt.center(10)
print(x)
# count()
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
#endswith()
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
# encode()
txt = "My name is adhi"
x = txt.encode()
print(x)
# expandtabs
txt = "h\tu\tl\tk"
x =  txt.expandtabs(2)
print(x)
# find()
txt = "Hello, welcome to my world."
x = txt.find("to")
print(x)
#index
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
# format
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 40))
# format_map()
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
# isalnum()
txt = "yeahhh"
x = txt.isalnum()
print(x)
# isalpha()
txt = "noooo"
x = txt.isalpha()
print(x)
# isdecimal()
x="bhbh"
s=x.isdecimal()
print("Is decimal:", s)
#isdigit()
x="100"
s=x.isdigit()
print("isdigit:",s)
#isidentifier()
x="developer"
w=x.isidentifier()
print(w)
#islower and isnumeric
x="avengers infinity war"
print(x.islower())
print(x.isnumeric())
#isprintable and isspace
x="ADHI"
print(x.isprintable())
print(x.isspace())
#istitle and isupper
x="ASHA"
print(x.istitle())
print(x.isupper())
#join
x="ADHI"
print(x.join("THYAN"))
#lower
x="Adhi"
print(x.lower())
#partition
x="ADITHYAN SATHEESH"
print(x.partition("S"))
#replace
x="Adhi satheesh"
print(x.replace("Adhi","Aaaadi",1))
#split
x="adithyan satheesh"
print(x.split("s"))
#swapcase
x="TALESOFADHI"
print(x.swapcase())
#title
x="TALESOFADHI"
print(x.title())
#upper
x="TALESOFADHI"
print(x.upper())

#2)Create a list and demonstrate the following

x = [1 , 2, 3, "A"]
x.append(6)
print(x)
x.clear()
print(x)
x = [1,2,3,"A"]
x.count(2)
print(x)
e = x.copy()
print(e)
x.extend([8])
print(x)
print(x.index(2))
x.insert(2, 'B')
print(x)
print(x.pop())
print(x)
x.remove('B')
print(x)
x.reverse()
print(x)
x = [1,2,3]
h = x.sort(reverse = True)
print(h)

#create a tuple
tuple = (1,2,4,3)
print(tuple.count(2))
print(tuple.index(3))


#create a dictionary
Dict={"art":"music", "guitar":"violin", 10: "lyrics"}
print(Dict.values())
print(Dict.keys())
Dict.clear()
print(Dict)
Dict={"art":"music", "guitar":"violin", 10: "lyrics"}
Dict1=Dict.copy()
print(Dict1)
Dict.pop("art")
print(Dict)
Dict1.popitem()
print(Dict1)
print(Dict.get(10))
print(Dict.setdefault(10,9))
print(Dict.setdefault(11,9))

#operators
#1)Arithmetic operators

print(2+2) #addition
print(5-3) #subtraction
print(5*2) #multiplication
print(10/2) #divison
print(15//2) #floor division
print(10%4) # modulus
print(2**3)  # Exponentiation

# Assignment operators
x= 10
x += 5
print(x)
x = 10
x -= 5
print(x)
x = 25
x *= 10
print(x)
x = 5
x /= 2
print(x)
x = 10
x //= 3
print(x)
x = 7
x %= 2
print(x)

# Comparison operators
print(2 == 1)
print(5 != 10)
print(5 > 2)
print(5 < 4)
print(5 >= 5)
print(5 <= 3)

# Logical operators
print(True and False)
print(True or False)
print(not True)

# Identity operators
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)
print(x is not y)

# Membership operators
print(1 in x)
print(4 not in x)

# Bitwise operators
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)
print(5 << 2)
print(5 >> 2)


# Get the name & nationality of the user from the followin

nat = input("Please enter your nationality ").lower()
name = input("please enter your name ")
if nat == 'india':
  print("Namaste" , name)
elif nat == 'usa':
  print("Welcome" , name)
elif nat == 'french':
  print("Bienvenue", name)
elif nat == 'spain':
  print("Bienveinida", name)
elif nat == 'uae':
  print("Marhaba" , name)
else:
  print ("Welcome", name)




# Display the first 10 natural numbers using while 
num = 1
while num <= 10:
    print(num)
    num += 1


# Create a program to reverse the digits of given integer.


def reverse_integer(n):
    str_n = str(n)  
    reversed_str = str_n[::-1] 
    reversed_int = int(reversed_str)
    return reversed_int

# Example usage
num = 12345
reversed_num = reverse_integer(num)
print("Original number:", num)
print("Reversed number:", reversed_num)


# create a program to print the below mentioned pattern.  1
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
num_rows = 5
print_pattern(num_rows)



# Create a program to print the below mentioned pattern.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def print_pattern(rows):
    for i in range(1, rows + 1):
        print("* " * i)
    for i in range(rows - 1, 0, -1):
        print("* " * i)
num_rows = 5
print_pattern(num_rows)
