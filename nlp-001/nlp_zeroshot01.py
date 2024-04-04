# Using python 3.10.13

from transformers import pipeline


espanol_txt   = "Necesito configurar la direccion IP del servidor"
espanol_label = ["cocina", "clima", "Linux", "informatica"]

ingles_txt    = "I need to update the server's IP addres"
ingles_label  = ["sport", "weather", "tech", "Linux", "Computer"]

model_type  = pipeline("zero-shot-classification")
resultado   = model_type(ingles_txt, candidate_labels=ingles_label,)

print(resultado)