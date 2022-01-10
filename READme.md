# Wordle solver

This project contains a basic Wordle solver written in python.


[Wordle](https://www.powerlanguage.co.uk/wordle/) is a popular browser-based word game that went viral on Twitter in early January 2022. The challenge is to guess a five-letter word in as few attempts as possible. Each attempt, you are told which letters in your guess are in the target word and whether they are in the correct positions, and you have at most six attempts.

To generate the word bank, I pulled the Ubuntu [/usr/share/dict/american-english](http://manpages.ubuntu.com/manpages/bionic/man5/american-english.5.html) file and filtered out all word that were not five letters long.

