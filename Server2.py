#A server application that receives messages from multi clients. 

from socket import *
import threading
from time import ctime

users = {
        'baris': '12345',
        'anil': '12345', 
        'metin': 'salak'
}

questions={
	'0Question: Dick Van Dyke played in Mary Poppins':'y',
	'1Question: Is there a pencil type named Ticonderoga No.2':'y',
	'2Question: Coca-Cola has always been brown':'y',
	'3Question: Are plastic plants made of plastic':'y',
	'4Question: Is Olive Garden a French restaurant':'n',
	'5Question: Pokemon is partially owned by Sega':'n',
	'6Question: Is sour cream the only food that doesnt spoil':'n',
	'7Question: Lachanophobia is the fear of height':'n',
	'8Question: Disney made a movie named Antz':'n',
	'9uestion: Is Bill Gates a founder of Microsoft':'y',
	'Z':'Z'
}

grades={}
	

class ThreadedServer():


    def listenToClient(self, client, addr):
	client.send("Press 1 to Sign Up, Press 2 to Sign In: ")
	message = client.recv(1024)
	if message=='1':
		client.send("Enter username and password: ")
		message = client.recv(1024)
		mes=message.split()
		users.update({mes[0]:mes[1]})
	username='failed'
	password='failed'
	while(username=='failed' and password=='failed'):
		client.send("Enter your username/password: ")
        	message = client.recv(1024)
		mes=message.split()		
		if mes[0] in users and mes[1]==users[mes[0]]:
			username=mes[0]
			password=mes[1]
		else:
			client.send("Invalid Username/Password")

        print (username+" Succesfully Logged In")

        if mes == "exit":
            print addr, " is closed"
            client.close()
            exit(0)
        else:
	    count=1
	    n=10
	    score=0
	    for i in sorted(questions.keys()):
		if count>n:
			break
		else:
			client.send(i)	
			mes2 = client.recv(1024)
			if mes2==questions[i]:
				score+=10
				print(username+" answered correct and gained 10 points. Current score: "+str(score))	
			else:
				print(username+" answered false. Current score: "+str(score))	
			
			count+=1
	grades.update({username:score})
	print(grades.items())
	
	

		


    def __init__(self,serverPort):

        try:
            serverSocket=socket(AF_INET,SOCK_STREAM)

        except:
    
            print "Socket cannot be created!!!"
            exit(1)
            
        print "Socket is created..."

        try:
            serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except:
    
            print "Socket cannot be used!!!"
            exit(1)

        print "Socket is being used..."

        try:
            serverSocket.bind(('',serverPort))
        except:
        
            print "Binding cannot de done!!!"
            exit(1)

        print "Binding is done..."

        try:
            serverSocket.listen(45)
        except:
    
            print "Server cannot listen!!!"
            exit(1)

        print "The server is ready to receive"


        while True:

            connectionSocket,addr=serverSocket.accept()
            
            threading.Thread(target = self.listenToClient,args = (connectionSocket,addr)).start()
            

if __name__=="__main__":
    serverPort=12000
    ThreadedServer(serverPort)
