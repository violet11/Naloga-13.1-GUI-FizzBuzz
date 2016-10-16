"""There has been a hideous crime! A full container of ice cream was stored in the SmartNinja fridge - and now it's
completely empty. But the criminal made a fatal mistake. S/he left a spoon inside the container and with a spoon
also his/her DNA. A perfect case for our CSI investigators!CSI lab successfully extracted the DNA and wrote it in the
ACTG code format. The only thing needed now is a program that would match that DNA with the suspects DNA and find the
criminal."""

print "Who ate the ice cream?"

# hair
Black_hair = "CCAGCAATCGC"
Brown_hair = "GCCAGTGCCG"
Blonde_hair = "TTAGCTATCGC"

# face
Square = "GCCACGG"
Round = "ACCACAA"
Oval = "AGGCCTCA"

# eyes
Blue = "TTGTGGTGGC"
Green = "GGGAGGTGGC"
Brown = "AAGTAGTGAC"

# gender
Female = "TGAAGGACCTTC"
Male = "TGCAGGAACTTC"

# race
White = "AAAACCTCA"
Black = "CGACTACAG"
Asian = "CGCGGGCCG"

# suspects
Eva = Female and White and Blonde_hair and Oval
Larisa = Female and White and Brown_hair and Brown and Oval
Matej = Male and White and Black_hair and Blue and Oval
Miha = Male and White and Brown_hair and Green and Square

dna = open("dna.txt").read()

if Eva in dna: # searching string within a string
    print "Eva did it!"

elif Larisa in dna:
    print "Larisa did it!"

elif Matej in dna:
    print "Matej did it!"

elif Miha in dna:
    print "Miha did it!"

else:
    print "There is no suspect!"


print "Crime is solved :)"