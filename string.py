#! /usr/bin/python

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

width = input('Please enter width: ')
price_width = 10
header_format = '%-*s%*s'
print '=' * width
print header_format % (25,'Item',25,'Price')

	
