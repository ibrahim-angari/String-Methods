text = "   welcome to PYTHON programming 101!   "

print(text.strip())
print(text.strip().capitalize())
print(text.strip().upper())
print(text.strip().lower())
print(text.strip().title())
print(text.strip().swapcase())
print(text.strip().center(50, '-'))
print(text.strip().count("o"))
print(text.strip().replace("PYTHON", "Java"))
print(text.strip().split())
print("|".join(text.strip().split()))

print(text.strip().startswith("welcome"))
print(text.strip().endswith("101!"))
print(text.strip().isalnum())
print(text.strip().isalpha())
print(text.strip().islower())
print(text.strip().isupper())
print(text.strip().isspace())

print("cat" == "cat")
print("cat" != "Cat")
print("cat" < "caterpillar")
print("dog" > "Dog")

print("10" == "10")
print("10" != str(10))

words = ["dog", "cat", "zebra", "ant"]
print(sorted(words))
words.sort()
print(words)

num = 123
print(str(num))
print(int("456"))
print(float("3.14"))
