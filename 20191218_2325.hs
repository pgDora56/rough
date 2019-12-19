-- State monad Test
--

import Control.Monad.State

plpl :: State Int Int
plpl = state $ plpl where 
    plpl x = x + 1

main = do
    
