from bCube import *
from bBoard import *
from bGame import *


myCubeList = [bCube(['a','a','e','e','g','n']),
bCube(['a','b','b','j','o','o']),
bCube(['a','c','h','o','p','s']),
bCube(['a','f','f','k','p','s']),
bCube(['a','o','o','t','t','w']),
bCube(['c','i','m','o','t','u']),
bCube(['d','e','i','l','r','x']),
bCube(['d','e','l','r','v','y']),
bCube(['d','i','s','t','t','y']),
bCube(['e','e','g','h','n','w']),
bCube(['e','e','i','n','s','u']),
bCube(['e','h','r','t','v','w']),
bCube(['e','i','o','s','s','t']),
bCube(['e','l','r','t','t','y']),
bCube(['h','i','m','n','qu','u']),
bCube(['h','l','n','n','r','z'])
              ]

tg = bGame(bBoard(myCubeList),'bogglescore.txt')

# to play a game open another IDLE editor window to record words
# save it as bogglescore.txt or whatever filename you choose
# tg.play(gametime) where gametime is in seconds (180 is standard)
# when done save your score file
# then print(tg)
