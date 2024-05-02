def getTempoViagem(hx,mx,hy,my):

    sentido = 1
    if hy >= hx:
        total = (hy-hx)*60
    else:
        total = (24-hx+hy)*60

    if mx >= my:
        total += mx-my
    else:
        total += 60-mx+my

    if total > 12*60:
        total = 1440 - total
        sentido = -1

    return total,sentido


pa,cb,pb,ca = input().split()

hpa,mpa = pa.split(':')
hpa = int(hpa)
mpa = int(mpa)

hcb,mcb = cb.split(':')
hcb = int(hcb)
mcb = int(mcb)

hpb,mpb = pb.split(':')
hpb = int(hpb)
mpb = int(mpb)

hca,mca = ca.split(':')
hca = int(hca)
mca = int(mca)

tempoIda,sentidoIda = getTempoViagem(hpa,mpa,hcb,mcb)

tempoVolta,sentidoVolta = getTempoViagem(hpb,mpb,hca,mca)

print(f'tempo ida {tempoIda} [{sentidoIda}] tempoVolta {tempoVolta} [{sentidoVolta}]')

if sentidoIda == 1 and sentidoVolta == 1:

    fuso = sentidoIda*(tempoIda - tempoVolta)//120
    print(f'{tempoIda-fuso*60} {fuso}')



#if tempoIda > tempoVolta:

#    fuso = sentidoIda*(tempoIda - tempoVolta)//120
#    print(f'{tempoIda-fuso*60} {fuso}')

#else:

#    fuso = sentidoIda*(tempoVolta - tempoIda)//120
#    print(f'{tempoVolta-fuso*60} {-fuso}')



