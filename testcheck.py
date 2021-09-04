from checkGrafph import finalCheck
x = [[], ['ac'], ['cb'], ['ac', 'cb'], ['ad'], ['ac', 'ad'], ['cb', 'ad'], ['ac', 'cb', 'ad'], ['db'], ['ac', 'db'], ['cb', 'db'], ['ac', 'cb', 'db'], ['ad', 'db'], ['ac', 'ad', 'db'], ['cb', 'ad', 'db'], ['ac', 'cb', 'ad', 'db'], ['cd'], ['ac', 'cd'], ['cb', 'cd'], ['ac', 'cb', 'cd'], ['ad', 'cd'], ['ac', 'ad', 'cd'], ['cb', 'ad', 'cd'], ['ac', 'cb', 'ad', 'cd'], ['db', 'cd'], ['ac', 'db', 'cd'], ['cb', 'db', 'cd'],
['ac', 'cb', 'db', 'cd'], ['ad', 'db', 'cd'], ['ac', 'ad', 'db', 'cd'], ['cb', 'ad', 'db', 'cd'], ['ac', 'cb', 'ad', 'db', 'cd']]

for i in x :
    print(i,"+")
    print(finalCheck(i,"a","b"),"++")
