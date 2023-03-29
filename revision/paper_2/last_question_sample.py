
def create2DArray(r,c):
    output = []
    
    # method 1
    for i in range(r):
        output += [[""] * c]

    # method 2
    for i in range(r):
        row = []
        for j in range(c):
            row.append("")
        output.append(row)

    return output


absences = [["Elma", 2], ["Mika", 8], ["Art", 0], ["Tan", 1], ["Gerbert", 3]]
# absences = [["Elma", "Mika", "Art", "Tan", "Gerbert"], [2,8,0,1,3]]

def getAbscences(name):

    for i in range(len(absences)):
        if absences[i][0] == name:
            return absences[i][1]

    return -1


def createSeatingChart(studentList, r, c):
    chart = create2DArray(r,  c)
    
    counter =  0

    col = 0
    row = 0

    while counter < len(studentList):
        absences = getAbscences(studentList[counter])
        if absences >= 0 and absences <= 5:
            chart[row][col] = studentList[counter]
            # The way below doesn't need a row or col, but is more difficult
            # chart[counter%c][counter//c] == studentList[counter] 

        counter += 1
        col += 2
        if col == c:
            col = 0
            row += 1
    return chart

students = ['Elma', 'Mika', 'Art', 'Tan', 'Gerbert', 'Patricia']

chart = createSeatingChart(students, 2,4)
print(chart)
