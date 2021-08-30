import requests

byteSize = 8
            
def getGame():
    season = getSeason()
    day = getDay()
    games = getGamesByDate(season, day)
    return getTeamGame(games)

def getSeason():
    while True:
        try:
            return int(input('Season of Internet League Blaseball: ')) - 1
        except:
            print('EMERGENCY ALERT! INVALID SEASON')          
            
def getDay():
    while True:
        try:
            return int(input('Game Day. Play must never stop: ')) - 1
        except:
            print('replay the unday')
            
def getGamesByDate(season, day):
    url = 'https://api.sibr.dev/corsmechanics/www.blaseball.com/database/games'
    query = {'season': season, 'day': day}
    return requests.request('GET', url, params=query).json()

def getTeamGame(games):
    while True:
        teamName = getTeamName()
        i = 0
        for i in range(len(games)):
            currentGame = games[i]
            namesForGame = [currentGame['homeTeamName'].lower(), currentGame['homeTeamNickname'].lower(), currentGame['awayTeamName'].lower(), currentGame['awayTeamNickname'].lower()]
            if teamName in namesForGame:
                return currentGame
        print('We\'re Fans, just like y-u ca-\'t ch-os- t-at t-am')
        
def getTeamName():
    return input('Many leagues, one team: ').lower()

def displayGame(game, fileName, home, away):
    feed = getGameFeed(game['id'])
    outputFile(feed, fileName, home, away)
    
def getGameFeed(gameId):
    url = 'https://api.sibr.dev/corsmechanics/www.blaseball.com/database/feed/game'
    query = {'id': gameId}
    return requests.request('GET', url, params=query).json()

def outputFile(feed, fileName, home, away):
    file = open(fileName, 'w', encoding='utf-8')
    if (feed):
        displayEvents(feed, file, home, away)
    else:
        displayFeedlessError(file, home, away)
    file.close()
    
def displayEvents(feed, file, home, away):
    for i in range(len(feed), 0, -1):
        event = feed[i-1]
        eventType = bin(event['type'])[2:].rjust(byteSize, '0')
        for i in range(byteSize):
            if eventType[i]=='0':
                file.write(home)
            elif eventType[i]=='1':
                file.write(away)
        file.write('\n')
        
def displayFeedlessError(file, home, away):
    file.write(home[0])
    file.write(chr(int('0x1F19A', 16)))
    file.write(away[0] + '\n')
    file.write(chr(int('0x1F4AC', 16)) + '\n')
    file.write(chr(int('0x1F991', 16)) + '\n')
    file.write(chr(int('0x26D4', 16)))
    file.write(chr(int('0x1F372', 16)))