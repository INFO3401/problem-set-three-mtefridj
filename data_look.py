import pandas as pd
import matplotlib.pyplot as plt
from utils import *
new_db = localandCleanData('creditData.csv')
#print(new_db.head(20))
#print(helloWorld())
column_name = list(new_db.columns)
for i in column_name:
    computePDF(i,new_db)
    visualDistribution(i,new_db)
    viewLogDistribution(i, new_db)
print(computeDefaultRisk('MonthlyIncome',[0,1000],new_db,'SeriousDlqin2yrs'), 'Monthly Income')
print(computeDefaultRisk('age',[0,40],new_db,'SeriousDlqin2yrs'), 'age')
print(computeDefaultRisk('RevolvingUtilizationOfUnsecuredLines',[0,10000],new_db,'SeriousDlqin2yrs'), 'Utilization of Unsecured Lines')
print(computeDefaultRisk('NumberOfTime30-59DaysPastDueNotWorse',[0,20],new_db,'SeriousDlqin2yrs'), 'Number of Days Past Due')
print(computeDefaultRisk('DebtRatio',[0,2],new_db,'SeriousDlqin2yrs'), 'Debt Ratio')
print(computeDefaultRisk('NumberOfOpenCreditLinesAndLoans',[0,20],new_db,'SeriousDlqin2yrs'), 'Open Credit Lines and Loans')
print(computeDefaultRisk('NumberOfTimes90DaysLate',[0,15],new_db,'SeriousDlqin2yrs'), '90 Days Late')
print(computeDefaultRisk('NumberRealEstateLoansOrLines',[0,15],new_db,'SeriousDlqin2yrs'), 'Number of Real Estate Loans')
print(computeDefaultRisk('NumberOfTime60-89DaysPastDueNotWorse',[0,5],new_db,'SeriousDlqin2yrs'), '60-89 Days past due')
print(computeDefaultRisk('NumberOfDependents',[0,5],new_db,'SeriousDlqin2yrs'), 'Number of Dependents')
other_db = localandCleanData('newLoans.csv')
def predictDefaultRisk(datarow, data):
    total_prob = 0
    columns = list(data.columns)
    for y in columns:
        if y == 'RevolvingUtilizationOfUnsecuredLines' or y == 'DebtRatio' or y == 'NumberOfOpenCreditLinesAndLoans' or y == 'NumberRealEstateLoansOrLines':
            feat_prob = .1 * computeDefaultRisk(y,[0,datarow[y]], new_db, 'SeriousDlqin2yrs')
            total_prob += feat_prob
        elif y == 'age' or y == 'NumberOfDependents':
            feat_prob = .025 * computeDefaultRisk(y,[0,datarow[y]], new_db, 'SeriousDlqin2yrs')
            total_prob += feat_prob
        elif y != 'SeriousDlqin2yrs':
            feat_prob = .15 * computeDefaultRisk(y, [0, datarow[y]], new_db, 'SeriousDlqin2yrs')
            total_prob += feat_prob
    return total_prob
for i,datarow in other_db.iterrows():
    datarow['SeriousDlqin2yrs'] = predictDefaultRisk(datarow, other_db)
    print(datarow['SeriousDlqin2yrs'])
new_pdf = other_db
pdf_columns = list(new_pdf.columns)
for x in pdf_columns:
    computePDF(x,new_pdf)