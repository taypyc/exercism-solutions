def recite(start_verse, end_verse):
    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    
    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ]

    verses = []
    for day in range(start_verse, end_verse + 1):
        intro = f"On the {ordinals[day-1]} day of Christmas my true love gave to me: "
        
        items = ""
        for i in range(day - 1, 0, -1):
            items += gifts[i]
            
        if day > 1:
            items += "and " + gifts[0]
        else:
            items += gifts[0]
            
        verses.append(intro + items)
        
    return verses