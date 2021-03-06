import System.IO
import Data.Char

main :: IO()
main = do
        text <- getLine
        putStrLn $ parse text

parse :: String -> String
parse "" = ""
parse (s:('-':[])) = s : "-"
parse (s:('-':ss)) = parse $ cont (ord s) (ord (ss !! 0)) ++ parse (tail ss)
parse (s:ss) = s : parse ss

cont :: Int -> Int -> String
cont b a = if b == a then chr a : "" else chr b : cont (b+1) a
