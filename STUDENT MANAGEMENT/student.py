import csv
import os

FILE_NAME = "student.csv"

#  create a csv file if doesn't exist
def create_file():
    if not  os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file :
            writer = csv.writer(file)
            writer.writerow(["Student_ID","Name", "Age", "Course", "Phone"])

#  add student
