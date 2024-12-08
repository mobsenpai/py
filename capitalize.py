a = input("Enter any sentence: ")

lista = a.split()
modlist = []
sent = ""

for i in lista:
    # modlist.append(i.capitalize())
    word = i.capitalize()
    sent = sent + word + " "
# print(str(modlist))
print(sent)
