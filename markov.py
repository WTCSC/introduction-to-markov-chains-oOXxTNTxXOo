import random
import sys
import string
import re  

"""
Create the sample text and the dictionary to store word transitions
"""
text = "The Markov chains are mathematical systems that undergo transitions from one state to another within a finite set of possible states. They are used to model various real-world phenomena in fields such as physics, economics, biology, and computer science. A key property of a Markov chain is that the probability of transitioning to the next state depends solely on the current state, and not on the sequence of events that preceded it. This is known as the memoryless property, or the Markov property. In this essay, we will walk through the theory behind Markov chains, and we will implement a basic Markov chain simulation using Python to better understand its workings. We will also test a simple Markov chain model and output the results in a readable format for further analysis."
transitions = {}

"""
Build the Markov Chain
1. Split the text into words
2. Iterate over the words
3. For each word, add the next word to the list of transitions
"""

words = re.findall(r"[\w]+|[^\s\w]", text.lower())   #splits words on puncuations
for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in transitions:
        transitions[current_word] = []
    transitions[current_word].append(next_word)

"""
Generate new text using the Markov Chain, starting with a given word and
generating a specified number of words:
1. Start with the given word
2. Add the word to the result list
3. For the specified number of words:
    a. If the current word is in the transitions dictionary, choose a random next word
    b. Add the next word to the result list
    c. Update the current word to the next word
4. Return the generated text as a string
"""

punc = string.punctuation # creates word puncuation list

def join_punctuation(seq, characters=punc):  #function joins words based if there is a puncuation or not
    characters = set(characters)
    seq = iter(seq)
    current = next(seq)

    for nxt in seq:
        if nxt in characters:
            current += nxt
        else:
            yield current
            current = nxt

    yield current

def generate_text(start_word, num_words):
    current_word = start_word
    result = [current_word.capitalize()] # capitalizes first word
    for _ in range(num_words - 1):
        if current_word in transitions:
            next_word = random.choice(transitions[current_word])
            if next_word == "-": # function here accounts for hyphens - however can not determin if is addition or writing so will assime writing 
                next_word = random.choice(transitions[next_word])
                current_word = (current_word + "-" + next_word)
                next_word = random.choice(transitions[next_word])
                result[-1] = current_word
            if current_word in punc: # checks if there is a puncuation added if there is adds next word then refreshes next word
                if current_word == ".": # checks for period
                    current_word = next_word
                    result.append(next_word.capitalize()) # capilized word after period
                else:
                    current_word = next_word
                    result.append(next_word)
                next_word = random.choice(transitions[current_word])
            current_word = next_word    
            result.append(next_word)
        else:
            break
    return " ".join(join_punctuation(result))

"""
Example usage, generating 10 words starting with "Mary"
"""
x = sys.argv[1] #allows inputs to be added form command line
y = sys.argv[2]
print(generate_text(str(x.lower()), int(y)))