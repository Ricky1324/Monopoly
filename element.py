'''
element.py - identify class Player and class City
'''

# Define the board layout: index (0-15) -> city or special tile name
map_index = {   0: 'GoGoGo', 1: 'London', 2: 'PayTax', 3: 'Berlin',
                4: ' Jail ', 5: 'Ottawa', 6: 'PayTax', 7: 'Sydney',
                8: 'Parkin', 9: 'Athens', 10:'PayTax', 11:'Seoul ',
                12:'GoJail', 13:'Milan ', 14:'Geneva', 15:'Tokyo'
                }

class Player:
    def __init__(self, name: str):
        self.name = name
        self.money = 1500
        self.location = 0

    def action(self, point: int):
        
        # If player passes the Start tile 'GoGoGo' again, collect salary and start all over again
        self.location += point
        if self.location > 15:
            print('>>>Collect M$200 Salary<<<')
            input('(Press [Enter] to continue...)')
            self.money += 200
            self.location -= 16

        # Special tile: Go to Jail
        if self.location == 12:
            print('>>>Please Go to Jail~<<<')
            input('(Press [Enter] to continue...)')
            self.location = 4
            return False

         # Special tiles: Pay Tax
        elif self.location in [2, 6, 10]:
            print('>>>Please Pay Income Tax: M$200<<<')
            input('(Press [Enter] to continue...)')
            self.money -= 200
            return False
        
        # Special tiles: Just rest (Visiting Jail or Parking)
        elif self.location in [4, 8]:
            print('>>>Just Have a Break<<<')
            input('(Press [Enter] to continue...)')
            return False  

        # Land on a City tile    
        else:
            return True

    #print player's current status.
    def __str__(self):
        line0 = f'\n---------------------\n'
        line1 = f'---Status of {self.name}---\n'
        line2 = f'Money: M${self.money}\n'
        line3 = f'Location: {map_index[self.location]}\n'
        line4 = f'---------------------\n'
        status = line0 + line1 + line2 + line3 +line4
        return status

class City:
    def __init__(self, name: str, price: int, rent: int, index: int):
        self.name = name
        self.price = price
        self.house_number = 0
        self.rent  = rent
        self.index = index
        self.owner = ' '

    #print Tile details
    def __str__(self):
        
        line1 = f'\n~~~~{self.name}~~~~~\n'
        line2 = f'House Cost: M${self.price}\n'
        line3 = f'Rent: M${self.rent}\n'
        line4 = f'Location: {self.index}/15\n'
        line5 = f'Houses: {self.house_number}\n'
        line6 = f'Owned by: {self.owner}\n'
        line7 = f'~~~~~~~~~~~~~~~~~\n'
        instruction = line1 + line2 + line3 + line4 + line5 + line6 + line7      
        return instruction

if __name__ == '__main__':
    pass

