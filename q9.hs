poss = [a * b * (1000 - a - b) | 
        a <- [1..1000], b <- [a+1..500-a`quot`2], 
        a^2 + b^2 == (1000 - a - b)^2]

main = print $ head poss
