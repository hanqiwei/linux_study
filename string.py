#! /usr/bin/python
#-*- codeing: UTF-8 -*-

# 1. Display the blackboard ------------------------------------
#~ sentence = raw_input("Sentence:")
#~ text_width = len(sentence)
#~ box_width = text_width + 2
#~ 
#~ print ' ' + '+' + '-' * box_width + '+'
#~ print ' ' + '|' + ' ' * box_width + '|'
#~ print ' ' + '|' + ' ' + sentence + ' ' + '|'
#~ print ' ' + '|' + ' ' * box_width + '|'
#~ print ' ' + '+' + '-' * box_width + '+'


#~ #2.check the username ------------------------------------
#~ users = ['tom','jack','hanqiwei']
#~ username = raw_input('Enter your useranme: ')
#~ if username in users :
	#~ print 'Hello, ' + username
#~ else :
	#~ print 'Sorry, ' + username + ' no exist!'
	
#3.checkout the usrname and password ------------------------------------
#~ database = [['lining','ln123456'],['zhangjie','zj123456'],['hanqiwei','hqw123456'],['tom','tom123456'],['jack','jack123456']]
#~ username = raw_input('UseName: ')
#~ password = raw_input('PassWord: ')
#~ if[username,password] in database :
	#~ print 'Hello, ' + username
#~ else :
	#~ print 'Sorry, ' + username + ' no exist!'

	
#4. ------------------------------------
#~ template = '''	<html> 
	#~ <head><title>%(title)s</title></head> 
	#~ <body> 
	#~ <h1>%(title)s</h1> 
	#~ <p>%(text)s<p>
	#~ </body>'''
#~ data = {'title':'My Home Page','text':'Welcome to my home page!'}
#~ print template % data

#5.-------------------------------------

#~ width = input('Please enter width: ')
#~ price_width = 20
#~ item_width = width - price_width
#~ header_format = '%-*s%*s'
#~ format = '%-*s%*.1f'
#~ print '=' * width
#~ print header_format % (item_width,'Item',price_width,'Price')
#~ print '-' * width
#~
#~ print format % (item_width,'Apples',price_width,0.42)
#~ print format % (item_width,'Pears',price_width,0.56)
#~ print format % (item_width,'Cantaloupes',price_width,1.92)
#~ print format % (item_width,'Dried Apricots',price_width,8.3)
#~ print format % (item_width,'Prunes',price_width,12.34)
#~
#~ print '=' * width

#6.-------------------------------------
#~ name = raw_input('What is your name? ')
#~ if name.endswith('Gumby'):
	#~ print 'Hello, ' + name
#~ else :
	#~ print 'Hei ...'

#7.-------------------------------------
#~ x = 1
#~ while x <= 100:
	#~ print x
	#~ x = x + 1

#~ name = ''
#~ count = 4
#~ basedata = ['hanqiwei','lining']
#~ while count and not name in basedata:
	#~ name = raw_input('Please input your name:')
	#~ count = count - 1
	#~ if not name in basedata:
		#~ print 'you have ' + str(count) + ' times'
#~ if not count:
	#~ print 'Sorry, Please try again!'
#~ else:
	#~ print 'Hello, ' + name

#~ #8.-------------------------------------
#~ name = ['Lining','Wenzhang','Hanqiwei','Liudehua']
#~ age = [29,34,27,45]
#~ format = '%-*s%*s'
#~
#~ for i in range(len(name)):
	#~ print format % (20,name[i],20,age[i])

#9.--------------------------------------------
#~ a = [1,2]
#~ number = input('Input the lenth: ')
#~ for i in range(number):
	#~ a.append(a[-1] + a[-2])
#~ print a

#10.-------------------------------------------
#~ def hello(name):
	#~ return 'Hello, ' + name + '!'
#~
#~ def fibs(num):
	#~ ''' xx ,this is a test, note: add the remark '''
	#~ result = [0,1]
	#~ for i in range(num - 2):
		#~ result.append(result[-1] + result[-2])
	#~ return result
#~
#~ print hello('World')
#~ print hello('Gumby')
#~ num_fibs = input('How many numbers do you want? -> ')
#~ print fibs(num_fibs)
#~ print fibs.__doc__

#11.-------------------------------------------
#~ def print_info(name='Nobody', age=24):
	#~ print 'Name: ', name
	#~ print 'Age: ', age
	#~ return
	#~
#~ print_info(name='HanQiwei',age=50)
#~ print_info(age = 50)
#~ print_info(name = 'Magnus')
#~ print_info()

#12.-------------------------------------------
#~ __metaclass__ = type
#~ class Person:
	#~ def setName(self, name):
		#~ self.name = name
	#~ def getName(self):
		#~ return self.name
	#~ def greet(self):
		#~ print "Hello,world! I'm %s" % self.name
#~
#~ foo = Person()
#~ bar = Person()
#~ foo.setName('Luke Skywalker')
#~ bar.setName('Anakin Skywalker')
#~ foo.greet()
#~ bar.greet()

#13.-------------------------------------------
#~ try:
	#~ fd = open("test_file", "r+")
	#~ fd.write("This is my test file for exception handling!\n")
#~ except IOError:
	#~ print "Error:can't find file or Read/Write data!"
#~ else:
	#~ print "Written content in the file successfully"

#14.--------------------------------------------
from Tkinter import *

root = Tk()

name  = ["Li xiaolong","Chen baiqiang","Jiang zeming","Hu jingtao","Mao zedong","Ma kesi"]
listb1 = Listbox(root)
for item in name:
	print 'item: ', item
	listb1.insert(len(name)-1,item)
listb1.pack()
root.mainloop()

	
