from matplotlib import pyplot as plt

file = open("CupcakeInvoices.csv")

total_choc = 0
total_van = 0
total_straw = 0

for line in file:
    line = line.rstrip('\n').split(',')
    if line[2] == "Chocolate":
        total_choc += 1
    elif line[2] == "Vanilla":
        total_van += 1
    else:
        total_straw += 1

line_x = ["Chocolate", "Vanilla", "Strawberry"]
line_y = [total_choc, total_van, total_straw]

plt.bar(line_x, line_y)
plt.xlabel('Cupcakes')
plt.ylabel('Money Earned')
plt.title('Money earned from each Cupcake Type')

plt.show()
