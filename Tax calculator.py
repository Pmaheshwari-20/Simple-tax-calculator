first_tax_rate= 0.12
Second_tax_rate= .18
third_tax_rate= .28
no_tax_rate= 0
Income= float(input("Please enter your income for tax to be calculated: "))
TDS= float(input("Enter if TDS paid"))
TDS_rate= 0.10

if Income <= 1200000.00:
 tax_rate = no_tax_rate
 Tax_calculated = Income*tax_rate
 print("No tax to be paid")

if 2500000.00 > Income > 1200000.00:
 tax_rate= first_tax_rate
 Tax_calculated = Income*first_tax_rate
 print(f"Tax Rate in your income slab is: {tax_rate:,.2f}")
 print(f"Tax calculated in income is: {Tax_calculated:,.2f}")


if 3500000.00 > Income >= 2500000.00:
 tax_rate = Second_tax_rate
 Tax_calculated = Income*tax_rate
 print(f"Tax Rate in your income slab is: {tax_rate:,.2f}")
 print(f"Tax calculated in income is: {Tax_calculated:,.2f}")

if Income >= 3500000.00:
 tax_rate = third_tax_rate
 Tax_calculated = Income*tax_rate
 print(f"Tax Rate in your income slab is: {tax_rate:,.2f}")
 print(f"Tax calculated in income is: {Tax_calculated:,.2f}")

if TDS >= 0:
 TDS_amount = TDS*TDS_rate
 print(f"TDS to be credited when filing annual income tax return:{TDS_amount:,.2f}")


Income_inhand = Income - Tax_calculated - TDS_amount
print(f"Total income in hand after taxes:{Income_inhand:,.2f}")