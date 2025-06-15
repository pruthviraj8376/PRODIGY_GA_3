import random

def build_markov_chain(text, n=1):
    words = text.split()
    markov_chain = {}
    
    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        if key in markov_chain:
            markov_chain[key].append(next_word)
        else:
            markov_chain[key] = [next_word]
    
    return markov_chain

def generate_text(chain, length=50):
    current = random.choice(list(chain.keys()))
    output = list(current)

    for _ in range(length):
        next_words = chain.get(current)
        if not next_words:
            break
        next_word = random.choice(next_words)
        output.append(next_word)
        current = tuple(output[-len(current):])
    
    return ' '.join(output)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        text = f.read().lower()

    chain = build_markov_chain(text, n=2)
    generated = generate_text(chain, length=100)
    print("\nGenerated Text:\n")
    print(generated)
