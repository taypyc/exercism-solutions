class Garden:
    DEFAULT_STUDENTS = [
        "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
        "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
    ]
    
    PLANT_NAMES = {
        "G": "Grass",
        "C": "Clover",
        "R": "Radishes",
        "V": "Violets"
    }

    def __init__(self, diagram, students=None):
        self.rows = diagram.split("\n")
        
        if students:
            self.students = sorted(students)
        else:
            self.students = self.DEFAULT_STUDENTS

    def plants(self, student_name):
        index = self.students.index(student_name)
        
        start = index * 2
        
        codes = [
            self.rows[0][start], self.rows[0][start + 1],
            self.rows[1][start], self.rows[1][start + 1]
        ]
        
        return [self.PLANT_NAMES[code] for code in codes]