import requests

BASE_URL = "https://instagram-scraper-2022.p.rapidapi.com/ig"
headers = {
    "X-RapidAPI-Key": "eae1b73cb9mshc5dece8c05b7c84p172949jsned39caa145b8",
    "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
}
followers_list = []

def main(username):
    def getUserId(username):
        param = {"user": username}
        res = requests.get(f"{BASE_URL}/info_username/", headers=headers, params=param)
        data = res.json()
        if data.get('status', None) == "ok":
            return data.get('user').get('pk')

    def getUser(username):
        param = {"user": username}
        res = requests.get(f"{BASE_URL}/info_username/", headers=headers, params=param)
        data = res.json()
        if data.get('status', None) == "ok":
            return data.get('user')

    def getFollowers(userId, max_id=None):
        param = {'id_user': userId}
        if max_id is not None:
            param['next_max_id'] = max_id
        request = requests.get(f"{BASE_URL}/followers/", headers=headers, params=param)
        res = request.json()
        if res.get('status', None) == "ok" and res.get('next_max_id', None) is not None:
            users = res.get('users', [])
            public_users = [item for item in users if not item["is_private"]]
            followers_list.extend(public_users)
            print("fetched and again call")
            getFollowers(userId=userId, max_id=res.get('next_max_id'))
        elif res.get('status', None) == "ok":
            users = res.get('users', [])
            public_users = [item for item in users if not item["is_private"]]
            followers_list.extend(public_users)
            print("finished")

    user = getUserId(username)
    if user:
        print(f"User ID for {username}: {user}")
        getFollowers(userId=user)
        temp = []
        lista = []
        for i in followers_list:
            usr = getUser(i['username'])
            lista.append(usr)
            print(usr)
            print("run")
            if usr.get('public_email', None) is not None and usr.get('public_email', None) != "":
                temp = [
                    usr.get("username", ""),
                    usr.get("full_name", ""),
                    usr.get("follower_count", ""),
                    usr.get("public_email", ""),
                    usr.get("public_phone_country_code", ""),
                    usr.get("public_phone_number", ""),
                    usr.get("whatsapp_number", ""),
                ]
        print(lista)
        return lista
    else:
        print(f"Couldn't find user with username: {username}")

