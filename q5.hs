import Data.Function
import Data.List
import Control.Arrow

smallestFactor x
    | x >= 2    = head $ filter ((==0) . mod x) [2..x]
    | otherwise = x

frequency :: Ord a => [a] -> [(Int, a)]
frequency = map (length &&& head) . group . sort

groupWith f xs = groupBy ((==) `on` f) sorted
    where sorted = sortBy (compare `on` f) xs

primeFactors x
    | factor1 == x = [x]
    | otherwise    = primeFactors factor1 ++ primeFactors factor2
    where factor1 = smallestFactor x
          factor2 = x `quot` factor1

leastCommonMultiple xs = product [y^x | (x, y) <- highestPowers]
    where primes = concatMap (frequency . primeFactors) xs
          grouped = groupWith snd $ sort primes
          highestPowers = map maximum grouped

main = print $ leastCommonMultiple [1..20]
