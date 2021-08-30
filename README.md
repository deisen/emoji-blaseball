# Emoji Blaseball
## How to View:
- Run emoji.py
- Enter Season, Day, and Team when prompted
- Open the Game file
## How to Interpret:
- A file is created for one Blaseball Game
- Each line in the file is a Game Feed Event
- The file name is `home emoji`vs`away emoji`.txt
- `home emoji` is used as `0`
- `away emoji` is used as `1`
- The Event Type is displayed in binary
## How it Exists:
- Created for the [cursed.sibr.dev](https://cursed.sibr.dev/) ~~hack~~ snackathon
- Games, Teams, inspiration, and more from [blaseball.com](https://www.blaseball.com/)
- Using [corsmechanics by SIBR](https://api.sibr.dev/corsmechanics/www.blaseball.com)
## How it Doesn't Work:
- This depends on Game Feed Events; i.e., Games without Feeds do not work correctly. Only Expansion Era Games display as described. Seasons 1-11 create files with very limited information
- This finds Teams by their names; e.g., there is no `Spies` Team for Season 24, Day 99. There are, however, multiple `-----` Teams. Only the first match is chosen
- Emoji are finicky. Python is finicky. Windows (especially when dealing with both of these) is finicky. Good luck
