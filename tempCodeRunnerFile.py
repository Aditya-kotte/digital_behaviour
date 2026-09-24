#app name
import csv
APP  = "Instagram"

minutes = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row[APP] = row['Instagram_Minutes'] #ikada reader ki assign chestunam abt the data we are taking
        minutes.append(int(row[APP]))

total_minutes = sum(minutes)
average_minutes = total_minutes / len(minutes)
minimum_minutes = min(minutes)
maximum_minutes = max(minutes)

counter = 0
for value in minutes:
    if value > average_minutes:
        counter += 1

print("Appname:", APP)
print("Total:", total_minutes)
print("Average:", average_minutes)
print("Minimum:", minimum_minutes)
print("Maximum:", maximum_minutes)
