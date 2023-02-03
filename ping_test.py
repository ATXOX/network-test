#!/usr/bin/python3

#Name: AbdullahTahir
#Date: 25/09/2022

import subprocess
import os
import time

def find_gateway():
	output= subprocess.check_output(['ip','r'])#This line will run the command ip r and get the output, the command ip r is run to find the default gateway.
	output= output.decode('utf-8')#This line decodes the output using utf-8
	for line in output.splitlines():
		if 'default' in line:#This line will search for the line that conatins the keyword default
			gateway= line.split()[2]#This line will ignore the first two words in the line and store the gateway ip
			break
	return gateway#This line returns the gateway which is the first thing left on the line after we used the split funtion 

def ping_host(host):
	ping= subprocess.check_output(['ping', '-c', '4', host])#This line will run the ping command for the provided host and stop after 4 packets are sent
	ping= ping.decode('utf-8')#This line will decode the output using utf-8
	x= 0
	for line in ping.splitlines():
		if 'packet loss' in line:#This line will search for the line that conatins the keyword packet loss
			x= line.split()[5]#This line will ignore the first 5 words so that the percentage '0%' is the first thing left and it will store that
			break
	return x#This will return the percentage of the packet loss

def ping_gateway():
	return ping_host(find_gateway())#This command will ping the gateway

def dns_test():
	return ping_host('www.google.com')#This command will ping the google

def main():
	option=0
	while option != 'q' or 'Q':
		time.sleep(4)
		os.system('clear')#This will run the clear command
		option=input('''
 ██████╗ ██████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗
██╔═══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║   ██║██████╔╝   ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║   ██║██╔═══╝    ██║   ██║██║   ██║██║╚██╗██║╚════██║
╚██████╔╝██║        ██║   ██║╚██████╔╝██║ ╚████║███████║
 ╚═════╝ ╚═╝        ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝                                                        

	1-Display gateway IP Address.
	2-Test for Gateway.
	3-Test for DNS connection.

Please enter your option or q/Q to quit the program.''')
		if option == '1':
			print ('\nYour Gateway IP address is:',find_gateway())#This line will just run the find_gateway command and show the gateway ip
		elif option == '2':
			if ping_gateway()=="0%":#This will ping the gateway and check if the packet loss is 0% or not
				print ('\nTest to Gateway works')#If this packet loss is 0% it will print this line
			else:
				print ('\nGateway is down')#If the packet loss is more than 0% it will print this line.
		elif option == '3':
			if dns_test() == '0%':#This will ping google and check if the packet loss is 0% or not
				print ('\nConnection to Google is up')#If this packet loss is 0% it will print this line
			else:
				print ('\nConnection to Google is down')#If the packet loss is more than 0% it will print this line.
		elif option == 'q' or option =='Q':
			print ('\nExiting')#If you enter q or Q and hit enter is will stop and exit the script 
			exit()
		else:
			print ('\nInvalid option. Try again')#If you enter any option that isnt shown or avaliable it will print Invalid option and it will tell the user to try again
main()
