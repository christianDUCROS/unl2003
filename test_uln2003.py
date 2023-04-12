#programme principal
import uln2003
import time

moteur1 = uln2003.ULN2003 (0,1,2,3) 
moteur2 = uln2003.ULN2003 (4,5,6,7)

#test de connectique : clignoter les leds
print("reset")
moteur1.reset()
time.sleep(1)
print("set")
moteur1.on()
time.sleep(1)


while (True):
    #500pas, sens horaire(-1), halfstep(0), periode de 10ms entre chaque pas  
    moteur1.rotation(500,-1,0,10)
    #90 degres sens horaire(-1), fullstep(1) periode de 10ms entre chaque pas  
    moteur1.angle(90,-1,1,10)
    #500pas, sens horaire(1),fullstep(1) periode de 100ms entre chaque pas  
    moteur1. rotation(500,1,1,100)
