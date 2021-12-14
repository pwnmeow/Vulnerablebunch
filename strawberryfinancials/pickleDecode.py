import pickle
from base64 import b64decode

print(pickle.loads(b64decode(b'gANjaW50cm9kdWN0aW9uLnZpZXdzClRlc3RVc2VyCnEAKYFxAX1xAlgFAAAAYWRtaW5xA0sAc2Iu')))
