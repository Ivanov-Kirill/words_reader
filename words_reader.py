class words:
	def _init_(self):
		self.words = []
		self.words.append('')
		self.in_word = False
	def add(self, data):
		for i in data:
			if(self.in_word):
				if(i.isalpha()):
					i.lower()
					self.words[len(self.words)-1]+= i
				else:
					self.words.append('')
					self.in_word = False
			elif(i.isalpha()):
				i.lower()
				self.words[len(self.words)-1]+= i
				self.in_word = True
			
