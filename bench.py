import requests

from fastcontain import FastContain
import time

hamlet_url = "https://raw.githubusercontent.com/cs109/2015lab1/master/hamlet.txt"

quotes = [
    "That one may smile, and smile, and be a villain;",
    "Though this be madness, yet there is a method in't.",
    "Good now, sit down, and tell me, he that knows,",
    "Together with all forms, moods, shows of grief,"
]

hamlet_text = requests.get(hamlet_url).text
fast_hamlet_text = FastContain(hamlet_text)

for quote in quotes:
    start = time.time()
    print(quote in hamlet_text, end=", ")
    print(f"Normal __contain__ finished in {time.time() - start}")

    start = time.time()
    print(quote in fast_hamlet_text, end=", ")
    print(f"Fast __contain__ finished in {time.time() - start}")