#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__ = "10.03.2017"
__version__ = 0

from translate import Translator
import clipboard, sys, subprocess, os

reload(sys)
sys.setdefaultencoding("utf-8")

espeak = "espeak -v tr \""

def translate(type):
	def sendResult(title, message, x):
		if x == "1":
			os.system("%s %s"%(espeak, message))
		elif x == "2":
			subprocess.call(["notify-send.exe", 'Ceviri: %s'%(title), '%s'%(message.lower().replace("ı", "i").replace("ü", "u").replace("ş", "s").replace("ö", "o").replace("ğ", "g"))])

	translator = Translator(to_lang="tr")
	f = open('history.txt', 'a')
	clipboard.copy("")
	print "\n[+] Listener started!"
	while True:
		try:
			if clipboard.paste():
				word = clipboard.paste().strip()
				mean = translator.translate(word)
				result =  "\n[>] %s\t: %s\n"%(word, mean) + "="*70
				f.write(result)
				print result
				clipboard.copy("")
				sendResult(word, mean, type)
			else:
				pass
		except KeyboardInterrupt:
			f.close()
			print "\n[*] Detected CTRL+C, press Enter to continue..."
			raw_input()
			main()

def main():
	type = raw_input("[-] 1. Text To Speech\n[-] 2. Notification\n[-] --> ")
	translate(type) if int(type) < 3 else sys.exit()

if __name__ == "__main__":
	main()
