print "Who ate ice cream?"

Black_hair = "CCAGCAATCGC"
Brown_hair = "GCCAGTGCCG"
Blonde_hair = "TTAGCTATCGC"

Square = "GCCACGG"
Round = "ACCACAA"
Oval = "AGGCCTCA"

Blue = "TTGTGGTGGC"
Green = "GGGAGGTGGC"
Brown = "AAGTAGTGAC"

Female = "TGAAGGACCTTC"
Male = "TGCAGGAACTTC"

White = "AAAACCTCA"
Black = "CGACTACAG"
Asian = "CGCGGGCCG"

Eva = Female and White and Blonde_hair and Blue and Oval
Larisa = Female and White and Brown_hair and Brown and Oval
Matej = Male and White and Black_hair and Blue and Oval
Miha = Male and White and Brown_hair and Green and Square

dna = open("dna.txt").read()

if Eva in dna:
    print "Eva did it!"

elif Larisa in dna:
    print "Larisa did it!"

elif Matej in dna:
    print "Matej did it!"

elif Miha in dna:
    print "Miha did it!"

else:
    print "There is no Suspect"

print "Crime is solved :)"


