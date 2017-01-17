#create linear regression with physics as
#linear independent variable
physics=[15,12,8,8,7,7,7,6,5,3]
history=[10,25,17,11,13,17,20,13,9,15]
n=len(physics)
xBar=sum(physics)/n
yBar=sum(history)/n
num=0
den=0
for i in range(n):
    xDist=physics[i]-xBar
    yDist=history[i]-yBar
    num+=xDist*yDist
    den+=xDist**2
beta=num/den
alpha=yBar-beta*xBar
regEquation='history= '+str(alpha)+'+'+str(round(beta,4))+'physics'
print(regEquation)
