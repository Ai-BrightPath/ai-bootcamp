hours = [2, 1.5, 3, 0, 2.5, 1, 4]
print(hours)
total = sum(hours)
print(f"Total hours this week: {total}")
average = total / len(hours)
print(f"Daily average: {average}")
best = max(hours)
print(f"Most hours in one day: {best}")
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
best_day = days[hours.index(best)]
print(f"Best day: {best_day}")