import spacy

npl = spacy.load('es_core_news_lg')
operaciones = {"suma": "+", "resta": "-"} # Aca deberia ir la palabra raiz nomas
doc = npl(u'Resolvé la suma de 140, 3731, 45, 46')
problema = []
for token in doc:
  if token.pos_ in ["NOUN", "NUM"]:
    problema.append(token)
  # print(f"{token.text:{10}} {token.pos_:{10}} {token.is_stop:{10}} {spacy.explain(token.tag_)}")

# print(problema)

def traduccion(token):
  if token.pos_ == "NOUN":
    return (operaciones[token.text], token)
  else: return (token.text, token)

problema_traducido = list(map(traduccion, problema))

# print(problema_traducido)

problema_traducido2 = []

for palabra, token in problema_traducido:
  if token.pos_ == "NOUN":
    noun = palabra
  else:
    problema_traducido2.append(palabra)
    problema_traducido2.append(noun)

problema_traducido2.pop()

# print(problema_traducido2)

mi_ecuacion = ' '.join(problema_traducido2)
print("Mi ecuacion para profe bot es: " + mi_ecuacion)