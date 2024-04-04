# Using python 3.10.13

from transformers import pipeline

text_esp  = "En este articulo aprenderas a configurar la direccion IP con el comando ip de linux"
text_eng  = "This article will help you understand the universe"

genera    = pipeline("text-generation")
resultado = genera(text_eng)


print(resultado)

## resultado text_esp
## [{'generated_text': "En este articulo aprenderas a configurar la direccion IP con 
##  el comando ip de linux. This section is focused on the IP address of some of the
## servers that use a VPN connection. I'm not sure if this is"}]

## resultado text_eng
## [{'generated_text': 'This article will help you understand the universe of the human
## language as it is understood by the modern man.\n\nA word of advice from my own 
## fellow human beings\n\nPlease consider contributing to the discussion. If you want 
## to read all the details'}]