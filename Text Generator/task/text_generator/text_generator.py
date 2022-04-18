import random

from nltk.tokenize import WhitespaceTokenizer
from nltk import trigrams
from collections import Counter


def chain_of_Markov(arr_trigrams) -> dict:
    dict_Markova = dict()
    for tuple_item in arr_trigrams:
        dict_Markova.setdefault(tuple_item[0] + " " + tuple_item[1], []).append(tuple_item[2])

    for key, value in dict_Markova.items():
        tmp_arr = []
        for tail, count in Counter(value).items():
            tmp_arr.append((tail, count))
        tmp_arr.sort(key=lambda x: x[1], reverse=True)
        dict_Markova[key] = tmp_arr
    return  dict_Markova


def get_tails_counts(arr_tails_counts) -> tuple:
    arr_tails = []
    arr_count = []
    for i in arr_tails_counts:
        arr_tails.append(i[0])
        arr_count.append(i[1])
    return arr_tails, arr_count


def create_Offer():
    for i in range(10):
        # List with heads, which can be chosen like first pair of word in our text
            first_heads = list(filter(lambda w: w.split()[0][-1] not in '.!?' and w.istitle() and w[0].isalpha(),
                                    list(dict_Markova.keys())))

            # Generation of pseudo-text
            selected_head_word = random.choice(first_heads)
            markov_chain_tails, markov_chain_counts = get_tails_counts(dict_Markova[selected_head_word])
            selected_tail_word = random.choices(markov_chain_tails, markov_chain_counts)[0]
            print(selected_head_word, selected_tail_word, end=' ')
            counter = 3
            while True:
                selected_head_word = selected_head_word.split()[1] + ' ' + selected_tail_word
                markov_chain_tails, markov_chain_counts = get_tails_counts(dict_Markova[selected_head_word])
                selected_tail_word = random.choices(markov_chain_tails, markov_chain_counts)[0]
                print(selected_tail_word, end=' ')
                counter += 1
                if selected_tail_word[-1] in '.!?' and counter >= 5:
                    break
            print()


if __name__ == "__main__":
    # with open("corpus.txt", "r") as file:
    with open(input(), "r") as file:
        text_file = file.read()
        arr_tokenized_text = WhitespaceTokenizer().tokenize(text_file)
        arr_trigrams = list(trigrams(arr_tokenized_text))
        dict_Markova = chain_of_Markov(arr_trigrams)

    create_Offer()
    print()
