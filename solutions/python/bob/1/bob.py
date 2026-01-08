def response(hey_bob):
    # 1. Clean up the input (remove leading/trailing whitespace)
    phrase = hey_bob.strip()
    
    # 2. Define the conditions
    is_silence = not phrase
    is_question = phrase.endswith("?")
    # is_yelling is true if there are letters AND all letters are uppercase
    is_yelling = phrase.isupper() 

    # 3. Bob's Logic Tree
    if is_silence:
        return "Fine. Be that way!"
    
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    
    if is_yelling:
        return "Whoa, chill out!"
    
    if is_question:
        return "Sure."
    
    return "Whatever."