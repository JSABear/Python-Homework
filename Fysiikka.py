
dt = 0.05 # aikavälin pituus (s)
time = [0.0] # ensimmäinen alkio (s)
x = [0.0] #
acc = [3.0] # ensimmäinen alkio (m/s^2)

while (time[-1] + dt < 10.0):
    time.append(time[-1] + dt)
    if (time[-1] < 2.0):
        acc.append(3.0)
    elif (time[-1] < 7.0):
        acc.append(0.0)
    else:
        acc.append(-2.0)


while (time[-1] + dt < 10.0):
    time.append(time[-1] + dt)
    if (time[-1] < 2.0):
        x.append(acc[4]-acc[0])
    elif (time[-1] < 7.0):
        x.append(6+x[-1])
    else:
        x.append(acc[12]-acc[19])

print (x)
print (acc)
#for i in range(10): # tulostetaan listojen 5 ensimmäistä alkiota  x.append((acc[4]-acc[0])/2+x[-1])
    #print('Aika =',time[i],'s, kuljettu matka =',x[i],'m')