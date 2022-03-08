class Player:

  def __init__(self, score, percent, totalQuestions):
    self.score = score
    self.percent = percent
    self.totalQuestions = totalQuestions

  def getScore(self):
    return self.score

  def setScore(self, score):
    self.score = score

  def getPercent(self):
    return self.percent

  def setPercent(self, percent):
    self.percent = percent

  def getTotalQuestions(self):
    return self.totalQuestions

  def setTotalQuestions(self, totalQuestions):
    self.totalQuestions = totalQuestions
