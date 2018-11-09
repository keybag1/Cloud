from flask import Flask
import psutil
import socket

app = Flask(__name__)

@app.route('/')
def SysDetails():
	hostname = socket.gethostname()
	host_ip = socket.gethostbyname(hostname)
	cpus = psutil.cpu_count()
	mem = psutil.virtual_memory().total
	return '''{
		hostname : %s
		ip address : %s
		cpus : %s
		memory : %s
		}'''%(hostname,host_ip,cpus,mem)

