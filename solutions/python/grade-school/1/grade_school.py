class School:
    def __init__(self):
        self._roster = {}
        self._all_students = set()
        self._add_log = []

    def add_student(self, name, grade):
        if name in self._all_students:
            self._add_log.append(False)
            return
        
        if grade not in self._roster:
            self._roster[grade] = []
            
        self._roster[grade].append(name)
        self._all_students.add(name)
        self._add_log.append(True)

    def roster(self):
        sorted_roster = []
        for grade in sorted(self._roster.keys()):
            sorted_roster.extend(sorted(self._roster[grade]))
        return sorted_roster

    def grade(self, grade_number):
        return sorted(self._roster.get(grade_number, []))

    def added(self):
        return self._add_log