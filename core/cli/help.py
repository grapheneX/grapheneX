class Help:
	"""
	Help class for commands
	"""

	@staticmethod
	def message(syntax,message):
		print("\nsyntax: " + syntax + "\n")
		print(message + "\n")

	def help_switch(self):
		self.message(syntax="switch [module]",message="Change module")