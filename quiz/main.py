from qcm import QCM
from player import Player

print('*******QUIZ PYTHON DE 10 QUESTIONS*******')

player = Player(0, 0, 10)

def createQuestion(question, answer, playerScore):
  print('\n-----------------------------------------\n')
  playerChoice = input(question)
  if playerChoice.lower() == answer:
    playerScore += 1
    print('Bonne réponse !')
  else:
    print('Mauvaise réponse !')
  return playerScore

# Question 1
question1 = 'Question 1 : En quel langage a été codé ce programme ? \nA : Python \nB : C \nC : Java \nD : C++ \nVotre réponse : '
qcm1 = QCM(question1, 'a')
playerScore = createQuestion(qcm1.getQuestion(), qcm1.getAnswer(), player.getScore())
if (playerScore != player.getScore()):
  player.setScore(playerScore)

# Question 2
question2 = 'Question 2 : Quel était la deadline de ce programme ? \nA : Lundi \nB : Mardi \nC : Mercredi \nD : Jeudi \nVotre réponse : '
qcm2 = QCM(question2, 'b')
playerScore = createQuestion(qcm2.getQuestion(), qcm2.getAnswer(), player.getScore())
if (playerScore != player.getScore()):
  player.setScore(playerScore)

# Question 3
question3 = 'Question 3 : En quel année est sortie la première version de python ? \nA : 1991 \nB : 1992 \nC : 1993 \nD : 1994 \nVotre réponse : '
qcm3 = QCM(question3, 'a')
playerScore = createQuestion(qcm3.getQuestion(), qcm3.getAnswer(), player.getScore())
if (playerScore != player.getScore()):
  player.setScore(playerScore)

# Question 4
question4 = 'Question 4 : Quel est la dernière version actuelle de python ? \nA : 3.0.0 \nB : 3.10.1 \nC : 3.10.2 \nD : 3.10.3 \nVotre réponse : '
qcm4 = QCM(question4, 'c')
playerScore = createQuestion(qcm4.getQuestion(), qcm4.getAnswer(), player.getScore())
if (playerScore != player.getScore()):
  player.setScore(playerScore)

# Question 5
question5 = 'Question 5 : Python est un langage ? \nA : Machine \nB : Interpreté \nC : Compilé \nD : Binaire \nVotre réponse : '
qcm5 = QCM(question5, 'b')
playerScore = createQuestion(qcm5.getQuestion(), qcm5.getAnswer(), player.getScore())
if (playerScore != player.getScore()):
  player.setScore(playerScore)

# Question 6
question6 = 'Question 6 : Quel est le type de donnée pour un caractère en python ? \nA : Chr \nB : Char \nC : Character \nD : Python ne possède aucun type de données pour les caractères \nVotre réponse : '
qcm6 = QCM(question6, 'd')
playerScore = createQuestion(qcm6.getQuestion(), qcm6.getAnswer(), player.getScore())
if (playerScore != player.getScore()):
  player.setScore(playerScore)

# Question 7
question7 = 'Question 7 : Récemment Python a feté ces ? \nA : 20 ans \nB : 30 ans \nC : 25 ans \nD : 35 ans \nVotre réponse : '
qcm7 = QCM(question7, 'b')
playerScore = createQuestion(qcm7.getQuestion(), qcm7.getAnswer(), player.getScore())
if (playerScore != player.getScore()):
  player.setScore(playerScore)

# Question 8
question8 = 'Question 8 : Quel est la bonne synthaxe pour charger un module ? \nA : include math \nB : import math \nC : #include math.h \nD : using math \nVotre réponse : '
qcm8 = QCM(question8, 'b')
playerScore = createQuestion(qcm8.getQuestion(), qcm8.getAnswer(), player.getScore())
if (playerScore != player.getScore()):
  player.setScore(playerScore)

# Question 9
question9 = 'Question 9 : Lequel des mots-clés suivants est un espace réservé pour le corp d’une fonction ? \nA : pass \nB : body \nC : continue \nD : break \nVotre réponse : '
qcm9 = QCM(question9, 'a')
playerScore = createQuestion(qcm9.getQuestion(), qcm9.getAnswer(), player.getScore())
if (playerScore != player.getScore()):
  player.setScore(playerScore)

# Question 10
question10 = 'Question 10 : Laquelle des affirmations suivantes est vraie ? \nA : Python est un langage de programmation de haut niveau \nB : Python est un langage interprété \nC : Python est un langage orienté objet \nD : Tout les réponses sont vrais \nVotre réponse : '
qcm10 = QCM(question10, 'd')
playerScore = createQuestion(qcm10.getQuestion(), qcm10.getAnswer(), player.getScore())
if (playerScore != player.getScore()):
  player.setScore(playerScore)

# Affichage final
print('\n-----------------------------------------\n')
print(f"Merci d'avoir jouer a mon jeu, votre score est de : {player.getScore()}/{player.getTotalQuestions()}")
player.setPercent(round((player.getScore() / player.getTotalQuestions()) * 100))
print(f"Votre pourcentage de bonnes réponses est de : {player.getPercent()}%")
