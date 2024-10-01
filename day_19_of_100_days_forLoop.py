# day_19_of_100_days_forLoop

# loan calculator
# ten year loan to borrom $1,000
# five percent interest rate

# variable for amount to be borrowed and add interest to
borrowed = 1_000
total = 0
interest_rate = 0.05
period = 10

# list comprehensions
simple_interest = [borrowed * interest_rate for _ in range(period)]
# print(sum(simple_interest))

compound_interest = [borrowed * (1 + interest_rate) ** _ for _ in range(period)]
print(compound_interest)

for year in range(period):
    year = year + 1
    borrowed = borrowed * (1 + interest_rate)
