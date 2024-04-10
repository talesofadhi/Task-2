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