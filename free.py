import wolframalpha
question="what is a truth table in electronics"
appid="P4HU6J-YTXTXUPV2T"
client=wolframalpha.Client('P4HU6J-YTXTXUPV2T')
result = client.query(question).results
answer=next(result).text
print(answer)