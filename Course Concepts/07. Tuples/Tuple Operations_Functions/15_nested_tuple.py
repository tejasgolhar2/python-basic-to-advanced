clubs = (("FC Barcelona", "Spain", 1899,
            [
                (3, "Pique"),
                (5, "Busquets"),
                (7, "Dembele"),
            ]
         ),
         ("Real Madrid CF", "Spain", 1902,
            [
                (7, "Hazard"),
                (9, "Benzema"),
                (10, "Modric"),
            ]
         ),
         ("Manchester United FC", "England", 1878,
            [
                (6, "Pogba"),
                (7, "Ronaldo"),
                (14, "Lingard"),
            ]
         ),
         ("Arsenal FC", "England", 1886,
            [
                (7, "Lacazette"),
                (14, "Aubameyang"),
                (16, "Holding"),
            ]
         ),
         )

# Formatting of Nested TUples

for team_name,country,year,players in clubs:
    print(f"Team Name:{team_name},Country:{country},Year:{year},Players:{players}")

# Accessing elements of Nested TUples using concept of INdexing
