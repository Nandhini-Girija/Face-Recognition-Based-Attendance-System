import cognitive_face as CF
from global_variables import personGroupId

Key = '6b2222d0eb264de99fb64b95ef49b851'
CF.Key.set(Key)
BASE_URL = 'https://centralindia.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

res = CF.person_group.train(personGroupId)
print(res)
