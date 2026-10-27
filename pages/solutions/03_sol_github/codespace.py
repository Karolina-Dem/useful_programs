characters = [
    ("Spider-Man", "Marvel Comics"),
    ("Batman", "DC Comics"),
    ("Wonder Woman", "DC Comics"),
    ("Asteriks", "Asteriks"),
    ("Naruto Uzumaki", "Naruto"),
    ("Son Goku", "Dragon Ball"),
    ("Sailor Moon", "Czarodziejka z Księżyca"),
    ("Monkey D. Luffy", "One Piece"),
    ("Totoro", "Mój sąsiad Totoro"),
    ("Mikasa Ackerman", "Atak Tytanów"),
]

for number, (name, series) in enumerate(characters, start=1):
    print(f"{number}. {name} — {series}")
