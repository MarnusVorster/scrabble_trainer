# Scrabble sentence trainer
## Intro
The purpose of this tool is to do the following:
1. Accept a word or sentence of words.
2. Look for similar words from a list (corncob_lowercase.txt)
3. Return a random similar word in the original's place.

## How to use
### Windows
+ Download the latest zip file from releases.
+ Open and unzip it into **My Documents**
+ Download the word list from [here](http://www.mieliestronk.com/corncob_lowercase.txt) and place it in the same unzipped folder.
+ Open cmd.exe (Just type 'cmd' in start menu)
+ Type the following commands:  
```
cd My Documents
cd scrabble_trainer
```
+ Then type the following to run the trainer:
```
scrabble_trainer.exe "your word or sentence"
```
+ This will output the scrabbled sentence for you eg.
```
     Your sentence: lightly fried fish are delicious
Scrabbled sentence: lectors fined full ass dexterity
```

### Linux
**NB: Make sure you have Python3 installed!!!**
+ Download this repository by clicking on the green `Code` and selecting `Download ZIP`
+ Unzip it to a known location
+ Download the word list from [here](http://www.mieliestronk.com/corncob_lowercase.txt) and place it in the same unzipped folder.
+ Open a terminal and cd to the unzipped location.
+ Run the following command:
```
python main.py "your word or sentence"
```
+ This will output the scrabbled sentence for you eg.
```
     Your sentence: lightly fried fish are delicious
Scrabbled sentence: lectors fined full ass dexterity
```

### macOS
+ No executable available.
+ Follow the Linux instructions if you know what you're doing.

## Developer Notes
To create the executable do the following:
+ `pip install -r requirements_dev.txt`
+ `python setup.py py2exe`
+ This will create a folder with the name scrabble_trainer which will contain the scrabble_trainer.exe and it's required libraries.

### Tests
Run the tests by running the following:
+ `pytest tests.py` 