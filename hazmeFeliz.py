import requests
from PIL import Image
from constants import API_kEY


# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = API_kEY
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json() #devuelve la información conseguida en formato Json, esta
        #información viene ordenada de mayor a menor coincidencia en la interpretación. 
        print(responseData)
        topMatch = responseData[0] #tomamos el primer valor de la lista que es el que mayor probabilidad tiene de ser
        #la respuesta correcta. 
        return topMatch
    else:
        response.raise_for_status()


'''
# CHANGE THIS to something you want your machine learning model to classify
demo = classify("The text that you want to test")

label = demo["class_name"]
confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))
'''


def run():
    mensaje = input("¿Que quieres decirme? ") #Pedimos al usuario que nos diga algo. 

    recognized = classify(mensaje) #Pasamos el mensaje a la función de clasificación de aprendizaje
    #Dicha función devolverá un diccionario en formato Json, el cual asignamos el valor de class_name
    #a label que nos servirá para devolver el mensaje al usuario. 
    print(recognized)
    label = recognized["class_name"]

    if label == "cosas_buenas":
        print("Eres muy agradable. ¡Gracias!")
        img = Image.open("img/feliz.jpg")
        img.show()

    else:
        print("¡No me simpatizas!")
        img = Image.open("img/triste.jpg")
        img.show()



if __name__ == '__main__':
    run()