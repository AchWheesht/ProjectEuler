# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

one = 3
two = 3
three = 5
four = 4
five = 4
six = 6
seven = 5
eight = 5
nine = 4
ten = 3
eleven = 6
twelve = 6
thirteen = 8
fourteen = 8
fifteen = 7
sixteen = 7
seventeen = 9
eighteen = 8
nineteen = 8
twenty = 6
thirty = 6
fourty = 6
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
hundred = 7

digits = {
"0": 0,
"1" : 3, #one
"2" : 3, #two
"3" : 5, #three
"4" : 4, #four
"5" : 4, #five
"6" : 3, #six
"7" : 5, #seven
"8" : 5, #eight
"9" : 4, #nine
"10" : 3, #ten
"11" : 6, #eleven
"12" : 6, #twelve
"13" : 8, #thirteen
"14" : 8, #fourteen
"15" : 7, #fifteen
"16" : 7, #sixteen
"17" : 9, #seventeen
"18" : 8, #eighteen
"19" : 8  #nineteen
}
ttotal = 0

sum_to_nineteen = 106
ttotal += sum_to_nineteen

sum_to_ten = 36
ttotal += (5 * 60) + (2*50) + 70 + (8*36)
sum99 = ttotal



tens = {
    "0": 0,
    "2" : 6, #twenty
    "3" : 6, #thirty
    "4" : 6, #fourty
    "5" : 5, #fifty
    "6" : 5, #sixty
    "7" : 7, #seventy
    "8" : 6, #eighty
    "9" : 6  #ninety
    }

total = 0

for i in range(1, 1001):
    if i < 20:
        total += digits[(str(i))]
    elif i >= 20 and i < 100:
        total += tens[str(i)[0]]
        total += digits[str(i)[1]]
    elif i % 100 == 0 and i != 1000:
        total += digits[str(i)[0]]
        total += 7 #hundred
    elif i > 100 and i < 1000:
        number = str(i)
        total += digits[number[0]]
        total += 10 #"hundred and"
        doubles = (int(number[1]) * 10) + int(number[2])
        if doubles < 20:
            total += digits[str(doubles)]
        else:
            total += tens[str(doubles)[0]]
            total += digits[str(doubles)[1]]
    elif i == 1000:
        total += 11 #one thousand
    else:
        raise ValueError

print(total)



#
