
# You'll need to install PyJWT via pip 'pip install PyJWT' or your project packages file

import jwt
import time
from django.http import HttpResponse

METABASE_SITE_URL = "Metabase Web url"
METABASE_SECRET_KEY = "metabase secret key"




def embed_question(request):

  payload = {
    "resource": {"question": 35},
    "params": {
      
    },
    "exp": round(time.time()) + (60 * 10) # 10 minute expiration
  }
  token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
  
  iframeUrl = METABASE_SITE_URL + "/embed/question/" + token + "#bordered=true&titled=true"
  return HttpResponse(iframeUrl)








