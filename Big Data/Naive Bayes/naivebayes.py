import numpy

def likelihood(x,input):
    if(x=='ya'):
        jumlahPenyebut=hasilPrior[0]
    else:
        jumlahPenyebut=hasilPrior[1]

    totalKondisi=numpy.zeros(4)
    for i in l:  
        for j in range(4):
            if(i[j]==input[j] and i[4]==x):
                totalKondisi[j]+=1
    
    hasillikelihood=[]
    for i in range (len(totalKondisi)):
        hasillikelihood.append(totalKondisi[i]/jumlahPenyebut)
        
    return hasillikelihood

def prior():
    jumlahYa=0
    jumlahTidak=0
    for i in l:
        if(i[4]=='ya'):
            jumlahYa+=1
        else:
            jumlahTidak+=1
    priorYa=jumlahYa/len(l)
    priorTidak=jumlahTidak/len(l)
    return jumlahYa,jumlahTidak,priorYa, priorTidak

def posterior(prior,likelihood):
    hasilPosterior=prior
    for i in likelihood:
        hasilPosterior*=i
    return hasilPosterior

def perbandingan(posteriorA,posteriorB):
    kesimpulan=""
    if(posteriorA>posteriorB):
        kesimpulan='ya'
    else:
        kesimpulan='tidak'
    return kesimpulan

l=[]
l.append(['cerah','panas','tinggi','stabil','tidak'])
l.append(['cerah','panas','tinggi','labil','tidak'])
l.append(['mendung','panas','tinggi','stabil','ya'])
l.append(['hujan','sedang','tinggi','stabil','ya'])
l.append(['hujan','dingin','normal','stabil','ya'])
l.append(['hujan','dingin','normal','labil','tidak'])
l.append(['mendung','dingin','normal','labil','ya'])
l.append(['cerah','dingin','tinggi','stabil','tidak'])
l.append(['cerah','dingin','normal','stabil','ya'])
l.append(['hujan','sedang','normal','stabil','ya'])
l.append(['cerah','sedang','normal','labil','ya'])
l.append(['mendung','sedang','tinggi','labil','ya'])
l.append(['mendung','panas','normal','stabil','ya'])
l.append(['hujan','sedang','tinggi','labil','tidak'])

print('data latih:\n',l,'\n')

input = ['hujan','sedang','tinggi','labil']
print('data uji:\n',input,'\n')

hasilPrior = prior()

hasillikelihoodYa = likelihood('ya',input)
hasillikelihoodTidak = likelihood('tidak',input)

posteriorYa=posterior(hasilPrior[2],hasillikelihoodYa)
posteriorTidak=posterior(hasilPrior[3],hasillikelihoodTidak)

kesimpulan = perbandingan(posteriorYa,posteriorTidak)
print('kesimpulan:',kesimpulan)