msg=input('>')
word=msg.split(" ")

emoji ={
    ":)":"😊",
    ":(":"😢"
}
output=""
for word in msg:
    output+=emoji.get(word ,word) + " "

print(output)