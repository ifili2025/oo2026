import urllib.request

fsisu = urllib.request.urlopen('https://oop2026.igorfilippov.eu/1kodutoo.txt').read().decode("utf-8")
andmeread = fsisu.split("\n")[1:] 
andmeread = [rida.strip().split(",") for rida in andmeread if rida.strip()]
def meeskonna_punktid(team):
    home_point = 0
    away_point = 0
    game_count = 0
    for rida in andmeread:
        if rida[0] == team:
            game_count += 1
            if int(rida[2]) > int(rida[3]):
                home_point += 3
            elif int(rida[2]) == int(rida[3]):
                home_point += 1
        if rida[1] == team:
            game_count += 1
            if int(rida[3]) > int(rida[2]):
                away_point += 3
            elif int(rida[3]) == int(rida[2]):
                away_point += 1            
    return game_count,home_point, away_point

team = str(input('Sisesta meeskonna nimi, siis annan sulle selle meeskonna kogupunktid praegusel hooajal: '))
game_count, home, away = meeskonna_punktid(team)
print(team, "sellel hooajal omab", home + away, "punktid, nendest tuli", home, "punkti kodumängudest ja", away, "punkti välimängudest ja kokku mängiti", game_count, "mängu. Max võimalik punktide arv võiks olla", game_count * 3)



