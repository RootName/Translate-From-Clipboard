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

def translate():
	translator = Translator(to_lang="tr")
	f = open('history.txt', 'a')
	clipboard.copy("")
	while True:
		try:
			if clipboard.paste():
				word = clipboard.paste().strip()
				mean = translator.translate(word)
				subprocess.call(["notify-send.exe", 'Ceviri: %s'%(word), '%s'%(mean.lower().replace("ı", "i").replace("ü", "u").replace("ş", "s").replace("ö", "o").replace("ğ", "g").replace("ç", "c"))])
				result =  "\n[>] %s\t: %s\n"%(word, mean) + "="*70
				f.write(result)
				clipboard.copy("")
			else:
				pass
		except KeyboardInterrupt:
			f.close()
			sys.exit()
def main():
	translate()

if __name__ == "__main__":
	main()
