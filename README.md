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
The current _extract_text()_ script make use of the [PyMuPdf](https://pymupdf.readthedocs.io/en/latest/) library. 

It reads and extracts the text from the .pdf file given as argument.
The script then splits the text on all newline markers (\n) and removes all lines starting by "Figure" and the lines being digits.
Then all the lines are joined, followed by the pages being joined altogether. 
Finally spaces are added after punctuation in order to improve readability.

**NB.** _LIGATURES:_ It worth noting that the flags in the _get_text()_ method are modified in order to remove ligatures. By default, PyMuPdf keeps ligatures as in the PDF. 
For instance, the ligature "ﬀ" would be kept as is in the extracted text instead of "ff", potentially leading to processing issues after extraction.

## Possible Improvements?
The _extract_text()_ script could possibly be improved by reducing the overhead induced by the library. 
PyMuPdf has a lot to offer and offers a lot of features yet, in this particular case, only the _get_text()_ method is used for each page. It could be possible to have a lower access to the text in order to gain in performance.

Making use of publicly available **LLMs** such as [OpenAI's models](https://platform.openai.com/docs/models) or [Google's models](https://ai.google.dev/gemini-api/docs/models/gemini) throught respective API could help improve accuracy. 
This has the downsides of **adding costs** depending on the number of PDF files processed as well as probably **reducing overall performances**. 
It relies also on a third party, possibly raising **reliability concerns**.
# Mission 2: count_occurrences_in_text()
Mission 2 focuses on writing the _count_occurrences_in_text()_ function. This function should execute as fast as possible and pass all the unitary tests.
## Current State
At the moment, the most efficient way found is to use a single regular expression. 

The unitary tests are quite a challenge to satisfy, ensuring a robust function. 

Before selecting this regex, several ideas have been tested, including a chunking strategy.
The idea was to breakdown large texts into their sentences or groups of sentences in order to process them independately. 

Using the [NLTK](https://www.nltk.org/) package and the _tokenize_ module slowed the process a lot. The idea was to break the text into sentences without having issues with abreviated text such as "c.v." for instance.
With poor results, a better performing solution was used using a _custom_split()_ function.

Using **Multiprocessing** or **Pandas**, the initialization of the modules were so high that, on these texts the performances were significantly worse. 

Also, a **double pointer** idea was tested without success. The goal was to outperform the regex.

## Possible Improvements?
Using a better formatted input text could be a possibility. Here, the unit tests are a challenge to process because of a lack of unity in the input format (missing blank spaces, no newline markers or poorly formated...)

Suggestions regarding performance improvments are welcome.

Thanks for reading this README.
