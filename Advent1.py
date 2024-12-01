#%% Imports
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Wed Sep 25 20:55:18 2024

@author: theorogers
"""
import requests

# URL of the input
link = "https://adventofcode.com/2023/day/1/input"

# My session cookie
session_cookie = "53616c7465645f5f516b2a5a99c26dc35e629ff4e89c2852b79c276c3031e7f5ca1df084c4ed2e6e83d92f87a676c56d34b0d46fcb6210000dd762b499429ee7"

# Pass the session cookie as a dictionary
cookies = {
    'session': session_cookie
}

# Get request to fetch the input
response = requests.get(link, cookies=cookies)

response = response.content.decode('utf-8')
response = str(response)






#%% Processing

lines = response.split("\n")


def find_unit(line):
    digit_present = False
    unit = None
    digit_index = None
    for index, char in enumerate(line[::-1]):
        if char.isdigit():
            unit = char
            digit_present = True
            break
        else:
            pass
    return(unit,digit_present)

def find_tens_unit(line):
    two_digit = False
    tens_unit = None
    for char in line:
        if char.isdigit():
            tens_unit = char
            break
        else:
            pass
    return(tens_unit)


sum = 0 
for line in lines:
    print(f"Line: {line}")
    #line = word2digit(line)


    unit,digit_present = find_unit(line)
    
    if digit_present:

        
        tens_unit = find_tens_unit(line)
             
        value = 10 * int(tens_unit) + int(unit)

            
        print(f"Value: {value}\n")
        sum += value

print(sum)

#Ans = 54877

#%% With Word2Digit (1.2)
import re

word_digit_map = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

def word2digit(string):
    for word in word_digit_map:
        replacement = word + word_digit_map[word] + word 
        # "One" becomes "one1one" as to not interfere with characters that pre or proceed it, like in "oneeight"
        if word in string:
            string = string.replace(word,replacement)
    return(string)

example_string = "threemqfptponesevendbjs17"

sum = 0 
for line in lines:
    print(f"Line: {line}")
    line = word2digit(line)


    unit,digit_present = find_unit(line)
    
    if digit_present:

        
        tens_unit = find_tens_unit(line)
             
        value = 10 * int(tens_unit) + int(unit)

            
        print(f"Value: {value}\n")
        sum += value

print(sum)
