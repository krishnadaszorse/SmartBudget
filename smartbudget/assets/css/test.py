students = ['Bharti','Bharat','Akash','Bhavya','Chand','Brijesh','Chetak','Aravind','Bhavana']

result = {}
for student in students:
	print student
	
	if student[0] in result:
		result[student[0]].append(student)
	else:
		result[student[0]] = [student]
print result
