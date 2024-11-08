vowels = {"a":"ah","e":"eh", "i":"ee","o":"oh","u":"oo"}
doubleVowels = {"ai":"eye","ae":"eye","ao":"ow","eu":"eh-oo","ei":"ay","au":"ow","iu":"ew","oi":"oyo","ou":"ow","ui":"ooey"}
cons =  "wphkmln"

def validate(validLetters, word):
    for letter in word:
        if validLetters.count(letter) == 0:
            print (letter, "is a invalid hawaiian character")
            return False
    return True

def pronounce(word):
    output = ""
    vowels_str = "aeiou"
    i = 0
    while i < len(word):
        if i > 0 and (not (word[i] in vowels_str and word[i - 1] in vowels_str + cons)):
            output += "-"
        if i < len(word) - 1 and word[i:i + 2] in doubleVowels:
            output += doubleVowels[word[i:i + 2]]
            i += 2
        elif i < len(word) - 2 and word[i:i + 3] in doubleVowels:
            output += doubleVowels[word[i:i + 3]]
            i += 3
        elif word[i] in vowels:
            output += vowels[word[i]]
            i += 1
        elif word[i] in cons:
            if word[i] == 'w':
                if i == 0 or word[i - 1] in 'au':
                    output += 'w'
                elif word[i - 1] in 'ie':
                    output += 'v'
            else:
                output += word[i]
            i += 1
        elif word[i] == "'":
            output += "'"
            i += 1
        elif word[i] == " ":
            output += " "
            i += 1
    return output.capitalize()

def main():
    valid_hawaiian_characters = "aeiouwphkmln'’"
    done = False
    while not done:
        gaveValidWord = False
        while not gaveValidWord:
            word = input("give word: ").lower()
            gaveValidWord = validate(valid_hawaiian_characters, word)

        print("Pronunciation:", pronounce(word))

        response = input("Do you want to enter another word? Y/YES/N/NO? ")
        if response.lower() in ["no", "n"]:
            done = True
main()

#Kakahi aka (no spave Kah-kah-heeah-kah) -> should've been Kah-kah-hee-ah-kah
#E komo mai (extra hypens  Eh- -koh-moh- -meye) -> should've been Eh koh-moh meye
#maui (no space Mowee) -> should've been Mow-ee
#HOALOHA (no space  Hohah-loh-hah) -> should've been Hoh-ah-loh-hah
#makua (nno space Mah-kooah) -> should've been Mah-koo-ah
#humuhumunukunukuapua’a (invalid character) -> should've been Hoo-moo-hoo-moo-noo-koo-noo-koo-ah-poo-ah’ah
#Hoaloha ( no space Hohah-loh-hah) -> should've been Hoh-ah-loh-hah
#kaiapuni (no space Keyeah-poo-nee) -> should've been Keye-ah-poo-nee
#Huaai (no hyphen Hooaheye) -> should've been Hoo-ah-eye
