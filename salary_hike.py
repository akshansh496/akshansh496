job_level=int(input("Enetr job level"))
current_salary=int(input("enter the current salary"))
if job_level==3:
    new_salary=current_salary+(15/100)*current_salary
elif job_level==4:
    new_salary=current_salary+(7/100)*current_salary
elif job_level==5:
    new_salary=current_salary+(5/100)*current_salary
else:
    new_salary=current_salary
print("New Salary:",new_salary)