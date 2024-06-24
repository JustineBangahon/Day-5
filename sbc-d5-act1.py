l = []

def add():
    n = int(input("Enter the number of data you want to insert: "))
    for i in range(n):
        num = input("Enter Number Data: ")
        l.append(num)
        print(f"\nThis is the Data: {l}")

def queue():
    #l.sort()
    l.pop(0)
    print(f"\nThis is the Queue Now: {l}")

def stack():
    l.pop(-1)
    print(f"\nThis is the Stack NOw: {l}")

add()
while True:
    choice = {1: 'Naa', 2: 'Wala'}
    print("Si Boss Kay  1: NAA | 2: WALA\n")
    you = int(input("Enter Choice: "))
    if you not in choice:
        print("Invalid Input\n")
        print(l)
    elif len(l) == 0:
        print("No Data Left\n")
        add()
    elif you == 1:
        queue()
    elif you == 2:
        stack()
    else: 
        ...
    
   


