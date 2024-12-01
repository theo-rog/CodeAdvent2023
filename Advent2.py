#%% Imports
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Wed Sep 25 20:55:18 2024

@author: theorogers
"""
import requests

# URL of the input
link = "https://adventofcode.com/2023/day/2/input"

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
#%% Cell 1
import re
games = response.split("\n")

def get_colours(games):
    colours = []
    for game in games:
        if game:
            game = game.split(":",1)[1]
            for game in games:
                reveals = game.split(";")
                for reveal in reveals:
                    draws = reveal.split(",")
                    for draw in draws:
                        colour = re.search(r"\d+\s+(\w+)", draw)
                        if colour:
                            colour = colour.group(1)
                            if colour not in colours:
                                colours.append(colour)
    return(colours)

colours = get_colours(games)

def get_name(game):
    if game != "":
        game_number = re.search(r"Game (\d+)", game).group(1)
        if game_number:
            return(game_number)

def find_max(game):
    game = game.split(":",1)[1]
    reveals = game.split(";")

    max_colours = {colour: 0 for colour in colours}
    
    for reveal in reveals:
        draws = reveal.split(",")
        for draw in draws:
            if draw:
                colour = re.search(r"\d+\s+(\w+)", draw).group(1)
                number = re.search(r"\d+", draw).group()
                number = int(number)
                if number > max_colours[colour]:
                    max_colours[colour] = number
    return(max_colours)

sum_numbers  = 0 
sum_powers = 0

for game in games:

    if game != "":
        max_colours = find_max(game)
        if max_colours["red"] <= 12 and max_colours["green"] <= 13 and max_colours["blue"] <= 14:
            sum_numbers += int(get_name(game))
        power = max_colours["red"] * max_colours["green"] * max_colours["blue"]
        sum_powers += power

print(sum_numbers)
print(sum_powers)

#ans1 = 2776
#ans2 = 68638


    
    