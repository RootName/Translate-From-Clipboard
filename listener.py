#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__ = "Black Viking"
__date__ = "10.03.2017"
__version__ = 0

from translate import Translator
import clipboard, sys, os

reload(sys)
sys.setdefaultencoding("utf-8")

espeak = "espeak -v tr \""

def main():
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
				os.system("%s %s"%(espeak, mean))
			else:
				pass
		except KeyboardInterrupt:
			f.close()
			print "\n[*] Detected CTRL+C, press Enter to continue..."
			raw_input()
			main()

if __name__ == "__main__":
	main()
