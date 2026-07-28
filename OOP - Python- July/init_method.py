class student:
    def __init__(self, matric_no, first_name, last_name):
        self.matric_no = matric_no
        self.first_name = first_name
        self.last_name = last_name


ayo = student( "2000", "Tinbzy", "Asiwajs")
ayo_two = student( "20200", "Tinb", "Asiwas")

print (f"ayo's matric number: {ayo.matric_no}")
print (f"ayo 2's matric number: {ayo_two.matric_no}")