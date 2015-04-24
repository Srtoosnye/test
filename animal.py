# filename: animal.py

class animal:
	def __init__(self):
		print 'Animal:',
	def sound(self):
		print 'fuck!'
		
class cat(animal):
	def __init__(self):
		print 'Cat:',
	def sound(self):
		print 'Meow!'

class dog(animal):
	def __init__(self):
		print 'Dog:',
	def sound(self):
		print 'Bark!'

a = animal()
a.sound()		
c = cat()
c.sound()
d = dog()
d.sound()