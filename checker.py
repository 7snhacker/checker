def log():
    print("""
                                                  
      ,--.                  ,--.                  
 ,---.|  ,---.  ,---.  ,---.|  |,-. ,---. ,--.--. 
| .--'|  .-.  || .-. :| .--'|     /| .-. :|  .--' 
\ `--.|  | |  |\   --.\ `--.|  \  \\   --.|  |    
 `---'`--' `--' `----' `---'`--'`--'`----'`--'    
                                                  
""")
    print("                    by 7snhacker")
    print("")
    import requests
    import tkinter
    import time
    from tkinter import messagebox
    root = tkinter.Tk()
    root.withdraw()
    user = open("list.txt","r")
    sleep = input("sleep : ")
    sleep = float(sleep)
    while True:
        lst = user.readline().split('\n')[0]
        time.sleep(sleep)
        headers = {
            'authority': 'www.instagram.com',
            'x-ig-www-claim': 'hmac.AR08hbh0m_VdJjwWvyLFMaNo77YXgvW_0JtSSKgaLgDdUu9h',
            'x-instagram-ajax': '82a581bb9399',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'user-agent': '',
            'x-requested-with': 'XMLHttpRequest',
            'x-csrftoken': 'rn3aR7phKDodUHWdDfCGlERA7Gmhes8X',
            'x-ig-app-id': '936619743392459',
            'origin': 'https://www.instagram.com',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.instagram.com/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cookie': ''


        }
        data = {
            'username': lst,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:sffdsfdsfdffrd'
        }
        url = "https://www.instagram.com/accounts/login/ajax/"
        r = requests.post(url,headers=headers,data=data).text
        if ('"user":true') in r:
            print("Not Avaiable [!] : ",lst)
        elif ('"user":false') in r:
            print("Avaiable [*] : ",lst)
            messagebox.showinfo("7snhacker", f'Avaiable : {lst}')
            input()
            break

log()

