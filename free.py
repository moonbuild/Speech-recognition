import wikipedia
statement="snails"
results = wikipedia.summary(statement, sentences=5)
print("According to Wikipedia")
print(results)