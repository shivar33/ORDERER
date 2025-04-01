import numpy as np
data_type = [('First_name','S15'),('class','S15'),('height',int)]
details = [('John','5J',127),('Philp','5W',152),('Jack','6O',140)]
students = np.array(details ,dtype=data_type)
print("Student list (no order)")
print(students)
print("Student list (Height order)")
print(np.sort(students,order='height'))

