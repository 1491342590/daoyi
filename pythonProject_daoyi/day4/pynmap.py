import nmap

nm = nmap.PortScanner()

nm.scan('127.0.0.1','80','-sV')
commd = nm.command_line()

print(commd)