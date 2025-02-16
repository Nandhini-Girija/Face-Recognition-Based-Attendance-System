import cognitive_face as CF
from global_variables import personGroupId
import sys

Key = '6b2222d0eb264de99fb64b95ef49b851'
CF.Key.set(Key)
BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)
personGroups = CF.person_group.lists()
for personGroup in personGroups:
    if personGroupId == personGroup['personGroupId']:
        print(personGroupId + " already exists.")
        sys.exit()

res = CF.person_group.create(personGroupId)
print(res)
