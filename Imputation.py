import pandas as pd
import numpy as np

data = {
    'Marks' : [90 , 95 , np.nan , 85] ,
    'Attendance' : [np.nan , 90 , 75 , 90]
}
df = pd.DataFrame(data) 
def missing(value):
    return value!=value
true_marks = [x for x in df['Marks'] if not missing(x)]
true_attendance = [y for y in df['Attendance'] if not missing(y)]
mean_marks = sum(true_marks) / len(true_marks)
mean_attendance = sum(true_attendance) / len(true_attendance)
df['Marks'] = [mean_marks if missing(x) else x for x in df['Marks']]
df['Attendance'] = [mean_attendance if missing(x) else x for x in df['Attendance']]

print(df)
