def add_applicant(applicant_, index):
    if applicant_[index] == 'Biotech':
        departments[applicant[index]].append([applicant[0], applicant[1], (float(applicant[6]) if float(applicant[6]) > (float(applicant[3]) + float(applicant[2])) / 2 else (float(applicant[3]) + float(applicant[2])) / 2)])
    elif applicant_[index] == 'Chemistry':
        departments[applicant[index]].append([applicant[0], applicant[1], (float(applicant[6])) if float(applicant[6]) > float(applicant[3]) else float(applicant[3])])
    elif applicant_[index] == 'Engineering':
        departments[applicant[index]].append([applicant[0], applicant[1], (float(applicant[6]) if float(applicant[6]) > (float(applicant[5]) + float(applicant[4])) / 2 else (float(applicant[5]) + float(applicant[4])) / 2)])
    elif applicant_[index] == 'Mathematics':
        departments[applicant[index]].append([applicant[0], applicant[1], (float(applicant[6]) if float(applicant[6]) > float(applicant[4]) else float(applicant[4]))])
    elif applicant_[index] == 'Physics':
        departments[applicant[index]].append([applicant[0], applicant[1], (float(applicant[6]) if float(applicant[6]) > (float(applicant[2]) + float(applicant[4])) / 2 else (float(applicant[2]) + float(applicant[4])) / 2)])


def sort_by_department(applcnts, depart):
    if depart == 'Chemistry':
        return sorted(applcnts, key=lambda x: (-float(x[6]) if -float(x[6]) < -float(x[3]) else -float(x[3]), x[0], x[1]))
    elif depart == 'Engineering':
        return sorted(applcnts, key=lambda x: (-float(x[6]) if -float(x[6]) < -(float(x[5]) + float(x[4])) / 2 else -(float(x[5]) + float(x[4])) / 2, x[0], x[1]))
    elif depart == 'Mathematics':
        return sorted(applcnts, key=lambda x: (-float(x[6]) if -float(x[6]) < -float(x[4]) else -float(x[4]), x[0], x[1]))
    elif depart == 'Physics':
        return sorted(applcnts, key=lambda x: (-float(x[6]) if -float(x[6]) < -(float(x[2]) + float(x[4])) / 2 else -(float(x[2]) + float(x[4])) / 2, x[0], x[1]))
    elif depart == 'Biotech':
        return sorted(applcnts, key=lambda x: (-float(x[6]) if -float(x[6]) < -(float(x[3]) + float(x[2])) / 2 else -(float(x[3]) + float(x[2])) / 2, x[0], x[1]))


max_n_students = int(input())
students = open('applicants.txt', 'r')

applicants = []  # List of all the applicants.
departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}

for student in students:
    applicants.append(student.split())  # Adds every student to applicants list.

# Sorts applicants firstly by their GPA then their department, name, surname.
applicants.sort(key=lambda x: (-float(x[2]), -float(x[3]), -float(x[4]), -float(x[5]), x[7], x[0], x[1], x[8], x[9]))


accepted = []
i = 7
while True:
    for depart in departments:
        applicants = sort_by_department(applicants, depart)
        for applicant in applicants:
            if len(departments[applicant[i]]) < max_n_students and applicant[i] == depart:
                add_applicant(applicant, i)
                accepted.append(applicant)
    i += 1
    for j in range(len(accepted)):
        if accepted[j] in applicants:
            applicants.remove(accepted[j])
    if i > 9:  # simple check to break loop.
        break


for department in departments.keys():
    departments[department].sort(key=lambda x: (-float(x[2]), x[0], x[1]))
    new_file = open(f"{department}.txt", "w")
    for name, surname, gpa in departments[department]:
        new_file.write(f"{name} {surname} {gpa}\n")
    new_file.close()

students.close()
