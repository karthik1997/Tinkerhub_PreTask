class peerLearning:        
   stack = []
   def _init_ (self,name,position):
		self.name = name
		self.position = position
   def addStacks(skill):
		stack.append(skill)

   def setMentorOrLearner(self):
		if self.position == "mentor":
			print (self.name,"is a mentor")
			stack.append(self.skill)
	    else:
			print(self.name,"is a learner")

   def setAvailableTime(self)
    if self.role=="Mentor":
			self.time=input("enter the availiabe time")
    return

    def getMentor(self,stack,time)
      if self.role == "Mentor":
			for n in stack:
				if n in self.stack and time < self.time:
					print(n, ":", self.name)
		return
time = input("Enter available time: ")
p1 = peerLearning()
p1.addStacks()
p1.setMentorOrLearner()
p1.setAvailableTime()
p1.getMentor(stack, time)