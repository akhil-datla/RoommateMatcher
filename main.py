import numpy as np
import pandas as pd
from algorithm import Matching, Group
import sys

# Group size is 4
groupSize = 4

#Student Groups list
studentGroups = []

# Check if there is a CSV file with the list of students and their preferences
if len(sys.argv) < 2:
    print("Please input a CSV file with students and their preferences.")
    sys.exit()
else:
    # Import the list of students as a Pandas dataframe
    studentsDf = pd.read_csv(sys.argv[1], header=0)

if studentsDf.shape[0] <= 0:
    print("Dataframe is empty.")
    sys.exit()

# Initialize a matrix of student preferences with the default value of 0 (no preference)
studentPrefMatrix = np.zeros((studentsDf.shape[0], studentsDf.shape[0]), dtype=float)

for idx in studentsDf.index:
    row = studentsDf.loc[idx]
    student = row["Email Address"]
    prefs = [
        row["Roommate Preference #1 Email"],
        row["Roommate Preference #2 Email"],
        row["Roommate Preference #3 Email"],
    ]

    for pref in prefs:
        # if the prefrence is in the dataset and student is not the same as the prefrence
        if (
            studentsDf[studentsDf["Email Address"] == pref].index.values.size > 0
            and pref != student
        ):

            studentPrefMatrix.itemset(
                (
                    studentsDf[studentsDf["Email Address"] == pref].index[0],
                    studentsDf[studentsDf["Email Address"] == student].index[0],
                ),
                (10 - (prefs.index(pref) * 3)),
            )
        else:
            print(f"{student} has no preference {prefs.index(pref)+1} or is the same as the prefrence: {pref}")

# Running Irving's algorithm
matching = Matching(
    studentPrefMatrix, group_size=groupSize, iter_count=2, final_iter_count=2
)
score, studentIdxs = matching.solve()
print(f"Irving's Algorithm Score: {score}")

# Converting list of student indexes to list of student names
for group in studentIdxs:
    studentGroup = []
    for studentIdx in group:
        studentGroup.append("Full Name: %s, Gender: %s, Grade: %s" % (studentsDf.iloc[studentIdx]["Full Name"], studentsDf.iloc[studentIdx]["Gender"], studentsDf.iloc[studentIdx]["Grade"]))
    studentGroups.append(studentGroup)

studentsDf = pd.DataFrame(data=studentGroups)
studentsDf.to_csv('rooms.csv',index=True, header=False)
