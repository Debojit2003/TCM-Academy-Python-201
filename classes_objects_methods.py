class Person:
	'Person base class'
	wants_to_hack = True


	def __init__(self, name, age):
		self.name = name
		self.age = age
	def print_name(self):
		print("My name is {}".format(self.name))
	def print_age(self):
		print("{}\'s age is {}".format(self.name, self.age))
	def birthday(self):
		self.age += 1
bob = Person("bob", 30)
alice = Person("alice", 20)
mallory = Person("mallory", 50)

print(bob)
print(alice)
print(mallory)

bob.print_name()
alice.print_name()
mallory.print_name()

bob.print_age()
alice.print_age()
mallory.print_age()


print(bob.name)
print(bob.age)

print(hasattr(bob, "age"))
print(hasattr(bob, "asd"))

print(getattr(bob, "age"))
setattr(bob, "asd", 100)
print(getattr(bob, "asd"))

delattr(bob, "asd")

#print(getattr(bob, "asd"))

print(Person.wants_to_hack)
print(bob.wants_to_hack)

Person.wants_to_hack = "No i'm afraid"
print(Person.wants_to_hack)
print(bob.wants_to_hack)
print(alice.wants_to_hack)

bob.wants_to_hack = "Yes i'm interested"
pprint(Person.wants_to_hack)
print(bob.wants_to_hack)
print(alice.wants_to_hack)