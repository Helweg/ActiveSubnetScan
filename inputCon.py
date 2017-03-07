import xmltodict

try:
	with open('input.txt') as fd:
		doc = xmltodict.parse(fd.read())
		fo = open('output.txt','w')
		for host in doc['nmaprun']['host']:
			fo.write( host['address'][0]['@addr']+' '+ host['address'][1]['@addr']+'\n')

		fo.close()
		fd.close()
except:
	pass