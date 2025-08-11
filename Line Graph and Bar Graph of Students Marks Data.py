import matplotlib.pyplot as plt
students_names = ["Meet", "Garg", "Rahil", "Pujan", "Devarsh", "Ansh", "Marmik"]
students_marks=[20,25,28,32,35,38,40]
marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)
def marks_line_chart():
    plt.plot(students_names,students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Percentage")
    plt.show()
marks_line_chart()
def marks_bar_chart():
    plt.bar(students_names,students_marks)
    plt.title("Students Marks Graph")
    plt.xlabel("Student Names")
    plt.ylabel("Student Percentage")
    plt.show()
marks_bar_chart()