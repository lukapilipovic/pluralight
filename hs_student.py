from student import Student


class HighSchoolStudent(Student):
    school_name = "srednja skola"

    def get_school_name(self):
        return "this is a high school student"

