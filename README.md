# Mini Monopoly Game (Python)

## 🎮 Game Overview
Two players take turns rolling a dice, moving across a 16-tile map. 
Players can buy properties, upgrade them and collect rent from each other. 
The richest player at the end of the game wins!

## 🏁 Features
- 🎲 2-player turn-based game by rolling dice
- 🏘️ Start with M$1500, buy and upgrade properties — manage every expense wisely 
- 💰 Try to earn rent from opponents or just save salary？
- 🚔 Watch out for taxes and jail — random events can flip the game anytime!

## 🛠️ Files
  - `monopoly.py` – main game logic and flow
  - `element.py` – player and city class definitions

## 🗺️ Map Layout
```text
              15        14       13       12
  |--------|--------|--------|--------|--------|
0 | GoGoGo | Tokyo  | Geneva | Milan  | GoJail |  
  |--------|--------|--------|--------|--------|
1 | London |                          | Seoul  |  11
  |--------|                          |--------|
2 | PayTax |                          | PayTax |  10
  |--------|                          |--------|
3 | Berlin |                          | Athens |  9
  |--------|--------|--------|--------|--------|
4 |  Jail  | Ottawa | PayTax | Sydney | Parkin | 
  |--------|--------|--------|--------|--------|
                5        6        7        8
