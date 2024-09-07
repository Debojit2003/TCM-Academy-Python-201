def print_out(a):
	print("Outer: {}".format(a))

	def print_in():
		print("\t Inner: {}".format(a))

	return print_in

test2 = print_out("test")


test2()