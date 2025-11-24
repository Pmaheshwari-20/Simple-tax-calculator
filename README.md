# Working and Logic:
-The core logic relies on defining specific income thresholds (tax brackets) and applying a corresponding tax rate to the portion of income that falls within that bracket.

-Conditional Logic: Uses if statements to check which tax rate bracket the income belongs to.

-Progressive Tax: Tax rates increase as the income amount increases
- Tax brackets :

- For: 
    - Income < 12 lakhs
      - Tax rate = 0%
 
    -  25 lakhs > Income >= 12 lakhs
       - Tax rate =  12%
 
    - 35 Lakhs > Income >= 25 lakhs
      - Tax rate = 18%
 
    - Income > 35 lakhs
      - Tax rate =  28%

- TDS Rate is fixed here, around 10% for any amount.

# How to use:
- You would input the user's annual taxable income, and the program would execute the conditional logic to output the calculated tax amount.
