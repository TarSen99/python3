#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def UI_input_string() -> str:
    '''Function input string'''
    ticket_number = input("Enter ticket number ")
    ticket_number = list(ticket_number)
    return ticket_number

def UI_print_result(result: bool):
    '''prints result'''
    if result:
        print("Your ticket is lucky")
    else:
        print("Your ticket is not lucky")

def ticket_number_check(ticket_number: list) -> bool:
    '''checks if ticket is lucky'''
    ticketHalfLength = int(len(ticket_number) / 2)
    firstHalf = 0
    secondHalf = 0

    for i in range(0, ticketHalfLength):
        firstHalf += int(ticket_number[i])

    for i in range(-(ticketHalfLength), 0):
        secondHalf += int(ticket_number[i])

    if firstHalf == secondHalf:
        return True
    else:
        return False


UI_print_result(ticket_number_check(UI_input_string()))
