#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__   = "28.03.2017"

import sys, os
import androidhelper

reload(sys)
sys.setdefaultencoding("utf-8")

droid = androidhelper.Android()
fileName = "/sdcard/history.txt"

try:
	from translate import Translator
except ImportError:
	print "[-] Çeviri için gerekli olan 'translate' modülü bulunamadı"!
	if raw_input("[?] Yüklensin mi? [Y/n] ==> ").lower() == "y"
		module()
	else:
		sys.exit()

def module():
	os.system(sys.executable+" "+sys.prefix+"/bin/"+"pip install %s"%("translate"))
	from translate import Translator

def translate(word):
	translator = Translator(to_lang="tr")
	mean = translator.translate(word.strip())
	droid.makeToast("[>] %s: %s"%(word.strip(), mean))
	return mean

def main():
	os.system("clear")
	droid.setClipboard("")

	try:
		file = open(fileName, "a")
		print "[>] File opened, %s"%(fileName)
		f = True
	except Exception as error:
		print "[!] Error: %s"%(error)
		f = False

	print "[>] Listener started!\n"+"-"*40
	droid.makeToast("[>] Listener Started!")

	while True:
		if droid.getClipboard().result != "":
			word = droid.getClipboard().result
			droid.setClipboard("")
			mean = translate(word)
			if mean:
				result = "[>] %s: %s"%(word, mean)
				print result
				droid.makeToast(result)
				if f == False:
					pass
				else:
					file.write(result+"\n")
					file.flush()
			else:
				pass
		else:
			pass

def start():
	try:
		main()
	except Exception as Error:
		droid.makeToast("[!] ERROR: %s"%(Error))
		print "[!] ERROR: %s"%(Error)
		print "-"*40
		raw_input("Press 'Enter' to continue...")
		start()

if __name__ == "__main__":
	start()
