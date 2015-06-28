def parse(data):
	persons = []
	for d in data:
		d = d.rstrip('\n')
		words = d.split(";")
		person = parse_person(words)
		if person:
			persons.append(person)
		
		appointment_data = parse_appointment(words)
		if appointment_data:
			id, start, end = appointment_data
			person = next(p for p in persons if p.id == id)
			person.add_appointment((start, end))

	return persons

def parse_person(words):
	if len(words) == 2:
		id = words[0]
		name = words[1]
		return Person(id, name)

def parse_appointment(words):
	if len(words) == 4:
		id = words[0]
		start = words[1]
		end = words[2]
		return id, start, end 


class Person():

	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.appointments = []

	def add_appointment(self, appointment):
		self.appointments.append(appointment)
















# def parse(schedules):
# 	res = []
# 	for s in schedules:

# 		person = parse_person(s)
# 		if person: 
# 			res.append(person)

# 		appointment_data = parse_appointment(s)
# 		if appointment_data:
# 			id, start, end = appointment_data
# 			person = next(p for p in res if p.id == id)
# 			person.add_appointment(start, end)

# 	return res


# def parse_appointment(s):
# 	strings = s.split(";")
# 	if len(strings) == 4:
# 		id = strings[0]
# 		start = strings[1]
# 		end = strings[2]
# 		return id, start, end


# def parse_person(s):
# 	strings = s.split(";")
# 	if len(strings) == 2:
# 		id = strings[0]
# 		name = strings[1]
# 		return Person(id, name)
		
# class Person:
# 	def __init__(self, id, name):
# 		self.id = id
# 		self.name = name
# 		self.appointments = []


# 	def add_appointment(self, start, end):
# 		self.appointments.append((start, end))


