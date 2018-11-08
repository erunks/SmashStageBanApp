class StageDownloader:
    def __init__(self,jsonFile):
        self.stages = self.loadJSON(jsonFile)
        self.downloadStages()

    def loadJSON(self,file):
        import json
        temp=open(file).read()
        return json.loads(temp)

    def downloadImage(self,host,local,fileName):
        from pathlib import Path
        my_file = Path(local+fileName)
        if my_file.is_file():
            print(fileName + ' exists. Skipping.')
            return

        import requests
        img_data = requests.get(host+url).content
        with open(host+fileName, 'wb') as handler:
            handler.write(local+img_data)
            print('Downloaded ' + fileName)

    def downloadStages(self):
        host = self.stages["0"]["origin"]
        local = self.stages["0"]["local"]
        for i in range(len(self.stages)):
            self.downloadImage(host,local,self.stages[str(i)]['image'])
            self.downloadImage(host,local,self.stages[str(i)]['thumb'])

import sys
if(len(sys.argv) < 2):
    return -1
    
SD = StageDownloader(sys.argv[1])
