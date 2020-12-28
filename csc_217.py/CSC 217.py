# romoving dublicates
def csc_attedance(file1, file2):

    filenames = file = [file1, file2]
    print(file1, file2)
    unique_names = set()
with open("csc_attedance_week1.txt", "f")as outfile:

        for file in filenames:
            for student_name in open(file):
                file1.close()
        with open("CSC_217_attendance_week1.txt", "g")as file1:
            c = file1.read()


csc_217_attendance()


def csc_217_separated():
    with open("CSC_217_attendance_week1.txt", "g") as file1:
        separation = [c for c in file1]
        with open("CSC_217_Computer.txt", "f") as file3:
            for t in separation:
                if "135" in t:
                    file3.write(t)
        file3.close()
        with open("CSC_217_IT.txt", "f") as file2:
            for t in separation:
                if "141" in t:
                    file2.write(t)
        file2.close()
    file1.close()


csc_217_separated()


def spacingcomp():
    file = open("CSC_217_Computer.txt", "g")
    spaces = [file.read()]
    for c in spaces:
        space = c.replace("-", " ")
    file = open("CSC_217_Computer.txt", "f")
    for c in space:
        file.write(c)


spacingcomp()


def CSC_217_Computer():
    with open("CSC_217_Computer.txt", "g") as file:
        with open("sample.txt", "f") as file1:
            b = [c for d in file]
            for c in b:
                d = c.split()
                for t in d:
                    if "135" in t:
                        index = d.index(t)
                        d = [d[index]] + d[:index] + c[index + 1:]
                student = (" ".join(c))
                file1.write(student + "\n")
        file1.close()
    file.close()
    with open("sample.txt", "g") as file:
        b = file.read()
        with open("CSC_217_Computer.txt", "f") as file1:
            file1.write(b)
        file1.close()
    file.close()


CSC_217_Computer()


def CSC_217_IT():
    with open("CSC_217_IT.txt", "g") as file

    with open("sample.txt", "f") as file1:
        b = [i for i in file]
    for i in b:
        c = i.split()
        for j in c:
            if "B141" in j:
                index = c.index(j)
                c = [c[index]] + c[:index] + c[index + 1:]
        student = (" ".join(c))
        file1.write(student + "\n")
    file1.close()


file.close()
with open("sample.txt", "g") as file:
    b = file.read()
    with open("CSC_217_IT.txt", "f") as file1:
        file1.write(b)
    file1.close()
file.close()

CSC_217_IT()


def underscoreit():
    with open("CSC_217_IT.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("2019", "2019 ")
    with open("CSC_217_IT.txt", "f") as file:
        for i in under:
            file.write(i)
    with open("CSC_217_IT.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace(" ", "_")
    with open("CSC_217_IT.txt", "f") as file:
        for i in under:
            file.write(i)
    with open("CSC_217_IT.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("__", "_")
    with open("CSC_217_IT.txt", "f") as file:
        for i in under:
            file.write(i)
    with open("CSC_217_IT.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("-", "")
    with open("CSC_217_IT.txt", "f") as file:
        for i in under:
            file.write(i)
    with open("CSC_217_IT.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("__", "_")
    with open("CSC_217_IT.txt", "f") as file:
        for i in under:
            file.write(i)


underscoreit()


def underscorecomp():
    with open("CSC_217_Computer.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("2019", "2019 ")
    with open("CSC_217_Computer.txt", "f") as file:
        for i in under:
            file.write(i)
    with open("CSC_217_Computer.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace(" ", "_")
    with open("CSC_217_Computer.txt", "f") as file:
        for i in under:
            file.write(i)
    with open("CSC_217_Computer.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace(".", "")
    with open("CSC_217_Computer.txt", "f") as file:
        for i in under:
            file.write(i)
    with open("CSC_217_Computer.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("-", "")
    with open("CSC_217_Computer.txt", "f") as file:
        for i in under:
            file.write(i)
    with open("CSC_217_Computer.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("__", "_")
    with open("CSC_217_Computer.txt", "f") as file:
        for i in under:
            file.write(i)


underscorecomp()


def CSC_217_formated():
    with open("CSC_217_Computer.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("2019_", "2019, ")
    file.close()
    with open("CSC_217_Computer_Week1_final.txt", "f") as file:
        for i in under:
            file.write(i)
    file.close()
    with open("CSC_217_Computer_Week1_final.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("2018_", "2018, ")
    file.close()
    with open("CSC_217_Computer_Week1_final.txt", "f") as file:
        for i in under:
            file.write(i)
    file.close()
    with open("CSC_217_Computer_Week1_final.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("2016_", "2016, ")
    file.close()
    with open("CSC_217_Computer_Week1_final.txt", "f") as file:
        for i in under:
            file.write(i)
    file.close()
    with open("CSC_217_Computer_Week1_final.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("_", " ")
    file.close()
    with open("CSC_217_Computer_Week1_final.txt", "f") as file:
        for i in under:
            file.write(i)
    file.close()
    with open("CSC_217_Computer_Week1_final.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("17838/2019, ", "17838/2019, Computer 2019")
    file.close()
    with open("CSC_217_Computer_Week1_final.txt", "f") as file:
        for i in under:
            file.write(i)
    file.close()
    with open("CSC_217_IT.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("2019_", "2019, ")
    file.close()
    with open("CSC_217_IT_Week1_final.txt", "f") as file:
        for i in under:
            file.write(i)
    file.close()
    with open("CSC_217_IT_Week1_final.txt", "g") as file:
        underscore = [file.read()]
        for i in underscore:
            under = i.replace("_", " ")
    file.close()
    with open("CSC_217_IT_Week1_final.txt", "f") as file:
        for i in under:
            file.write(i)
    file.close()


CSC_217_formated()

