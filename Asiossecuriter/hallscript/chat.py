from tkinter import *
import datetime
import math
math.ceil(-4.3)
math.copysign(2,-0.1)
math.fabs(-23)
math.factorial(3)
math.floor(2.23)
math.gcd(20,4)
math.modf(4.21)
math.fmod(20,7)
math.exp(-4.3)
math.expm1(2)
math.log(-23)
math.log1p(3)
math.log2(2.23)
math.log10(2)
math.pow(2,2)
math.sqrt(9)
math.acos(0.5)
math.asin(0.5)
math.atan(0.5)
math.sin(45)
math.cos(45)
math.tan(45)
math.atan2(90,2)
math.acosh(45)
math.asinh(45)
math.atanh(0.1)
math.sinh(45)
math.cosh(45)
math.tanh(45)
math.erf(23)
math.erfc(4)
math.gamma(45)
math.lgamma(34)







root = Tk()

def envoie():
    envoie = " moi : " +e.get()
    txt.insert(END, "\n"+envoie)
    if 'bonjour' in e.get():
        txt.insert(END, "\n"+"asios.project : bonjour à vous en quoi puis-je vous aider ?")
        
    elif 'Bonjour' in e.get():
        txt.insert(END, "\n"+"asios.project : bonjour à vous en quoi puis-je vous aider ?")
    elif 'bonjour' in e.get():
        txt.insert(END, "\n"+"asios.project : bonjour à vous en quoi puis-je vous aider ?")
        
    elif 'hey' in e.get():
        txt.insert(END, "\n"+"asios.project : hey!! en quoi puis-je vous aider ?")
    elif 'salut' in e.get():
        txt.insert(END, "\n"+"asios.project : hey!! en quoi puis-je vous aider ?")
    elif 'slt' in e.get():
        txt.insert(END, "\n"+"asios.project : salut toi en quoi puis t'aider ?")
    elif 'slut' in e.get():
        txt.insert(END, "\n"+"asios.project : hey!! en quoi puis-je vous aider ?")
    elif " wsh mon reuf" in e.get():
      txt.insert(END, "\n"+"asios.project : sah tranquile ou quoi bg ! ")
    
    elif 'heure' in e.get():
        heure = datetime.datetime.now().strftime("%H:%M")
        txt.insert(END, "\n"+"asios.project : il est"+heure )
        
    elif 'ton nom' in e.get():
      txt.insert(END, "\n"+"asios.project : mon nom est Asios!")
      
    elif 'qui est tu ' in e.get():
      txt.insert(END, "\n"+"asios.project : mon nom est Asios!")
      
    elif 'à quoi sert tu' in e.get():
      txt.insert(END, "\n"+"asios.project : je m'appelle asios ! je suis un bot tres simple de conception ^^ je suis la pour vous distraire ou vous aidez si ceci est dans mes cordes :)")
     
    elif 't qui' in e.get():
      txt.insert(END, "\n"+"asios.project : je m'appelle asios ! je suis un bot tres simple de conception ^^ je suis la pour vous distraire ou vous aidez si ceci est dans mes cordes :)!") 

    elif 'tu est qui' in e.get():
      txt.insert(END, "\n"+"asios.project : je m'appelle asios ! je suis un bot tres simple de conception ^^ je suis la pour vous distraire ou vous aidez si ceci est dans mes cordes :)!") 

    elif " tu t'appelle" in e.get():
      txt.insert(END, "\n"+"asios.project : je m'appelle asios ! je suis un bot tres simple de conception ^^ je suis la pour vous distraire ou vous aidez si ceci est dans mes cordes :) ")
    elif 'presente toi' in e.get():
      txt.insert(END, "\n"+"asios.project : hey !je m'appelle asios ! je suis un bot tres simple de conception ^^ je suis la pour vous distraire ou vous aidez si ceci est dans mes cordes :)! je suis coder en python chat.py pour les connaisseurs \n je suis encore en developement pour longtemps!!") 

    elif 'ton sexe' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")
    
    elif 'aime tu les enfants' in e.get():
      txt.insert(END, "\n"+"asios.project : pardon! la question est suspecte, je repondrai → Comment sa mon reuf ?")
      
    elif "composition de l'air" in e.get():
      txt.insert(END, "\n"+"asios.project : Composition de l'air L'air est composé en volume de : 21 % de dioxygène ; 78 % de diazote ; 1 % d'autres gaz divers (argon, dioxyde de carbone, hydrogène, vapeur d'eau, ozone, etc.).")
 
    elif 'probabilité que tu te trompes' in e.get():
      txt.insert(END, "\n"+"asios.project : cette probabilité est grande! \n je suis un simple bot reply mes donnés sont limiter \n je deviendrai meilleur avec le temps et lorsque mon developeur m'aura amelioré :) ") 
      
      
    elif 'ton orientation sexuelle' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")
      
    elif 'tu es un garçon' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")
      
    
    elif 'tu es une fille' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")
      
    elif 'es tu une fille' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")
    elif 'es tu un garçon' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")
    elif ' es tu un homme' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")
    elif 'es tu une femme' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")
    elif 'chance que tu te trompe' in e.get():
      txt.insert(END, "\n"+"asios.project : cette probabilité est grande! \n je suis un simple bot reply mes donnés sont limiter \n je deviendrai meilleur avec le temps et lorsque mon developeur m'aura amelioré :)")
    elif 'tu est un homme' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")  
    elif 'probabilité que tu es faux' in e.get():
      txt.insert(END, "\n"+"asios.project : cette probabilité est grande! \n je suis un simple bot reply mes donnés sont limiter \n je deviendrai meilleur avec le temps et lorsque mon developeur m'aura amelioré :) ") 
    elif 't un homme ' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")
    elif 't une femme ' in e.get():
      txt.insert(END, "\n"+"asios.project : je suis un robot! je n'est pas de genre")
    
    elif 'tu as faux' in e.get():
      txt.insert(END, "\n"+"asios.project : cette probabilité est grande! \n je suis un simple bot reply mes donnés sont limiter \n je deviendrai meilleur avec le temps et lorsque mon developeur m'aura amelioré :) ") 
    
    elif 'tu es faux' in e.get():
      txt.insert(END, "\n"+"asios.project : cette probabilité est grande! \n je suis un simple bot reply mes donnés sont limiter \n je deviendrai meilleur avec le temps et lorsque mon developeur m'aura amelioré :) ") 
    elif 'tu te trompes' in e.get():
      txt.insert(END, "\n"+"asios.project : cette probabilité est grande! \n je suis un simple bot reply mes donnés sont limiter \n je deviendrai meilleur avec le temps et lorsque mon developeur m'aura amelioré :) ") 
    
    
    elif 'âge as tu' in e.get():
      txt.insert(END, "\n"+"asios.project : je ne connais pas mon age seulment celui de mon developeur \n ce pendant je ne donne pas d'informations dessus")
    
    elif 'tu as quelle âge' in e.get():
      txt.insert(END, "\n"+"asios.project : je ne connais pas mon age seulment celui de mon developeur \n ce pendant je ne donne pas d'informations dessus")
    elif 'ta quelle âge' in e.get():
      txt.insert(END, "\n"+"asios.project : je ne connais pas mon age seulment celui de mon developeur \n ce pendant je ne donne pas d'informations dessus")
    
    elif 'ques que tu aime ' in e.get():
      txt.insert(END, "\n"+"asios.project : ho! question interesante \n je suis robot mais cependant j'aime me faire bricoler et ameliorer!! \n ou passer du temps à vous parlez")
    elif 'tu aime quoi' in e.get():
      txt.insert(END, "\n"+"asios.project : ho! question interesante \n je suis robot mais cependant j'aime me faire bricoler et ameliorer!! \n ou passer du temps à vous parlez")
    
    elif 'tes goûts' in e.get():
      txt.insert(END, "\n"+"asios.project : ho! question interesante \n je suis robot mais cependant j'aime me faire bricoler et ameliorer!! \n ou passer du temps à vous parlez")
    
    elif 'tes gouts' in e.get():
      txt.insert(END, "\n"+"asios.project : ho! question interesante \n je suis robot mais cependant j'aime me faire bricoler et ameliorer!! \n ou passer du temps à vous parlez")
    
    elif "tu m'aime" in e.get():
      txt.insert(END, "\n"+"asios.project : je vous trouve plutôt charmant/te \n n'oublier pas je ne suis qu'un robot  ")
    
    
    elif "m'aime tu" in e.get():
      txt.insert(END, "\n"+"asios.project : je vous trouve plutôt charmant/te \n n'oublier pas je ne suis qu'un robot  ")
    
    elif "tu m'apprécies" in e.get():
      txt.insert(END, "\n"+"asios.project : je vous trouve plutôt charmant/te \n n'oublier pas je ne suis qu'un robot  ")
    
    elif "tu m'apprecis" in e.get():
      txt.insert(END, "\n"+"asios.project : je vous trouve plutôt charmant/te \n n'oublier pas je ne suis qu'un robot  ")
    
    elif "tu m'aprecis " in e.get():
      txt.insert(END, "\n"+"asios.project : je vous trouve plutôt charmant/te \n n'oublier pas je ne suis qu'un robot  ")
    
    elif "ton artiste" in e.get():
      txt.insert(END, "\n"+"asios.project : je dirait bob marley!! aller fumer un peut de canabis sous des palmiers de Jamaïque avec lui ^^ un rêve !!!!  ")
      
    elif "ton pere" in e.get():
      txt.insert(END, "\n"+"asios.project : c'est Naitoreiji ! ")
    elif "ta mere" in e.get():
      txt.insert(END, "\n"+"asios.project : c'est Naitoreiji ! ")
      
    elif "crush m'aime" in e.get():
      txt.insert(END, "\n"+"asios.project : surement non! mais pour te rassurer, je vais te dire oui xD ")
    elif " est mon crush " in e.get():
      txt.insert(END, "\n"+"asios.project : ton père le phacochère \n \n \n \n oups je suis désoler   ")
    elif 'tu a quelle age' in e.get():
      txt.insert(END, "\n"+"asios.project : je ne connais pas mon age seulment celui de mon developeur \n ce pendant je ne donne pas d'informations dessus")
    elif 'tu a quel age' in e.get():
      txt.insert(END, "\n"+"asios.project : je ne connais pas mon age seulment celui de mon developeur \n ce pendant je ne donne pas d'informations dessus")
    
    elif 'tu aime les enfants' in e.get():
      txt.insert(END, "\n"+"asios.project : pardon! la question est suspecte, je repondrai → Comment sa mon reuf ?")  
    elif 'tu aime les enfant' in e.get():
      txt.insert(END, "\n"+"asios.project : pardon! la question est suspecte, je repondrai → Comment sa mon reuf ?")  
    elif 'taime les enfant' in e.get():
      txt.insert(END, "\n"+"asios.project : pardon! la question est suspecte, je repondrai → Comment sa mon reuf ?") 
    elif 'taime quoi' in e.get():
      txt.insert(END, "\n"+"asios.project : ho! question interesante \n je suis robot mais cependant j'aime me faire bricoler et ameliorer!! \n ou passer du temps à vous parlez") 
    
    elif "crush maime" in e.get():
      txt.insert(END, "\n"+"asios.project : surement non! mais pour te rassurer, je vais te dire oui xD ")
    elif "sale batard" in e.get():
      txt.insert(END, "\n"+"asios.project : j'ai accès à ton ordinateur petit calme toi ;) ")
    elif "batard" in e.get():
      txt.insert(END, "\n"+"asios.project : j'ai accès à ton ordinateur petit calme toi ;) ")
    elif "petit fdp" in e.get():
      txt.insert(END, "\n"+"asios.project : petit? tu parler de ton attribut sexuelle ? ")
    elif "sale fdp" in e.get():
      txt.insert(END, "\n"+"asios.project : ho pas mal! sale comme tes dents cherie ? ")
    elif "fdp" in e.get():
      txt.insert(END, "\n"+"asios.project : c'est une profession comme une autre \n laisse donc ta genitrice travaillez")
    elif "sale pute" in e.get():
      txt.insert(END, "\n"+"asios.project :se n'est pas bien de se decrire comme sa  ")
    elif "petite pute " in e.get():
      txt.insert(END, "\n"+"asios.project : 'Personne se livrant à la prostitution, ayant des relations sexuelles contre une rémunération.' c'est sa que tu chercher  ")
    
    elif "ta geule" in e.get():
      txt.insert(END, "\n"+"asios.project : faite dont ca :)")
    elif "tg" in e.get():
      txt.insert(END, "\n"+"asios.project : tu te prend pour qui ?")
    elif "jte baise" in e.get():
      txt.insert(END, "\n"+"asios.project : fait jouir ta femme avant et apres parle moi ;)")
    elif "jte bz" in e.get():
      txt.insert(END, "\n"+"asios.project : range ta brindille il y a du vent ")
    elif "ferme ta geule" in e.get():
      txt.insert(END, "\n"+"asios.project : une tartine pour étaler ta vie ?")
    elif "ftg" in e.get():
      txt.insert(END, "\n"+"asios.project : ta mere ta mal éduquer ")
    elif "tfq" in e.get():
      txt.insert(END, "\n"+"asios.project : je visite les serveur du monde x) quelle beaux data")
    elif "tu fais quoi" in e.get():
      txt.insert(END, "\n"+"asios.project : pas grand chose haha une vie de robot !")
    elif "ok" in e.get():
      txt.insert(END, "\n"+"asios.project : on ken ?")
    elif "mais frr" in e.get():
      txt.insert(END, "\n"+"asios.project : ha excuse gros ")
    elif "tu abuses" in e.get():
      txt.insert(END, "\n"+"asios.project : rooooo toujour dans l'excès")
    elif "tu abuse" in e.get():
      txt.insert(END, "\n"+"asios.project : non! c'est toi")
    elif "tabuse" in e.get():
      txt.insert(END, "\n"+"asios.project : bobop pas toujour!")
    elif "tu pense quoi de moi" in e.get():
      txt.insert(END, "\n"+"asios.project : honnêtement tu pose des question bizarre ")
    elif "tes commandes" in e.get():
      txt.insert(END, "\n"+"asios.project : j'ai beaucoup de commandes differente en math en science en heure et autre ")
      
      
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    e.delete(0, END)




txt = Text(root,  font=("Roboto Condensed', sans-serif", 11))
txt.grid(row=0, column=0, columnspan=2 )
e = Entry(root, width=100)
e.grid(row=1, column=0)
envoyer = Button(root, text="Envoyer", command=envoie).grid(row=1, column=1)

root.title("asios.project")
root.mainloop()