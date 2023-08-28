import matplotlib.pyplot as plt
import numpy as np

data = {'C': 20, 'C++': 15, 'Java': 30, 'Python': 35};

courses = list(data.keys());
values = list(data.keys());

fig = plt.figure(figsize = (10, 5));

plt.bar(courses, values, color='Maroon', width = 0.4);

plt.xlabel("Courses Offered");
plt.ylabel("No. of Students Offered");
plt.title("Student Enrolled In Different Courses");

plt.show();