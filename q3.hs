smallestFactor x = head $ filter ((==0) . mod x) [2..x]

largestFactor x = x `quot` smallestFactor x

largestPrimeFactor x
    | largest == 1 = x
    | otherwise    = largestPrimeFactor largest
    where largest = largestFactor x

main = print $ largestPrimeFactor 600851475143
