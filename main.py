class Course:
    def __init__(self, course_label, section, instructor, days, time_display):
        self.course_label = course_label
        self.time_display = time_display # 8:00-9:15
        self.section = section  # 0,1,2,3,...
        self.instructor = instructor  # name
        self.days = days  # "S,M,T,W,R" capital letters with comma
    def time_start(self): # return string
        return self.time_display.split("-")[0]
    def time_end(self): # return string
        return self.time_display.split("-")[1]
    def collision(self, other): # other is another Course object
        # return True if self and other have collision
        flag_days = True # keep True if no days in common

        for day in self.days:
            if day in other.days:
                flag_days = False
        if flag_days: # no days in common

            return False
        if float(self.time_start().replace(":", ".")) >= float(other.time_end().replace(":", ".")):
            # print(other.time_end())
            return False
        if float(self.time_end().replace(":", ".")) <= float(other.time_start().replace(":", ".")):
            return False
        return True


    def __str__(self):
        return f"{self.course_label}-{self.section}-{self.instructor}-{self.days}-{self.time_start()} -> {self.time_end()}"


# course_label, section, instructor, days, time_display
arab1 = Course("CS101", 0, "Dr. John", "Tue,Wen", "8:00-9:15")
arab2 = Course("CS101", 1, "Dr. John", "Tue,Wen", "7:30-10:45")
arab3 = Course("CS101", 2, "Dr. John", "Tue,Wen", "9:30-10:45")
# print(arab1.collision(arab3))

eng1 = Course("CS102", 0, "Dr. Abbas", "Tue,Wen", "8:00-9:15")
eng2 = Course("CS102", 1, "Dr. Abbas", "Tue,Wen", "7:30-10:45")
eng3 = Course("CS102", 2, "Dr. Abbas", "Tue,Wen", "9:30-10:45")
# print(eng1.collision(eng3))

courses = [[arab1, arab2, arab3], [eng1, eng2, eng3]]

# ------------------ 1 ------------------

dec = {}

def print_combinations(ArraySec, index=0, current_combination=[]):
    if index == len(ArraySec):
        chosenSections = []
        for sec in range(len(current_combination)): # making list of chosen sections
            chosenSections.append(courses[sec][current_combination[sec]])
            #example : chosenSections =  [<__main__.Course object at 0x000002B2EF867FD0>, <__main__.Course object at 0x000002B2EF867D90>]

        # check if there is a collision between chosen sections
        for i in range(len(chosenSections)):
            for j in range(i+1, len(chosenSections)):
                if chosenSections[i].collision(chosenSections[j]):
                    return
        chosenSectionsTuple = tuple(chosenSections)

        dec[chosenSectionsTuple] = False
        return

    max_number = len(ArraySec[index]) - 1
    for i in range(max_number + 1):
        current_combination.append(i)
        print_combinations(ArraySec, index + 1, current_combination)
        current_combination.pop()

ArraySec = [[arab1, arab2, arab3], [eng1, eng2, eng3]]

print_combinations(ArraySec)
# print(dec)
# ------------------ 2 ------------------
for key in dec.keys():
    for k in key:
        print(k)

    print("*************")
