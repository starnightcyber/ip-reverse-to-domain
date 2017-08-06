#!/usr/bin/env python
# Reverse IP Lookup By: Joinse7en
# Modified by : starnight_cyber@foxmail.com

import urllib2, urllib, sys, json
from optparse import OptionParser
import time

# Terminal Colors

class bc:
    P = '\033[95m' # purple
    B = '\033[94m' # Blue
    G = '\033[92m' # Green
    Y = '\033[93m' # Yellow
    R = '\033[91m' # Red
    ENDC = '\033[0m' # end colors


if sys.platform == 'win32':
	bc.P = ''
	bc.B = ''
	bc.G = ''
	bc.Y = ''
	bc.R = ''
	bc.ENDC = ''

# End of terminal colors


url = "http://domains.yougetsignal.com/domains.php"

contenttype = "application/x-www-form-urlencoded; charset=UTF-8"

def banner():
	print bc.B +\
"""+-----------------------------------+
|         Reverse IP Lookup         |
|           By: Joinse7en           |
+-----------------------------------+""" + bc.ENDC


def request(target, httpsproxy=None, useragent=None):
	global contenttype

	if not useragent:
		useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:54.0) Gecko/20100101 Firefox/54.0"
	else:
		print "["+ bc.G + "+" + bc.ENDC + "] User-Agent: " + useragent

	if httpsproxy:
		print "["+ bc.G + "+" + bc.ENDC + "] Proxy: " + httpsproxy + "\n"
		opener = urllib2.build_opener(
                urllib2.HTTPHandler(),
                urllib2.HTTPSHandler(),
                urllib2.ProxyHandler({'http': 'http://' + httpsproxy}))
		urllib2.install_opener(opener)

	postdata = [('remoteAddress',target),('key','')]
	postdata = urllib.urlencode(postdata)

	request = urllib2.Request(url, postdata)

	request.add_header("Content-type", contenttype)
	request.add_header("User-Agent", useragent)
	try:
		result = urllib2.urlopen(request).read()
	except urllib2.HTTPError, e:
		print "Error: " + e.code
	except urllib2.URLError, e:
		print "Error: " + e.args

	obj = json.loads(result)
	return obj


# format json data for output
def output(obj):
	print bc.B + "Status:    " +bc.ENDC + obj["status"]
	if obj["status"] == "Fail":
		message = obj["message"].split(". ")
		print bc.R + "Error:     " + bc.ENDC + message[0] + "."
		sys.exit(1)

	print bc.B+ "Domains:   " +bc.ENDC+ obj["domainCount"]
	print bc.B+ "Target:    " +bc.ENDC+ obj["remoteAddress"]
	print bc.B+ "Target IP: " +bc.ENDC+ obj["remoteIpAddress"]

	print "\n" + bc.P + "Results:" + bc.ENDC

	for domain, hl in obj["domainArray"]:
		print bc.G + domain + bc.ENDC

fr = open(sys.argv[1], 'r')
fw = open('ip-reverse-domain-info.txt', 'w')

def main():

	index = 0

	if len(sys.argv) != 2:
		print 'Usage : reverse_ip_batch.py <ip_src_file>'
		exit(-1)

	banner()
	fw.write('----------------------------------------\n')

	for target in fr:
		print '\n------------------------------------------'
		index += 1
		print '[%d] - %s' % (index, target)
		fw.write('[%d] - %s' % (index, target) + '\n')

		# sleep 3 seconds for not to put too much pressure on the server
		time.sleep(3)
		obj = request(target.strip())			# request
		print obj

		# check whether there is a domain reverse to that ip address
		if obj['domainCount'] != '0':
			output(obj)
			for domain, hl in obj["domainArray"]:
				fw.write(domain + '\n')
		else:
			print obj
			fw.write('None\n')
		fw.write('----------------------------------------\n\n')


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "["+ bc.R + "!" + bc.ENDC + "] KeyboardInterrupt detected!\nGoodbye..."
		sys.exit()
	finally:					# close file, anyway
		fr.close()
		fw.close()