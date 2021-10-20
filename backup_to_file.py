import paramiko
import time
from getpass import getpass

username = 'admin15'
password = 'password'

rtr_list = open ('devices.txt')
for rtr in rtr_list:
	print('### connecting to device ' + rtr.strip() + '###\n')
	SESSION = paramiko.SSHClient()
	SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	SESSION.connect(rtr.strip(),port=22,
			username = username,
			password = password,
			look_for_keys = False,
			allow_agent = False)

	DEVICE_ACCESS = SESSION.invoke_shell()
	DEVICE_ACCESS.send(b'ter len 0\n')
	DEVICE_ACCESS.send(b'sh run\n')
	time.sleep(5)
	output = DEVICE_ACCESS.recv(65000)
	print(output.decode('ascii'))
	
	BAK_file = open('Backup_' + rtr.strip(), 'w')
	BAK_file.write(output.decode('ascii'))
	BAK_file.close
	
	SESSION.close
