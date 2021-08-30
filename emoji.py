import cursed

def main():
    print('"Pillars Form"')
    game = cursed.getGame()
    print('"Plays Remembered"')
    home, away = getEmoji(game)
    print('"Emoji Appear"')
    fileName, home, away = formatDisplay(home, away)
    cursed.displayGame(game, fileName, home, away)
    print('"File Away"')
    pass

def getEmoji(game):
    try:
        home = chr(int(game['homeTeamEmoji'], 16))
    except:
        home = game['homeTeamEmoji']
    try:
        away = chr(int(game['awayTeamEmoji'], 16))
    except:
        away = game['awayTeamEmoji']
    return home, away

def formatDisplay(home, away):
    fileName = home + 'vs' + away + '.txt'
    home = home + '\t'
    away = away + '\t'
    return fileName, home, away

if __name__=='__main__':
    main()