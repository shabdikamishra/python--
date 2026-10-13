
def talk(phrase):
    def say(word):
        print(word)
    
    words = phrase.split(' ')
    for word in words:
        say(word)

talk("I am going to buy the milk")

# Closure with nonlocal
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

increment = counter()
print(increment())  # 1
print(increment())  # 2
print(increment())  # 3