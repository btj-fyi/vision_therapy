from constants import ALPHABET_LOWER
import random


class MichiganTacking:
    def __init__() -> None:
        pass


# 4.33 lines
# 352 chars
example: str = """
    Narg rek koh mool. Sobe ohn ceti mot. Pok dul oth riep lok thon pirf. Uhl 
    palk ruaq ugb lirk bhar tquo. Quak rilt beld tob tuj bop tak deod upt. 
    Deh nop nule bot nuad cerm buh wuh daj quat narc teub vaf iod. Arj pade zug 
    quif mulg twur. Luge mise kicgu pah blik tubil velc dalm. Olp kwe fexam pogs 
    yac gane quez firg pemy.
    """

# print(len(example))
# print(len(example.replace(" ", "")))
# print(len(ALPHABET_LOWER))

TOTAL_SPACES = 352
MIN_SECTION_JUMP = 0
MAX_SECTION_JUMP = 4

words = ""
for i, letter in enumerate(ALPHABET_LOWER):
    if len(words) < TOTAL_SPACES:
        word_length = range(0, random.randint(1, 7))
        word = "".join([random.choice(ALPHABET_LOWER) for i in word_length])
        split_index = random.randint(0, len(word))
        l, r = word[:split_index], word[split_index:]
        words += " " + l + letter + r
words = words.strip()
remaining_spaces = TOTAL_SPACES - len(words)
additional_words = ""
while len(additional_words) < remaining_spaces:
    if remaining_spaces >= 7:
        word_length = range(0, random.randint(1, 7))
    else:
        word_length = range(0, random.randint(1, remaining_spaces))
    word = "".join([random.choice(ALPHABET_LOWER) for i in word_length])
    additional_words += " " + word
additional_words = additional_words.strip()
words_list = words.split()
additional_words_list = additional_words.split()

print(words_list)
cache: list[tuple] = {letter: words_list[i] for i, letter in enumerate(ALPHABET_LOWER)}
print(cache)
while len(words) < TOTAL_SPACES:
    remaining_spaces = TOTAL_SPACES - len(words)
    for letter in ALPHABET_LOWER:
        skip = random.randint(0, 1)
        if skip > 0:
            print("SKIPPED", letter)
            continue
        alphabet_tmp = ALPHABET_LOWER.copy()
        alphabet_tmp.remove(letter)
        if remaining_spaces >= 7:
            word_range = range(0, random.randint(1, 7))
        else:
            word_range = range(0, random.randint(1, remaining_spaces))
        additional_word = "".join([random.choice(alphabet_tmp) for i in word_range])
        print("Addidng new word", additional_word, "for", letter.upper())
        i = words_list.index(cache[letter])
        words_list.insert(i, additional_word)
        words = " ".join(words_list)
print(cache)
print()
print(words_list)
