sumOfSquares = sum . map (^2)

squareOfSum = (^2) . sum

main = print $ squareOfSum [1..100] - sumOfSquares [1..100]
