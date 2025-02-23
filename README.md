# Introduction

This repository is part of my application as **Data Engineer** at _Aimigo_ (ex- _Gymglish_) and <mark style="background-color: red">should be kept private</mark>.

It should be assessed by the _Aimigo_ team on two main objectives:
- Cleaness
- Performance (rapidity of execution)

The following README explains how to run the tests used to assess the code performance. It also explains what have been done in each of the two missions.

# How to install and run the code
The code should be executed on a Linux machine and using [Python 3.11](https://www.python.org/downloads/release/python-3110/) as requested in the mission decription. 

Then, the following command can be executed in a shell:

>$ python -m venv venv && source venv/bin/activate && pip install pytest && pip install -r requirements.txt

It will create a virtual environment in which the code will be executed, activate it, install the _pytest_ package as well as all the packages included in the _requirements.txt_ file.

Once everything is setup, the tests can be runned using the command:
>$ python -m pytest _etl_a9number_v4.py

The -s option can also be added to the previous command in order to display the prifiling of the tests. It can help identify bottlenecks for instance.

# Mission 1: pdftextractor.py
The first mission given is write a script allowing the text extraction from the _etl_sample.pdf_ file. 
Accuracy is important as, in a second time, the text extrated is used in mission 2 as text input for the unitary tests.

## Current State

## Possible Improvements?

# Mission 2: count_occurrences_in_text()

## Current State

## Possible Improvements?