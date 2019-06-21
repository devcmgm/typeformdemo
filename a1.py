import json
import requests

res = requests.get('https://api.typeform.com/forms/BsW5wg/responses', headers={'Authorization': 'bearer 8GzVyxy7VYaBT1pCcL11ZRCZ9xych3Juxen33LcwSsiY' } )
data = res.json()

#with open('typeform.demo') as json_file:
#data = json.load(json_file)

for a1 in data["items"]:
    if (a1["answers"] == "phone_number"):
       print("phone:" + a1["phone_number"])
    print(a1)


if not isinstance(data, dict):
    for key in data["items"]:
       for V1 in key["answers"]:
          for V2 in V1:
            if (V2 == "phone_number"):
               print("phone:" + V1["phone_number"])
            elif (V2 == "choice"):
               print("________________________")
               for choice in V1["choice"]:
                 if isinstance(V1["choice"], dict):
                    print("V1:" + str(V1["choice"]["label"]))
            elif (V2 == "email"):
               print("email:" + V1["email"])
               print("________________________")
            
