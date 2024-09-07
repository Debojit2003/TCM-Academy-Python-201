from datetime import datetime
import time
def logger(func):
	def wrapper():
		print("-"*50)
		print("> Execution started {}".format(datetime.today().strftime("%d-%m-%Y %H:%M:%S")))
		func()
		print("> Execution completed {}".format(datetime.today().strftime("%d-%m-%Y %H:%M:%S")))
		print("-"*50)
	return wrapper

@logger #logger(demo_function())
def demo_function():
	print("Executing task!")
	time.sleep(3)
	print("Task Completed!")

#demo_function()

def logger_args(func):
	def wrapper(*args, **kwargs):
		print("-"*50)
		print("> Execution started {}".format(datetime.today().strftime("%d-%m-%Y %H:%M:%S")))
		func(*args, **kwargs)
		print("> Execution completed {}".format(datetime.today().strftime("%d-%m-%Y %H:%M:%S")))
		print("-"*50)
	return wrapper
@logger_args
def demo_function_args(sleep_time):
	print("Executing task!")
	time.sleep(sleep_time)
	print("Task is completed")

demo_function_args(1)
demo_function_args(2)
demo_function_args(3)

