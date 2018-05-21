#Random
#Αν έχουμε ένα σύνολο στοιχείων μπορούμε με την εντολή shuffle να τα 
# αναδιατάξουμε τυχαία. Αν έχουμε 5 στοιχεία, π.χ. L=[1,2,...,5], 
# με την shuffle(L), τροποποιεί την L, π.χ. L=[2,3,1,5,4]. Φτιάξτε 
# μια τράπουλα με χρώματα ['Κούπα','Μπαστούνι','Σπαθί','Καρό'] και 
# χαρτιά τα 
# ['1','2','3','4','5','6','7','8','9','10','Βαλές','Ντάμα','Ρήγας'], 
# χρησιμοποιώντας ένα στοιχείο της πρώτης και ένα στοιχείο της 
# δεύτερης λίστας. Φτιάξτε μια συνάρτηση η οποία να ανακατεύει 
# την τράπουλα και να επιστρέφει μια λίστα με τα 3 τελευταία χαρτιά, 
# διαγράφοντας τα από την τράπουλα. Π.χ. Αν η τράπουλα deck, 
# ανακατεμένη είναι π.χ. 
# deck=['1_Μπαστούνι',...'Ρήγας_Κούπα','6_Σπαθί', 'Ντάμα_Καρό', '3_Κούπα'], 
# η συνάρτηση θα επιστρέψει τη λίστα 
# ['6_Σπαθί', 'Ντάμα_Καρό', '3_Κούπα'] 
# και το deck θα είναι deck=['1_Μπαστούνι',...'Ρήγας_Κούπα']. 
# Η εντολή pop() για λίστες επιστρέφει το τελευταίο στοιχείο της 
# λίστας, διαγράφοντας το από τη λίστα. 
# [Numpy9-cards.py]Numpy9-cards.py

import random

color=['Κούπα','Μπαστούνι','Σπαθί','Καρό']
val=['1','2','3','4','5','6','7','8','9','10','Βαλές','Ντάμα','Ρήγας']
emptyDeck = []
# class card():
# 	def __init__(self, rank, color):
# 		self.rank = rank
# 		self.color = color

class deck():
	def __init__(self, color, val, filed = False, deck = []):
		self.color = color
		self.val = val
		self.filed = filed
		self.deck = deck
		self.createDeck()
		if self.filed:
			self.createFiles('deck.txt', self.deck)

	def createFiles(self, fileName, content):
		f = open(fileName, 'w')
		for card in content:
			f.write(str(card))
			f.write('\n')
		
	def createDeck(self):
		for cardType in self.color:
			for number in self.val:
				self.deck.append('%s_%s'%(number, cardType))
		if self.filed:
			self.createFiles('deck.txt', str(self.deck))
		return self.deck

	def shuffle(self):
		random.shuffle(self.deck)
		if self.filed:
			self.createFiles('deck.txt', self.deck)
		return self.deck

	def __str__(self):
		return str(self.deck)
	
	def getPokerHand(self):
		cards = []
		for i in range(3):
			cards.append(self.deck[-1-i])
			self.deck.remove(self.deck[-1-i])
		if self.filed:
			self.createFiles('pokerHand.txt', cards)
			self.createFiles('deck.txt', self.deck)
		return cards

	def pickRandom(self, cardNum = 1):
		cards = random.sample(self.deck, cardNum)
		for i in cards:
			self.deck.remove(i)
		if self.filed:
			self.createFiles('randomCard.txt', cards)
			self.createFiles('deck.txt', self.deck)
		return cards

	def handOut(self, players = 4, cards = 7):
		self.shuffle()
		returned = []
		for i in range(players):
			playerCards = []
			for x in range(cards):
				playerCards.append(self.deck[x])
				self.deck.remove(self.deck[x])
			returned.append(playerCards)
			if self.filed:
				self.createFiles('player%s.txt'%(i+1), playerCards)
				self.createFiles('deck.txt', self.deck)
		return returned




deck1 = deck(color,val, True)
deck1.shuffle()


# def test(n):
# 	deck1 = deck(color, val)
# 	p1,p2 = deck1.handOut(2,7)

# 	#p1
# 	aces = 0
# 	for cardType in color:
# 		if str(n) + '_' + cardType in p1:
# 			aces += 1
# 	if aces == 4:
# 		return True
			
# 	#p2 
# 	aces = 0
# 	for cardType in color:
# 		if str(n) + '_' + cardType in p2:
# 			aces += 1
# 	if aces == 4:
# 		return True

# 	return False

# x = 0
# n = 1000
# for i in range(n):
# 	b = test(2)
# 	if b:
# 		x +=1

# print('%.10f %%' %((x/n)*100))


##################
#    Homework    #
##################

#  handOut() w/  dictionaries

##################

# Create the deck as a file, and player's card in another file

##################

# Έχουμε μια ανακατεμένη τράπουλα όπως πριν και θέλουμε να μοιράσουμε σε 2 
# παίκτες 7 χαρτιά (τροποποιήστε την προηγούμενη συνάρτηση ώστε να 
# επιστρέφει 2 λίστες με 7 χαρτιά). Επαναλαβεται Ν φορές ώστε να 
# υπολογίστε την πιθανότητα να έχει ο ένας από τους 2 παίκτες 4 άσσους. 

# class deckFile():
# 	def __init__(self, color, val):
# 		self.color = color
# 		self.val = val
# 		self.deck = self.createDeck()
		
# 	def createDeck(self):
# 		for cardType in self.color:
# 			for number in self.val:
# 					self.deck.append('%s_%s'%(number, cardType))
# 		f = open('deck.txt', 'w')
# 		f.write(self.deck)
# 		return self.deck

# 	def shuffle(self):
# 		random.shuffle(self.deck)
# 		f = open('deck.txt', 'w')
# 		f.write(self.deck)
# 		return self.deck

# 	def __str__(self):
# 		f = open('deck.txt', 'r')
# 		r = f.readlines()
# 		return str(r)
	
# 	def getPockerHand(self):
# 		cards = []
# 		for i in range(3):
# 			cards.append(self.deck[-1-i])
# 			self.deck.remove(self.deck[-1-i])
# 		f = open('pokerHandCards.txt', 'w')
# 		f.write(cards)
# 		return f

# 	def pickRandom(self, cardNum = 1):
# 		cards = random.sample(self.deck, cardNum)
# 		for i in cards:
# 			self.deck.remove(i)
# 		return cards

# 	def handOut(self, players = 4, cards = 7):
# 		self.shuffle()
# 		returned = []
# 		for i in range(players):
# 			playerCards = []
# 			for x in range(cards):
# 				playerCards.append(self.deck[x])
# 				self.deck.remove(self.deck[x])
# 			returned.append(playerCards)
# 			f = open('player%s.txt'%(i+1), 'w')
# 			f.write(returned[i])
# 		return returned
