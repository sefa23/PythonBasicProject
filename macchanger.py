import subprocess
import optparse

print("-----------")
print("MAC CHANGER")
print("-----------")
parse_object=optparse.OptionParser()
parse_object.add_option("-i","--interface",dest="interface",help="interface help")
parse_object.add_option("-m","--mac",dest="macadres",help="New mac adress")
(user_input,argumants)=parse_object.parse_args()

user_interface=user_input.interface
user_mac=user_input.macadres

subprocess.call(["ifconfig",user_interface,"down"])
subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac])
subprocess.call(["ifconfig",user_interface,"up"])

print("Congratulation")
