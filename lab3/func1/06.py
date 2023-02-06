def reverse(sentence):
    word = sentence.split()
    revword = word[::-1]
    print(" ".join(revword))

sentence = "We are ready"
reverse(sentence)
