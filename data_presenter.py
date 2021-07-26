file = open('CupcakeInvoices.csv')

for line in file:
    print(line)

file.close()
file = open('CupcakeInvoices.csv')

for line in file:
    line = line.rstrip('\n').split(',')
    print(line[2])

file.close()
file = open('CupcakeInvoices.csv')

total = 0

for line in file:
    line = line.rstrip('\n').split(',')
    quantity = float(line[3])
    amount = float(line[4])
    line_total = quantity*amount
    total += line_total
    print(round(line_total, 2))

print(round(total, 2))

file.close()



