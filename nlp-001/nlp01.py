# Using python 3.10.13

from transformers import pipeline

pipe_model = pipeline("sentiment-analysis")
resultado = pipe_model("No me gusta hacer ejercicio en la noche")

print(resultado)
