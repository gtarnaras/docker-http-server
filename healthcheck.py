import sys, requests

endpoint_check = "http://0.0.0.0:8080"

try:
    resp = requests.head(endpoint_check)
    print(resp.status_code)
    sys.exit(0) # return code 0 = healthy
except requests.ConnectionError:
    print("failed to connect")
    sys.exit(1) # return code 1 = unhealthy
