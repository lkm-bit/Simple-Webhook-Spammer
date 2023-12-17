import requests, threading, time


url = input("Enter url: ")
payload = input("Enter payload: ")

def function():
    requests.post(url,json={'content': payload})

while True:
    function()
    time.sleep(0.7)
    print("Sent message! ShadyFb on top")
