def answer(question):
    content = question.replace("What is", "").replace("?", "").strip()
    
    if not content:
        raise ValueError("syntax error")
    
    content = content.replace("multiplied by", "multiplied")
    content = content.replace("divided by", "divided")
    
    tokens = content.split()
    supported = {"plus", "minus", "multiplied", "divided"}
    
    try:
        res = int(tokens[0])
    except ValueError:
        if tokens[0] in supported:
            raise ValueError("syntax error")
        raise ValueError("unknown operation")

    i = 1
    while i < len(tokens):
        op = tokens[i]
        
        try:
            int(op)
            raise ValueError("syntax error")
        except ValueError as e:
            if str(e) == "syntax error": 
                raise e
            if op not in supported:
                raise ValueError("unknown operation")

        if i + 1 >= len(tokens):
            raise ValueError("syntax error")
            
        try:
            val = int(tokens[i + 1])
        except ValueError:
            raise ValueError("syntax error")
            
        if op == "plus":
            res += val
        elif op == "minus":
            res -= val
        elif op == "multiplied":
            res *= val
        elif op == "divided":
            res //= val
            
        i += 2
        
    return res