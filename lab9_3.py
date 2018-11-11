#! /usr/bin/python3
# -*- coding: utf-8 -*-
import random

def ui_input_text() -> str:
	""" This function inputs text"""
	text = input('enter your text ')
	return text

def ui_output_text(morzeText: str):
    """ This function print result"""
    print(morzeText)

def to_morze(text: str) -> str:
	""" This function change text to morze"""

	morze = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.",
	"G":"--.","H":"....","I":"..","J":"-.-.","K":"-.-","L":".-..","M":"--",
	"N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-",
	"U":"..-","V":"...-","W":".--","X":".-..","Y":"-.--","Z":"--.."}

	textMorze = ''.join([morze.get(c.upper(), ' ') for c in text])

	return textMorze
	

ui_output_text(to_morze(ui_input_text()))
