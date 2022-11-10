from bs4 import BeautifulSoup
from requests import get
import matplotlib.pyplot as plt

URL = 'https://en.wikipedia.org/wiki/Special:Random'
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Index 0 means the number 0 and its value is equal to how many times the program will find this number in Wikipedia
numbersOfNumbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# variable for loop
x = 0

while(x < 1000):

    page = get(URL)  # entrance to the site
    # downloading the page
    bs = BeautifulSoup(page.content, features="html.parser")

    # searching for numbers
    for i in numbers:
        tags = bs.find_all(text=numbers[i])

        numbersOfNumbers[i] = numbersOfNumbers[i] + \
            tags.__len__()  # save the occurrence

    x += 1
    print("search number " + x)

print(numbersOfNumbers)

# creating a plot
plt.title("Frequency of numbers")
plt.ylabel("Frequency")
plt.xlabel("Numbers")
plt.bar(numbers, numbersOfNumbers, color="#266cf7")
plt.grid(axis="y", linewidth=0.5)
plt.show()
