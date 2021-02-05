class Annie:
    def __init__(self,health, mana,ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
        
    
    def tibbers(self):
        print('티버: 피해량 ',self.ability_power*0.65+400)
        
in