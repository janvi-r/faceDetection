
import csv

def mark_attendance(name, attendance):
    print("in mark_attendance")

    with open("attendance.csv", newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        if row["name"] == name:
            print("Found the row:", row)
            row["attendance_today"] = str(attendance)
            row["attendance_timestamp"] = 0  # idk how to do the time stamp
            row["total_attendance"] = str(int(row["total_attendance"]) + 1)

    # rewrites all the new data, i didn't know how else to do it.
    with open("attendance.csv", "w", newline='') as file:
        writer = csv.DictWriter(file,
                                fieldnames=["name", "attendance_today", "attendance_timestamp", "total_attendance"])
        writer.writeheader()
        writer.writerows(rows)