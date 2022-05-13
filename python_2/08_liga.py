class Spieler:
    def __init__(self, name, alter, karriereStart, gehalt, position):
        self.name = name
        self.alter = alter
        self.karriereStart = karriereStart
        self.gehalt = gehalt
        self.position = position

    def __str__(self) -> str:
        return "{} ist {} Jahre alt und verdient {}€".format(self.name, self.alter, self.gehalt)


class Team:
    def __init__(self, name):
        self.name = name
        self.tore = 0
        self.spielerListe = []

    def meldeSpielerAn(self, spieler):
        self.spielerListe.append(spieler)

    def printTeam(self):
        for spieler in self.spielerListe:
            print(spieler)

    def __str__(self):
        return "{} hat {} Tore geschossen!".format(self.name, self.tore)


class Liga:
    def __init__(self, name):
        self.__name = name
        self.__teams = []

    def __str__(self):
        return self.__name

    def meldeAn(self, team):
        self.__teams.append(team)

    def spiele(self, team1, team2, toreTeam1, toreTeam2):
        team1.tore += toreTeam1
        team2.tore += toreTeam2

    def printTabelle(self):
        empty_dict = {}

        for team in self.__teams:
            empty_dict[team.name] = {"goals": team.tore}

        print(empty_dict)


liga = Liga("Bundesliga")

t1 = Team("Bayern")
t2 = Team("Dortmund")
t3 = Team("Leverkusen")
t4 = Team("Leibzig")
t5 = Team("FC Freiburg")
t6 = Team("Union Berlin")

s1 = Spieler("Peter", 20, 2016, 5, "Stürmer")
s2 = Spieler("Günther", 21, 2015, 6, "Abwehr")
s3 = Spieler("Hans", 40, 2005, 0, "Torwart")

t1.meldeSpielerAn(s1)
t1.meldeSpielerAn(s2)
t1.meldeSpielerAn(s3)

print(t1.printTeam())

liga.meldeAn(t1)
liga.meldeAn(t2)
liga.meldeAn(t3)
liga.meldeAn(t4)
liga.meldeAn(t5)
liga.meldeAn(t6)

liga.spiele(t1, t2, 3, 2)
liga.spiele(t3, t2, 1, 0)
liga.spiele(t4, t2, 2, 1)
liga.spiele(t1, t3, 0, 2)
liga.spiele(t4, t3, 1, 1)
liga.spiele(t1, t4, 2, 2)
liga.spiele(t5, t6, 2, 1)
liga.spiele(t1, t6, 3, 1)
liga.spiele(t3, t5, 0, 1)

liga.printTabelle()
