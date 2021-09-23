
def make_request(error):
    import requests
    print("Searching for your error in StackOverflow")
    resp  = requests.get("https://api.stackexchange.com/"+"2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
    json_dict = resp.json()
    url_list = []
    count = 0
    for i in json_dict['items']:
        if i["is_answered"]:
            url_list.append(i["link"])
        count+=1
    return url_list

    
a = make_request("AttributeError: 'NoneType' has no attribute")
print(a)