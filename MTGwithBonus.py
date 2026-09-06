class MagicCard:
    DEFAULT_SET = "Core Set"
    def __init__(self, rarity, card_name, mana_cost, card_type, rules_text, artist, power=1):
        self.rarity = rarity
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.card_type = card_type
        self.rules_text = rules_text
        self.artist = artist
        self.power = power

Nine_Lives = MagicCard("Rare", "Nine Lives", 1, "Enchantment", "Hexproof\nIf a source would deal damage to you, prevent that damage and put an incarnation counter on Nine Lives.\nWhen there are nine or more incarnation counters on Nine Lives, exile it." \
"                       \nWhen Nine Lives leaves the battlefield, you lose the game.", "Paul Scott Canavan")
Pridemalkin = MagicCard("Common", "Pridemalkin", 2, "Creature", "When Pridemalkin enters the battlefield, put a +1/+1 counter on target creature you control.\nEach creature you control with a +1/+1 counter on it has trample."
"                       \nThey can deal excess combat damage to the player or planeswalker they're attacking.", "Karl Copinski")

Nine_Lives.power = 0

print("Set:", MagicCard.DEFAULT_SET)
print("Rarity:", Nine_Lives.rarity)
print("Card Name:", Nine_Lives.card_name)
print("Mana Cost:", Nine_Lives.mana_cost)
print("Power:", Nine_Lives.power)
print("Rules Text:", Nine_Lives.rules_text)
print("Artist:", Nine_Lives.artist)

print()
print()

print("Set:", MagicCard.DEFAULT_SET)
print("Rarity:", Pridemalkin.rarity)
print("Card Name:", Pridemalkin.card_name)
print("Mana Cost:", Pridemalkin.mana_cost)
print("Power:", Pridemalkin.power)
print("Rules Text:", Pridemalkin.rules_text)
print("Artist:", Pridemalkin.artist)