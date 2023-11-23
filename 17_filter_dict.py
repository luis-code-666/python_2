matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

partido_ganador = list(filter(lambda item: item['home_team_result'] == 'Win' ,matches))
print(partido_ganador)
print(len(partido_ganador))



def filter_by_length(words):
   # Escribe tu solución 👇
   numandletras = list(filter(lambda word: len(word) >=4, words))
   return numandletras

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)