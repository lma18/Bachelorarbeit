# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import openpyxl
wb = openpyxl.load_workbook('Bachelorarbeit_Abbildungen.xlsx')
sheet = wb.get_sheet_by_name("Teaser_Variante2_Moritz")
activities = []
for rowOfCellObjects in sheet['A19':'A25']:
    for cellObj in rowOfCellObjects:
               activities.append(cellObj.value)

slices = []

for Flaechen in sheet['C19':'C25']:
    for prozent in Flaechen:
               slices.append(prozent.value)        
plt.pie(slices, labels = activities,colors = colors, shadow = True, autopct = '%1.1f%%')               
            