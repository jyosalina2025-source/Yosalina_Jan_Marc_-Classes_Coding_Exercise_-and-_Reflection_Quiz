class MagicCard:
    
    DEFAULT_SET = "Core Set"
    
    def __init__(self, card_name, mana_cost, power=1):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.power = power

Nine_Lives = MagicCard("Nine Lives", 1)
Pridemalkin = MagicCard("Pridemalkin", 2)

Nine_Lives.power = 0

print("Card Name:", Nine_Lives.card_name)
print("Mana Cost:", Nine_Lives.mana_cost)
print("Set:", MagicCard.DEFAULT_SET)
print("Power:", Nine_Lives.power)

print()
print()

print("Card Name:", Pridemalkin.card_name)
print("Mana Cost:", Pridemalkin.mana_cost)
print("Set:", MagicCard.DEFAULT_SET)
print("Power:", Pridemalkin.power)