import json

with open('../160221.json', 'r',encoding="utf-8") as json_file:
    data = json.load(json_file)

for nop in data['NOP']:
    print(nop)



from datetime import datetime
class NOP:
    def __init__(self, date, wojewodztwo, powiat, plec, objawy):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.wojewodztwo = wojewodztwo
        self.powiat = powiat
        self.plec = plec
        self.objawy = objawy
