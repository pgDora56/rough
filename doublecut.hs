import System.Environment
import System.IO 

main :: IO()
main = do
    args <- getArgs
    handle <- openFile (args !! 0) ReadMode
    encoding <- mkTextEncoding "cp65001"
    hSetEncoding handle encoding
    contents <- hGetContents handle
    let datas = lines contents
    main' datas ""
    hClose handle

main' :: [String] -> String -> IO()
main' [] prv = return ()
main' (line:remain) prv = do
    let cpr = cutdate line
    if cpr == prv
        then main' remain prv
        else do
            putStrLn line
            main' remain cpr

cutdate :: String -> String
cutdate (']':cs) = cs
cutdate (_:cs)   = cutdate cs

