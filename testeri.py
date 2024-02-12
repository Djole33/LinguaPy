from translate import Translator
translator= Translator(to_lang="de")
with open("C:\\Users\\Asus\\Desktop\\tarnslatorjapan\\japann.txt", mode="a") as textjapan:
    text = input("What do you want to translate: ")
    translation = translator.translate(text)
    textjapan.write(text + "\n")
    print(translation)
