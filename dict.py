rollno = int(input("Enter roll no: "))

Std = { 
        4553 :
        "\n-----------------------------------------------------REPORT CARD-----------------------------------------------\n"
            "---------------------------------------------------------------------------------------------------------------\nCourses\t\t\t\t\t\tMarks\t\t\tPoints\t\t\tGrade\n---------------------------------------------------------------------------------------------------------------"
            "\nEnglish\t\t\t\t\t\t90\t\t\t4.0\t\t\tA+\n"
            "Physics\t\t\t\t\t\t76\t\t\t2.5\t\t\tC+\n"
            "Computer Architecture\t\t\t\t88\t\t\t3.5\t\t\tB+\n"
            "Digital Logia Design\t\t\t\t62\t\t\t2.0\t\t\tC\n"
            "Data Structures and Algorithms\t\t\t72\t\t\t2.5\t\t\tC+\n"
            "OOP in Java\t\t\t\t\t77\t\t\t3.0\t\t\tB\n---------------------------------------------------------------------------------------------------------------\n"
            "\t\t\t\t\t\t\t\t\t\t\t\tGPA 2.92 ",

        4552 : 
        "\n-----------------------------------------------------REPORT CARD-----------------------------------------------\n"
            "---------------------------------------------------------------------------------------------------------------\nCourses\t\t\t\t\t\tMarks\t\t\tPoints\t\t\tGrade\n---------------------------------------------------------------------------------------------------------------"
            "\nEnglish\t\t\t\t\t\t66\t\t\t2.5\t\t\tC+\n"
            "Physics\t\t\t\t\t\t78\t\t\t2.5\t\t\tC+\n"
            "Computer Architecture\t\t\t\t81\t\t\t3.5\t\t\tB+\n"
            "Digital Logic Design\t\t\t\t62\t\t\t2.0\t\t\tC\n"
            "Data Structures and Algorithms\t\t\t92\t\t\t4.0\t\t\tA+\n"
            "OOP in Java\t\t\t\t\t67\t\t\t2.5\t\t\tB\n---------------------------------------------------------------------------------------------------------------\n"
            "\t\t\t\t\t\t\t\t\t\t\t\tGPA 2.9 ",
 }

if rollno in Std:
    print(Std[rollno])
else:
    print("invalid id")