n_defn = "ecehan"
s_defn = "vergiliel"
list_of_course = []

def grades():
    m = int(input("Please enter your midterm grade: "))
    f = int(input("Please enter your final grade: "))
    p = int(input("Please enter your project grade: "))
    d = {"Midterm: ": m, "Final:": f, "Project:": p}
    print (d)
    final_grade = (m * 0.3) + (f * 0.5) + (p * 0.2)
    print ("Your average is: {}".format(final_grade))
    if final_grade > 90:
        print("AA")
    elif 70 < final_grade < 90:
        print("BB")
    elif 50 < final_grade < 70:
        print("CC")
    elif 30 < final_grade < 50:
        print("DD")
    elif final_grade < 30:
        print("FF")
        print("You failed in class.")

def course_name():
    course = input("Please enter course name (min 3 and max 5 courses)[enter Q to quit]: ")
    list_of_course.append(course)
    count1 = 1
    while count1 < 5:
        count1 += 1
        course = input("Please enter course name: ")
        list_of_course.append(course)
        if course == "Q" and count1 < 4:
            print("You failed in class")
            break
        elif course == "Q" and count1 >= 3:
            print("Your course info has been saved")
            list_of_course.pop()
            print("Your courses: ", list_of_course)
            grades()
            break
        elif count1 == 5:
            print("Your course info has been saved")
            print("Your courses: ", list_of_course)
            grades()
            break


count = 0
n = input("Please enter your name: ")
s = input("Please enter your surname: ")
if n_defn == n.lower() and s_defn == s.lower():
    print("Welcome, {}".format(n.capitalize()))
    course_name()
else:
    while n_defn != n and s_defn != s:
        count += 1
        if n_defn != n and s_defn != s and count != 3:
            print("You entered wrong name/surname, try again.")
            n = input("Please enter your name: ")
            s = input("Please enter your surname: ")
        if n_defn == n.lower() and s_defn == s.lower() and count != 3:
            print("Welcome, {}".format(n.capitalize()))
            course_name()
            break
        elif count == 3:
            print("Please try again later.")
            break
