#Supacharn Kaowanan 653380026-4 Section-1
#PS : Partly psuedoed, unclear if implementation of utils is correct, Not expected to be executable, though the idea is there even if it's still a bit unclear.
from io import BytesIO
from requests.models import Response

def get_mock_THBtoKRW_api_response():
    mock_api_response = Response()
    mock_api_response.status_code = 200
    mock_api_response.raw = BytesIO(b'{'base' : 'THB','Result' : {'KRW' = 38.69} }')

    return mock_api_response
