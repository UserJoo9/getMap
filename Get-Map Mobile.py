import os

try:
    import phonenumbers
    from phonenumbers import carrier
    import geocoder
    import folium
    import requests

except:
    os.system('pip install phonenumbers')
    os.system('pip install geocoder')
    os.system('pip install folium')
    os.system('pip install requests')

def getLocation():
    global our_map, ip
    try:
        ip = input("\nEnter Target IP: ")
        if ip == '':
            print("\nIP Can't Empty!")
        elif ip.isalpha() or ip.startswith(' ') or ip.startswith('192') or ip.startswith('127') or ip.startswith('169') or ip.startswith('172.16') or ip.startswith('172.32') or ip.startswith('10') or ip.startswith('255') or ip.startswith('254'):
            print("Invalid IP!")
            print("الايبي غلط!")
        else:
            our_ip = geocoder.ip(ip)
            location = our_ip.latlng
            our_map = folium.Map(location=location, zoom_start=10)
            folium.Marker(location).add_to(our_map)
            print("Server Coordination in Map: ",location)
            print("To Save Location As HTML File Press 'Y', or Else to cancel")
            switch = input(">> ")
            if switch.upper() == "Y":
                saveLocation()
            else:
                pass
    except:
        print("\ncan't get ip info, try again!")


def saveLocation():
    try:
        our_map.save(f"{ip}_map.html")
        print("HTML File has been Saved!")
    except:
        print("\nCan't save file, try again later.")


def getInfoByNumber():
    try:
        phoneNumber = input("\nEnter Phone Number (With Country Code): ")
        if phoneNumber == '' or phoneNumber.startswith(" "):
            print("\nPhone Number is Wrong!")
        elif not phoneNumber.startswith("+"):
            print("Phone Number Must Starts With '+'")
        else:
            service_pro = phonenumbers.parse(phoneNumber)
            service_provider = carrier.name_for_number(service_pro, "en")
            print("Carrier: ", service_provider)
    except:
        print("\nCan't Get Number Carrier!")

# def qrCodeGEnrator():
#     link = input("Enter Target: ")
#     nameOfCode = input("Enter Name Of QRCode: ")
#     try:
#         if link != '' and nameOfCode !='':
#             qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2,)
#             qr.add_data(link)
#             qr.make(fit=True)
#             img = qr.make_image()
#             img.save(f'{nameOfCode}.png')
#             filePath=os.getcwd()+'\\'+nameOfCode+'.png'
#             print("Saved In Path: ", filePath)
#
#         else:
#             print("You Must Type Target and Name for it to Generate QrCode")
#             qrCodeGEnrator()
#     except:
#         print("An Error, try again later or choose another name")


print("\n************** Get-Map **************\n")
print("Welcome to Get-Map\n")
while 1:
    try:
        switch = requests.get("https://pastebin.com/raw/WxHWL0m7").text
        pwd = input("\nPassword: ")
        if pwd == switch:
            print("Welcome !!\nاهلا بيك في برنامج جيت ماب, لا تستخدم البرنامج في ما لا يرضي الله")
            print("")
            while 1:
                print("1- Get Map From IP")
                print("2- Get Number Carrier")
                print("3- Exit")
                choose = input(">> ")
                if choose == '1':
                    getLocation()
                elif choose == '2':
                    getInfoByNumber()
                elif choose == '3':
                    break
                else:
                    print("Unknown Option!")
        else:
            print("Password is wrong!!\nالباسورد غلط متحاولش فيه كتير")
            print("")
            print("افتح الموقع شوف التحديثات الجديده")
            print("https://userjoo9.github.io/youssefinfo/#main")
    except:
        print("Check internet connection!")
        print("اتاكد ان الانترنت شغال!")
        break