in_file = open('chicken.txt', 'r')

total_sales = 0
day_count = 0
for line in in_file:
    sales = line.strip().split(": ")
    total_sales += int(sales[1])
    day_count += 1

in_file.close()
print(total_sales / day_count)