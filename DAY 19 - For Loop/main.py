print ("""Loan Calculator

Working out the interest of a oan of $1000 over 10 years at 5% APR:
""")

loan = 1000
apr = 0.05
for year in range(10):
  loan+=(loan*apr)
  print("Year", year+1, "is $", round (loan,2))