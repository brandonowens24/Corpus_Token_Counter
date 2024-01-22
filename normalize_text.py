import argparse, re
from nltk.stem import PorterStemmer
import plotly.express as px
import pandas as pd
import numpy as np

N = 10

def from_arguments():
    parser = argparse.ArgumentParser()

    # Establish command line arguments
    parser.add_argument("filename", type=str, help="Your Text File to be Normalized")
    parser.add_argument("-l", "--lower", action="store_true", help="Converts Text to Lowercase")
    parser.add_argument("-s", "--stem", action="store_true", help="Stems text to affix to suffixes, prefixes, or the word root")
    parser.add_argument("-p", "--punctuation", action="store_false", help="Punctuation and special characters are automatically removed. This command reinstates punctuation while creating tokens")
    parser.add_argument("-w", "--stopwords", action="store_true", help="Removes stop-words from text")
    parser.add_argument("-c", "--contractions", action="store_true", help="Splits contractions into their respective parts")
    parser.add_argument("-i", "--individual", action="store_true", help="Gives a plot with the top 10 most used tokens on the x-axis and their frequencies on the y-axis")
    parser.add_argument("-r", "--reverse", action="store_false", help="Gives the last N most common tokens from the text file")
    args = parser.parse_args()

    return args

# Applies arguments to create list of augmented tokens.
def edit_corpus(args):
    if not args.filename.endswith('.txt'):
        return exit("Error: The inserted file must be a text file.")
    
    with open(args.filename, 'r', encoding="utf8") as file:
        text = file.read()
        text = re.sub(r'\’', '\'', text)

    # Change text to lowercase    
    if args.lower:
        text = text.lower()

    # Splits contractions up
    # UTF 8 uses ’ instead of '
    if args.contractions:
        contraction_dict = {"'m": "am", "'ll": "will", "'d": "would", "'ve": "have", "'re": "are", "'s": "is", "n't": "not"}

        for contraction, fullword in contraction_dict.items():
            text = text.replace(contraction, ' ' + fullword)

    # Space out text for argument manipulation
    tokens = re.findall(r'[\w\']+|[^\s\w]+', text)
    text = ' '.join(tokens)

    # Removes stopwords from text
    # List obtained from: GitHub https://gist.github.com/sebleier/554280
    if args.stopwords:
        with open("stopwords.txt") as f:
            stopwords = f.read().splitlines()
            stopwords = set(stopwords)
        tokens = [tok for tok in text.split() if tok.lower() not in stopwords]
        text = ' '.join(tokens)

    # Stems words using Porter Stemmer
    if args.stem:
        stemmer = PorterStemmer()
        tokens = text.split()
        stemmed_tokens = [stemmer.stem(plural) for plural in tokens]
        text = ' '.join(stemmed_tokens)   

    # Now that text has been fully altered, split into token list
    tokens = text.split()

    # Remove punctuation from token list
    if args.punctuation:
        tokens = [re.sub(r'\.|\-+|\?|\:|\;|\(|\)|\"|\,|\!|\”|\%|\#|\@|\$|\^|\&|\*|\`|\—|\_+|\“', '', x) for x in tokens]

    # Remove empty strings from token list
    while('' in tokens):
        tokens.remove('')

    return tokens

# Creates a dictionary where the key is the token and the value is the amount of times it occurs in the text
def determine_counts(tokens, args):
    total_wc = len(tokens)
    counts = dict((x, tokens.count(x)) for x in set(tokens))
    sorted_counts = dict(sorted(counts.items(), reverse=args.reverse, key=lambda item: item[1]))
    count_list = {k: sorted_counts[k] for k in list(sorted_counts)}

    for key, value in list(count_list.items())[:N]:
        print(f'{key:<15}{value}')

    return count_list, total_wc

# OpenAI Helped to Create Histogram Code. X axis is token. Y axis is count.
def histogram(count_list, total_wc):
    df = pd.DataFrame(list(count_list.items()), columns=['Tokens', 'Counts'])
    df['Token_Bins'] = pd.cut(df.index, bins=np.arange(-1, len(df), 100), labels=False)

    grouped_df = df.groupby('Token_Bins').agg({'Counts': 'sum'}).reset_index()
    grouped_df['Counts (log10)'] = grouped_df['Counts'].transform(lambda x: np.log10(x))
    bin_ranges = [f'{i}-{i+99}' for i in range(1, len(grouped_df)*100, 100)] 

    fig = px.bar(grouped_df, x=bin_ranges, y='Counts (log10)', labels={'y': '<b> Counts (log10)</b>', 'x': '<b> Most Frequent Token Rankings </b>'}, title='<b>Frequency of Top Ranking Tokens')
    fig.update_layout(title_x=0.5, xaxis_title_standoff=80)
    fig.add_annotation(text=f'<b>Total Normalized Token Count = {total_wc} </b>', xref='paper', yref='paper', x=1, y=1,showarrow=False, font=dict(size=12))
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    fig.show()

# OpenAI Helped to Create Histogram Code. X axis is token. Y axis is count.
def ind_histogram(count_list, total_wc):
    appended_count_list = {k: count_list[k] for k in list(count_list)[:N]}
    tokens = list(appended_count_list.keys())
    counts = list(appended_count_list.values())
    fig = px.bar(x=tokens, y=counts, labels={'x': '<b>Token</b>', 'y': '<b>Counts</b>'}, text_auto="1f", title='<b>Token Counts via Text File</b>')
    fig.update_layout(title_x=0.5, xaxis_title_standoff=80)
    fig.add_annotation(text=f'<b>Total Normalized Token Count = {total_wc} </b>', xref='paper', yref='paper', x=1, y=1,showarrow=False, font=dict(size=12))
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    fig.show()

if __name__ == "__main__":
    args = from_arguments()
    print("Normalizing Text...")
    polished_tokens = edit_corpus(args)
    count_list, total_wc = determine_counts(polished_tokens, args)
    if args.individual:
        ind_histogram(count_list, total_wc)
    else:
        histogram(count_list, total_wc)
