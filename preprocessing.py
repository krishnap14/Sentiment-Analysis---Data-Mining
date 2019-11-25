import sys
import re

out = open("trainTestSaturday.csv", "w+")

with open(sys.argv[1]) as x:
    for line in x:
        a, b, c = line.split(",")
        #Replace all the strings with nothing

        replaceDoubleQuotes = a.replace('"', "")
        replaceBackSlash = replaceDoubleQuotes.replace("\\", " ")
        replaceSlash = replaceBackSlash.replace("/", " ")
        replaceBrackOpen = replaceSlash.replace("(", " ")
        replaceOpenSquare = replaceBrackOpen.replace("[", "")
        replaceCurlyOpen = replaceOpenSquare.replace("{", "")
        replaceCurlyClose = replaceCurlyOpen.replace("}", "")
        replaceTilda = replaceCurlyClose.replace("~", "")
        replaceCloseSquare = replaceTilda.replace("]", "")
        replaceBrackClose = replaceCloseSquare.replace(")", " ")
        replaceUnderScore = replaceBrackClose.replace("_", " ")
        replaceHyphens = replaceUnderScore.replace("-", " ")
        replaceCommas = replaceHyphens.replace(",", " ")                             #Special case ","
        replaceSemiColons = replaceCommas.replace(";", " ")                          #Special case ";"
        replaceSingleQuotes = replaceSemiColons.replace("'", "")                         #THIS WAS THE FINAL ONE
        
        list = []

        for word in replaceSingleQuotes:                                              #Check for each word if it is a problematic word.
            y = re.sub("^[0-9$*#|@!%^&+-,.:?=_]+$", " ", word)                         #Starts with, contains and ends with non alphabets.
            yy = re.sub("^[a-zA-Z]+[0-9$*#|@!%^&:?=_]+[a-zA-Z]+$", " ", y)             #Contains non-alphabets in the middle of the word.
            wordString = ""
            if re.search(r"^[0-9!-//@=\\_}{~]+[a-zA-Z]+$", yy) != None:                     #Check for nonsense followed by words.
                position = re.search("[a-zA-Z]+$", yy)                                   #position of alphabets.

                temp, temp_1 = str(position).split("(")                               #Convert position to string, and split it 
                temp_2, temp_3, temp_4 = temp_1.split(",")                            #Further split the string to get the number

                ourNum = int(temp_2)                                                   #Convert the string to integer to get the position of the word
                wordString = line[ourNum:line.__len__()-1]                              #Get the word

            if re.search(r"^[a-zA-Z]+[0-9!-//@=\\_}{~]+$", yy) != None:                     #Check for words followed by nonsense.
                position = re.search(r"[0-9!-//@=\\_}{~]+$", yy)                           #position of nonsense.

                temp, temp_1 = str(position).split("(")                               #Convert position to string, and split it 
                temp_2, temp_3, temp_4 = temp_1.split(",")                            #Further split the string to get the number

                ourNum = int(temp_2)                                                   #Convert the string to integer to get the position of the word
                wordString = line[0:ourNum]                                             #Get the word
            
            if wordString == "":
                list.append(yy)
            else:
                list.append(wordString)

        finalReview = "".join(list)
        replaceNewLine = c.replace("\n", "")                                            #Replace new line character.
        
        l = '"' +finalReview + '",' + replaceNewLine + "," + b                          #This is the line without original quotes and with the new quotes around the reviews
        out.write(l)
        out.write("\n")
        print(l)


###############################TEST FILE###########################################
with open(sys.argv[2]) as y_2:
    for stuff in y_2: 
        a, b = stuff.split(",")

        replaceDoubleQuotes = b.replace('"', "")
        replaceBackSlash = replaceDoubleQuotes.replace("\\", " ")
        replaceSlash = replaceBackSlash.replace("/", " ")
        replaceBrackOpen = replaceSlash.replace("("," ")
        replaceOpenSquare = replaceBrackOpen.replace("[", "")
        replaceCurlyOpen = replaceOpenSquare.replace("{", "")
        replaceCurlyClose = replaceCurlyOpen.replace("}", "")
        replaceTilda = replaceCurlyClose.replace("~", "")
        replaceCloseSquare = replaceTilda.replace("]", "")
        replaceBrackClose = replaceCloseSquare.replace(")", " ")
        replaceUnderScore = replaceBrackClose.replace("_", " ")
        replaceHyphens = replaceUnderScore.replace("-", " ")
        replaceCommas = replaceHyphens.replace(",", " ")
        replaceSemiColons = replaceCommas.replace(";", " ")
        replaceSingleQuotes = replaceSemiColons.replace("'", "")

        replaceNewLine = replaceSingleQuotes.replace("\n", "")                          #Text

        list_2 = []

        for word_2 in replaceNewLine:                                                   #Check for each word if it is a problematic word.
            y = re.sub("^[0-9$*#|@!%^&+-,.:?=_]+$", " ", word_2)                         #Starts with, contains and ends with non alphabets.
            yy = re.sub("^[a-zA-Z]+[0-9$*#|@!%^&:?=_]+[a-zA-Z]+$", " ", y)             #Contains non-alphabets in the middle of the word.
            wordString = ""

            if re.match(r"^[0-9!-//@=\\_}{~]+[a-zA-Z]+$", yy) != None:                     #Check for nonsense followed by words.
                position = re.search("[a-zA-Z]+$", yy)                                   #position of alphabets.

                temp, temp_1 = str(position).split("(")                               #Convert position to string, and split it 
                temp_2, temp_3, temp_4 = temp_1.split(",")                            #Further split the string to get the number

                ourNum = int(temp_2)                                                   #Convert the string to integer to get the position of the word
                wordString = line[ourNum:line.__len__()-1]                              #Get the word

            if re.match(r"^[a-zA-Z]+[0-9!-//@=\\_}{~]+$", yy) != None:                     #Check for words followed by nonsense.
                position = re.search(r"[0-9!-//@=\\_}{~]+$", yy)                           #position of nonsense.

                temp, temp_1 = str(position).split("(")                               #Convert position to string, and split it 
                temp_2, temp_3, temp_4 = temp_1.split(",")                            #Further split the string to get the number

                ourNum = int(temp_2)                                                   #Convert the string to integer to get the position of the word
                wordString = line[0:ourNum]                                             #Get the word
            
            if wordString == "":
                list_2.append(yy)
            else:
                list_2.append(wordString)
        
        finalReview_2 = "".join(list_2)                                                #Join the words to complete the review.

        
        l_2 ='"'+ finalReview_2 + '",' +a + ",?"                                        #This is the line without original quotes and with the new quotes around the reviews
        out.write(l_2)
        out.write("\n")

out.close()

            #Modify the program so that it does not take out words if they have ***priya, but replaces ***priya with priya
            #Check why the program keeps running.