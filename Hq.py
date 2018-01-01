try:
	import Image
except ImportError:
	from PIL import Image
import pytesseract
import pyscreenshot
import time
import webbrowser
import requests
from bs4 import BeautifulSoup

#Gathering the Question

if __name__ == "__main__":
	Question = pyscreenshot.grab(bbox=(100,200,600,400)) #left,top,right,bottom
	Question.show()
	Question.save("Question.png")
	Question = pytesseract.image_to_string(Image.open('Question.png'))
	print(Question)

#Gathering Answer1

if __name__ == "__main__":
	Answer1 = pyscreenshot.grab(bbox=(100,400,600,500)) #left,top,right,bottom
	#Answer1.show()
	Answer1.save("Answer1.png")
	Answer1 = pytesseract.image_to_string(Image.open('Answer1.png'))
	print(Answer1)

#Gathering Answer2

if __name__ == "__main__":
	Answer2 = pyscreenshot.grab(bbox=(100,500,600,600)) #left,top,right,bottom
	#Answer2.show()
	Answer2.save("Answer2.png")
	Answer2 = pytesseract.image_to_string(Image.open('Answer2.png'))
	print(Answer2)

#Gathering Answer3

if __name__ == "__main__":
	Answer3 = pyscreenshot.grab(bbox=(100,600,600,700)) #left,top,right,bottom
	#Answer3.show()
	Answer3.save("Answer3.png")
	Answer3 = pytesseract.image_to_string(Image.open('Answer3.png'))
	print(Answer3)

#Answer 1 result count
if __name__ == "__main__":
	page = requests.get("https://www.google.com/search?q=" + Question + "'" + Answer1 + "'")
	#print(page.status_code)
	soup = BeautifulSoup(page.content, 'html.parser')
	for row1 in soup.find_all('div',attrs={"class" : "sd"}):
		continue
		#^^^Google result amount row1.text
		#print(row1.text)
	for row6 in soup.find_all('body',attrs={'class' : 'hsrp'}):
		continue
		#print(row6.text.encode('utf-8'))
	s = row6.text
	sb = Answer1
	results1 = 0
	sub_len = len(sb)
	for i in range(len(s)):
   		if s[i:i+sub_len] == sb:
       			results1 += 1
	print('{}: {} and {} mentions'.format(Answer1, row1.text, results1))


#Answer 2 result count
if __name__ == "__main__":
	page = requests.get("https://www.google.com/search?q=" + Question + "'" + Answer2 + "'")
	#print(page.status_code)
	soup = BeautifulSoup(page.content, 'html.parser')
	for row2 in soup.find_all('div',attrs={"class" : "sd"}):
		#^^^Google result amount row1.text
		#print(row2.text)
		for row6 in soup.find_all('body',attrs={'class' : 'hsrp'}):
		#print(row6.text.encode('utf-8'))
			s = row6.text
	sb = Answer2
	results2 = 0
	sub_len = len(sb)
	for i in range(len(s)):
   		if s[i:i+sub_len] == sb:
       			results2 += 1
	print('{}: {} and {} mentions'.format(Answer2, row2.text, results2))


#Answer 3 result count
if __name__ == "__main__":
	page = requests.get("https://www.google.com/search?q=" + Question + "'" + Answer3 + "'")
	#print(page.status_code)
	soup = BeautifulSoup(page.content, 'html.parser')
	for row3 in soup.find_all('div',attrs={"class" : "sd"}):
		#^^^Google result amount row1.text
		#print(row3.text)
		for row6 in soup.find_all('body',attrs={'class' : 'hsrp'}):
		#print(row6.text.encode('utf-8'))
			s = row6.text
	sb = Answer3
	results3 = 0
	sub_len = len(sb)
	for i in range(len(s)):
   		if s[i:i+sub_len] == sb:
       			results3 += 1
	print('{}: {} and {} mentions'.format(Answer3, row3.text, results3))


#Main keyword
if __name__ == "__main__":
	page = requests.get("https://www.google.com/search?q=" + Question)
	#print(page.status_code)
	soup = BeautifulSoup(page.content, 'html.parser')
	for row4 in soup.find_all('span',attrs={"class" : "_m3b"}):
		print("\nGoogle says it's: " + row4.text)
	for row5 in soup.find_all('div',attrs={"class" : "_Oqb"}):
		print("\nGoogle says it's:" + row5.text)
	if results1 > results2 and results1 > results3:
		print('\nBest choice {}'.format(Answer1))
	elif results2 > results1 or results2 > results3:
		print('\nBest choice {}'.format(Answer2))
	elif results1 == results2 and results2 == results3 and results1 == results3:
		print('\nNo best choice, sorry')
	else:
		print('\nBest choice {}'.format(Answer3))





