# DATA

**File selected:** `myfile.txt` which serves as an example text containing *The Blue Castle* by L. M. Montgomery.
* Obtained from [Project Gutenberg]([https://www.google.com](https://www.gutenberg.org/browse/scores/top)) 
* utf-8 encoded text file
* The main character is named Valancy which is a unique name (that stems to valanc)
* There seem to be strings surrounded by underscores in the text.

# METHODOLOGY

* Used `argparse` library to be able to manipulate command-line arguments
  * Options include:
    * Lowercasing
    * Stemming
    * Stopword Removal
    * Addition/Removal of Punctuation
      > Program automatically removes punctuation. <br>
      > If `-p` argument is given, punctuation tokens will be present in the simulated graph.
      > Important for maintaining specific formats but also for potential future text segmentation (ex: "!" tends to be more associated with positives).
    * Contraction Splitting
      > Allows the user to split contractions into their respective parts <br>
      > Important for maintaining tense and negation of specific phrases
      > Ex: she'll instead of she's shows she is going vs. she is <br>
      > Ex: wouldn't instead of would shows being opposed to vs. being open to
    * Reverse Order
      > Gives least frequently used normalized tokens from the text.
    * Individual Word Selection
      > Allows the corpus to pull out the individual tokens occurring most frequently instead putting them in ranking buckets.
* Created a .txt file involving stopwords found on GitHub with hundreds of example words
* Used NLTK for PortStemmer
* Split text into tokens. Made the tokens the key values in a dictionary with their frequency counts as the values.
* Used plotly to generate plots from the given dictionary used with token, count pairs. This way plots can be generated every time the program is ran with any inputted text.
      
# SAMPLE OUTPUT

### Bucket Distribution
`$ python normalize_text.py myfile.txt -lcs`
![Top Occurring Tokens Bucketed by Ranking vs. Frequency](https://github.com/brandonowens24/NLP_HW0/blob/main/images/full_rank.png)

### Individual Top 10: Most Frequent Tokens from Sample Text
**With Stop Words** - `$ python normalize_text.py myfile.txt -li`
![Top 10 w/ Stop Words](https://github.com/brandonowens24/NLP_HW0/blob/main/images/top_ten_w_sw.png)

**Without Stop Word and with Contraction Splitting** - `$ python normalize_text.py myfile.txt -lwi`

![Top 10](https://github.com/brandonowens24/NLP_HW0/blob/main/images/top_ten_wout_sw.png)

### Individual Bottom 10: Least Frequented Tokens from Sample Text
`$ python normalize_text.py myfile.txt -lwri`
![Bottom 10](https://github.com/brandonowens24/NLP_HW0/blob/main/images/bottom_ten.png)

# DISCUSSION

### Part One
While looking at the most frequenlty occurring tokens ranked in order and bucketed via 100 tokens, the graph provided above may not signal that largest indication of exponential decay -- however, that is because the count values are in log form. Without log form, there is a significant decline from the bucket of stop words compared to other token buckets of lesser frequency ranking. When the amount of tokens in each ranking bucket is decreased (ex: from 100 to 10), this form of decay is even more apparent because some words that act as stop words are significantly more likely.  <br>

Originally, upon using my program with just the lowercase parameter, all top ten words were stop words. After adjusting for this and using my stop word argument, a majority of the top ten words (for multiple texts) became nouns! This was surprising, as I was expecting that the removal of the stopword parameter would cause there to be a large amount of verbs; however, upon thought it makes sense because usually the repetition of descriptive words and actions wears them out. Meanwhile, the bottom words on my list just happened to be ten tokens that were only used a single time. There were plenty more tokens that were also only used a single time -- however, the program only selected ten of them so these words could have been different. With that being said, these words, for the most part, are either unique verbs or adjectives.<br>

Compared to Zipf's law (stating that the most common word occurs about n times the nth most common one), my sample text doesn't really follow this sentiment with the inclusion of stopwords from an individual word perspective. Instead it almost looks like the top ten words are linearly decreasing. If I increase the parameter of tokens to be read to be higher, I wonder if this would model more accurate. When the model is used with the ranking system on the x-axis, Zipf's law is much more noticeable as the most frequent words are exponentially more likely to appear than the least frequent. Additionally, the levelling off occurs around 2, which is log10(100) and this makes sense because the least occurring words are occurring only once. If buckets were marginalized, this exponential decay would approach zero, but never go under one.<br>

When sampling other texts, like *Moby-Dick*, the inclusion of stopwords actually modelled Zipf's law even better! An additional idea for this discrepancy may be that *Moby-Dick* is about 4x as long as my sample text so that the larger the count of tokens to sample, the more a text will fit into the model.


### Part Two
Upon completing this assignment, I learned many new things. My programming background is pretty lackluster coming from the field of medicine. I was able to work on my Python skills and familiarize myself with the argparse, nltk, and plotly libraries. The most interesting to me was the argparse library, as I didn't know that I didn't have to manually use sys to install command-line arguments. In terms of NLP, I was able to learn methods of how stopwords can be removed and gained experience with some (relatively simple) regex strings and stemming. One challenge I faced during this experience was ordering the arguments that were passed in -- for example, if my punctuation removal argument was before my contractions argument in the code, there wouldn't be any contractions to separate. Additionally, I wanted punctuation to be their own strings; therefore, splitting the text on punctuation early and the putting the tokens into a list with the punctuation being separated by spaces was immensely helpful.  Professor Wilson also taught us about the set() function, which I didn't know existed but greatly sped up my program -- although I could definitely optimize more if I had the time. Lastly, as silly as it sounds, I familiarized myself more with Git and markdown -- things I was lacking experience in. Outside of things I felt like I gained understanding in, I think it would be beneficial to work on optimizing the speed at which my programs can operate in the future.

      


