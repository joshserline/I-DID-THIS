# nested loops = the 'inner loop will finish all of its iteration before finishing one interaction of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many collums?: "))
symbols = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbols, end="")
    print()