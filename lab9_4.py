#! /usr/bin/python3
# -*- coding: utf-8 -*-


def ui_input_int() -> int:
    """This function inputs int number"""
    IntNumber = input('Enter your number: ')
    return IntNumber

def ui_input_rome() -> str:
    """This function inputs rome number"""
    romeNumber = input('Enter your rome number: ')
    return romeNumber

def ui_output_number(number: str) -> None:
    """This function prints numbers"""
    print(number) 

def int_to_rome(number:int) -> str:
    """This funtion converts int to rome"""
    main = "I"*int(number)
    
    main = main.replace("I"*5, "V")
    main = main.replace("V"*2, "X")
    main = main.replace("X"*5, "L")
    main = main.replace("L"*2, "C")
    main = main.replace("C"*5, "D")
    main = main.replace("D"*2, "M")
    
    main = main.replace("DCCCC", "CM")
    main = main.replace("CCCC", "CD")
    main = main.replace("LXXXX", "XC")
    main = main.replace("XXXX", "XL")
    main = main.replace("VIIII", "IX")
    main = main.replace("IIII", "IV")
    return main

def rome_to_int(rome: str) ->str:
    """This funtion converted rome to int"""
    main = rome
    main = main.replace("I", "1 ")
    main = main.replace("V", "5 ")
    main = main.replace("X", "10 ")
    main = main.replace("L", "50 ")
    main = main.replace("C", "100 ")
    main = main.replace("D", "500 ")
    main = main.replace("M", "1000 ")
    
    main = main.replace("CM", "900 ")
    main = main.replace("CD", "400 ")
    main = main.replace("XC", "90 ")
    main = main.replace("XL", "40 ")
    main = main.replace("IX", "9 ")
    main = main.replace("IV", "4 ")
    main = main.strip()
    
    main_result = main.split(" ")
    main_result = list(map(int, main_result))
    main_result=sum(main_result)
    return main_result
      

ui_output_number(int_to_rome(ui_input_int()))
ui_output_number(rome_to_int(ui_input_rome()))
