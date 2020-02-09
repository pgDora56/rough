{-# LANGUAGE OverloadedStrings #-}
module Lib where

import Data.Aeson
import Network.HTTP.Simple
import System.IO

url = "https://script.google.com/macros/s/AKfycbwcQayK15gTHEPrmAwwSEgEyV7W8rHeQzJ7O8UsLG4Cr4No-ZY/exec"

trans :: String -> IO()
trans text = do
                let access_url =  (url ++ "?text=" ++ text ++ "&source=en&target=fr") 
                let res = parseRequest access_url :: Maybe Request
                case res of 
                    Nothing  -> putStrLn "Nothin"
                    Just res -> do
                                print res
                                lbs <- httpLBS res
                                print $ getResponseBody lbs



