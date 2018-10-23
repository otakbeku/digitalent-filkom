import numpy as np
import pandas as pd

data = pd.read_csv('data.csv')
cuaca = data['Cuaca']
suhu = data['Suhu']
kelembapan = data['Kelembapan']
arah_angin = data['Arah Angin']
play_tennis = data['Play Tennis']

# likelihood_play_tennis = [i/len(data) for i in play_tennis]
likelihood_suhu_tidak = sum(1 for k in data['Suhu'] if data['Play Tennis'][k] == 'tidak')
likelihood_suhu_ya = sum(1 for k in data['Suhu'] if data['Play Tennis'][k] == 'ya')
print(likelihood_suhu_tidak)
# likelihood_kelembapan = [i/len(data) for i in kelembapan]
# likelihood_arah_angin = [i/len(data) for i in arah_angin]