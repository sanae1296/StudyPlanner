# planner.py

available_hours = int(input("Enter available hours today: "))
subjects = []

while True:
    name = input("Enter subject name (or 'done' to finish): ")
    if name.lower() == "done":
        break
    priority = int(input(f"Enter priority for {name} (1-5): "))
    hours = int(input(f"Enter hours needed for {name}: "))
    subjects.append({"name": name, "priority": priority, "hours": hours})

subjects_sorted = sorted(subjects, key=lambda x: x["priority"], reverse=True)

plan = []
hours_left = available_hours

for subject in subjects_sorted:
    if hours_left >= subject["hours"]:
        plan.append(f"{subject['name']} → {subject['hours']}h")
        hours_left -= subject["hours"]

print("\nStudy Plan for Today:")
for item in plan:
    print("-", item)
print("Free time left:", hours_left, "hours")
