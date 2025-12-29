# name: ADEKEYE JOHN OLAOLUWA
# matric: BU24SEN1045
tax_bracket = {
    0: [  # Single filers
        (0, 8350, 0.10),
        (8350, 33950, 0.15),
        (33950, 82250, 0.25),
        (82250, 171550, 0.28),
        (171550, 372950, 0.33),
        (372950, float("inf"), 0.35)
    ],
    1: [  # Married filing jointly /widower
        (0, 16700, 0.10),
        (16700, 67900, 0.15),
        (67900, 137050, 0.25),
        (137050, 208850, 0.28),
        (208850, 372950, 0.33),
        (372950, float("inf"), 0.35)
    ],
    2: [  # Married filing separately
        (0, 8350, 0.10),
        (8350, 33950, 0.15),
        (33950, 68525, 0.25),
        (68525, 104425, 0.28),
        (104425, 186475, 0.33),
        (186475, float("inf"), 0.35)
    ],
    3: [  # Head of household
        (0, 11950, 0.10),
        (11950, 45500, 0.15),
        (45500, 117450, 0.25),
        (117450, 190200, 0.28),
        (190200, 372950, 0.33),
        (372950, float("inf"), 0.35)
    ]
    # the bracket contains the lower, upper limit and tax rate

}
def tax_calculation(status,income): # this part of the code code calculates you tax based on your tax bracket 
    tax= 0
    for lower, upper,tax_rate in tax_bracket[status]:
        if income > lower:
            taxable_money = min(income,upper) - lower
            tax += taxable_money * tax_rate
        else:
            break
    return tax
status = int(input('Enter filing status (0=Single, 1=Married Joint, 2=Married Separate, 3=Head): '))
income = float(input("Enter taxable income: "))
if status not in [0,1,2,3] and income< 0:
    print("invalid input")
else:
    print(f'your tax from your tasabe income is: {tax_calculation(status,income)}')
