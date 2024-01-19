# Counting_Tokens_HW0
**Input a utf8 standard text file of your choice and insert arguments in order to find the top ten most frequently occurring normalized tokens within the corpus.**

## Files / Folders
* **requirements.txt** - Contains necessary packages to run script
* **myfile.txt** - Contains utf-8 encoded text
* **normalize_text.py** - Script that returns most/least frequent tokens from text file and gives bar plot
* **stopwords.txt** - Text file of stopwords that are removed from tokens with `-w` argument
* **report.md** - Post-project report on process and learning
* **images/** - Contains images used in report

## Instructions
* Install necessary requirements found in `requirements.txt` into your environment <br>
* `$ python normalize_text.py myfile.txt --arguments` <br>
  * **myfile.txt can be replaced with any utf-8 text file of your liking**
    *   Either replace text in the myfile.txt
    *   Insert your own utf-8 .txt file and use on the command line
  * Current example myfile.txt is *The Blue Castle* by L.M. Montgomery
* This should produce a bar plot with the **top 10** token counts. <br>

## Arguments
* `'-h' '--help'` Argument help <br>
* `'-l' '--lower'` Converts corpus to lowercase. IGNORES CASE <br>
* `'-s' '--stem'` Stems corpus to root word use nltk Port Stemmer<br>
* `'-p' '--punctuation'` Punctuation is automatically removed from the text. This command reinstates punctuation as tokens <br>
* `'-w' '--stopwords'` Removes stop words from the corpus <br>
* `'-c' '--contractions'` Splits contractions into their respective parts <br>
* `'-r' '--reverse'` Gives least frequently used tokens instead of most frequent.
