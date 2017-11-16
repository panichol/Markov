from Markov import MarkovMap

if __name__ == "__main__":
    emailMap = MarkovMap("Data/juggling.txt",order = 7)
    print(emailMap.Generate(1000))
