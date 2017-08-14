def popularity(t, p):
    if t == 0:
        return 1 #its a good recursive funcion because it has a base case
    else:
        score = 0
        for f in friends(p):
            score = score + popularity(t - 1, f)
        return score
