meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma",
            "CREEPY": "aterrador, siniestro",
            }
word = input("Escribe una palabra que no entiendas (con mayusculas)")

if word in meme_dict.keys():
    print(word, meme_dict[word])
else:
    print("esa palabra no esta en el diccionario intentalo otra vez")
