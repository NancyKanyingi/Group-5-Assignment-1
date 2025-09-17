basic_salary = (input("Enter salary: "))
benefits = (input("Enter benefits: "))
#calculate gross_salary
def calaculate_gross_salary(basic_salary,benefits):
    return basic_salary + benefits
#calculate shif
def calculate_shif_deductions(gross_salary):
    return (2.75 / 100) * gross_salary
#calculate nssf
def calculate_nssf_deductions(gross_salary):
    NSSF = 0.06 * gross_salary
    if gross_salary >= 8000 and gross_salary <=72000:
       return NSSF
    else:
        NSSF < 8000
        return 0

#calculate payee
def calculate_payee(taxable_income):
    tax = 0
    tax1 =0
    tax2 =0
    tax3 =0
    tax4 =0
    tax5 =0
    if taxable_income <= 24000:
         tax1 = 0.1 * taxable_income
    elif taxable_income <= 32333:
         tax2 = (24000*0.1) + ((taxable_income-24000)*0.25)
    elif taxable_income <= 500000:
         tax3 = (24000*0.1) + ((taxable_income-32333)*0.3)
    elif taxable_income <= 800000:
         tax4 = (24000*0.1) + ((taxable_income-500000)*0.325)
    elif taxable_income >= 800000:
         tax5 = (24000*0.1) + ((taxable_income-800000)*0.35)
    else:
         tax = 0
    tax = tax1+tax2+tax3+tax4+tax5
    return tax

print(calculate_payee(20000))

def calculate_net_salary(gross_salary,payee, nssf,shif):
    return (gross_salary)-(payee+shif+nssf)
print(calculate_net_salary(30000,4000,2000,3000))
gross_salary = calaculate_gross_salary(20000, 10000)
print(gross_salary)
print(calculate_shif_deductions(gross_salary))
print(calculate_nssf_deductions(gross_salary))