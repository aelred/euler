isPalindrome x = s == reverse s
    where s = show x

palindromes = [x * y | x <- [100..999], y <- [x..999], isPalindrome (x * y)]

main = print $ maximum palindromes
