import os
import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

try:
    import webbrowser
except:
    os.system('pip install webbrowser')

try:
    from PIL import Image
except:
    os.system('pip install Pillow')

try:
    import qrcode
except:
    os.system('pip install qrcode')

try:
    import phonenumbers
    from phonenumbers import carrier
    from phonenumbers import geocoder as geo
except:
    os.system('pip install phonenumbers')

try:
    import opencage
    from opencage.geocoder import OpenCageGeocode
except:
    os.system('pip install opencage')

try:
    import geocoder as gc
except:
    os.system('pip install geocoder')

try:
    import folium
except:
    os.system('pip install folium')

try:
    import requests
except:
    os.system('pip install requests')

#---------------------------- Location By Ip ----------------------------------#

def locationByIp(*args):
    global l1, l2, lx, ll, saveLocation, ipEntry, getIpButton
    LocationByIP.destroy()
    LocationByNumber.destroy()
    # GenrateQrCode.destroy()
    Menulabel.destroy()
    # exiT.destroy()
    Developer.destroy()
    l1 = tkinter.Label(top, text='Target IP', width=50, font='Arial 18 bold', bg='black', fg='red')
    l1.pack(pady=5)
    ipEntry = tkinter.Entry(top, width=20, font='Arial 14 bold', bg='gray', fg='black')
    ipEntry.pack()
    ipEntry.focus_set()
    ipEntry.bind('<Return>', getLocation)
    ipEntry.bind('<Escape>', BackFromIP)
    getIpButton = tkinter.Button(top, text='GET MAP', font='Arial 12 bold', activeforeground='gray', bg='red', width=15,
                                 command=getLocation)
    getIpButton.pack(pady=10)
    ll = Button(top, text='Back', width=10, font='Arial 10 bold', bg='black', fg='red',
                activeforeground='gray', command=BackFromIP)
    ll.pack()
    lx = tkinter.Label(top, text='Server Coordination on Map:-', width=50, font='Arial 14 bold', bg='black', fg='red')
    l2 = tkinter.Label(top, text='', width=50, font='Arial 14 bold', bg='black', fg='red')
    saveLocation = tkinter.Button(top, text='Save location html', font='Arial 11 bold', activeforeground='gray',
                                  bg='blue', width=20, command=saveLocati0n)


def getLocation(*args):
    global our_map, our_ip, saveLocation
    try:
        ip = ipEntry.get()
        if ip == '' or ip.startswith(' ') or ip.startswith('192') or ip.startswith('127') or ip.startswith('169') or ip.startswith('172.16') or ip.startswith('172.32') or ip.startswith('10') or ip.startswith('255') or ip.startswith('254'):
            messagebox.showwarning("IP Error", "Invalid IP Address.\n\nNote: Don't Type Any Private or Special Address!")
        else:
            our_ip = gc.ip(ipEntry.get())
            location = our_ip.latlng
            our_map = folium.Map(location=location, zoom_start=15)
            folium.Marker(location).add_to(our_map)
            if location == '' or location == ' ':
                messagebox.showerror('Error', "Can't Get Server Coordination!")
            else:
                lx.pack(pady=10)
                l2.pack()
                l2['text'] = location
                saveLocation.pack(pady=5)
    except:
        messagebox.showerror('Error', "can't get ip info, try again!")


def saveLocati0n(*args):
    global OpenHtml, ip, ipath
    ip = ipEntry.get()
    try:
        OpenHtml.destroy()
    except:
        pass

    try:
        ipath = filedialog.askdirectory(title="Save Location")
        if ipath == '' or ipath == ' ':
            messagebox.showwarning("Alert!", "You Not Select Any Directory!")
        else:
            if os.path.exists(f"{ipath}\{ip}_map.html"):
                messagebox.showwarning("Alert!","File Already Exists!")
            else:
                our_map.save(f"{ipath}\{ip}_map.html")
                messagebox.showinfo("Saved..!", "HTML File has been Saved!")
                sw = messagebox.askyesno("ASK!","Do You Want to Open The Location?")
                if sw == True:
                    webbrowser.open_new_tab(f"{ipath}\{ip}_map.html")
                else:
                    pass
            OpenHtml = Button(top, text='Open HTML', width=15, font='Arial 10 bold', bg='black', fg='blue',
                              activeforeground='gray', command=openHtmlFile)
            OpenHtml.pack(pady=5)
    except:
        messagebox.showerror('Save Error!!', "Can't save file, try again later.")

def openHtmlFile(*args):
    webbrowser.open_new_tab(f"{ipath}\{ip}_map.html")

def BackFromIP(*args):
    global l1, l2, lx, ll, saveLocation, ipEntry, getIpButton, OpenHtml
    l1.destroy()
    l2.destroy()
    lx.destroy()
    ll.destroy()
    saveLocation.destroy()
    ipEntry.destroy()
    getIpButton.destroy()
    try:
        OpenHtml.destroy()
    except:
        pass
    MainMenu()

#-------------------------------- Location By Number ------------------------------------#

def locationByNumber(*args):
    global l0, ll0, lx0, l20, NumberEntry, getNumberButton, saveLocat1on
    LocationByIP.destroy()
    LocationByNumber.destroy()
    # GenrateQrCode.destroy()
    Menulabel.destroy()
    # exiT.destroy()
    Developer.destroy()
    l0 = tkinter.Label(top, text='Target Number', width=50, font='Arial 18 bold', bg='black', fg='red')
    l0.pack(pady=5)
    NumberEntry = tkinter.Entry(top, width=20, font='Arial 14 bold', bg='gray', fg='black')
    NumberEntry.pack()
    NumberEntry.focus_set()
    NumberEntry.bind('<Return>', getInfoByNumber)
    NumberEntry.bind('<Escape>', BackFromNumber)
    getNumberButton = tkinter.Button(top, text='GET INFO', font='Arial 12 bold', activeforeground='gray', bg='red',
                                     width=15, command=getInfoByNumber)
    getNumberButton.pack(pady=10)
    ll0 = tkinter.Button(top, text='Back', width=10, font='Arial 10 bold', bg='black', fg='red',
                         activeforeground='gray', command=BackFromNumber)
    ll0.pack()
    lx0 = tkinter.Label(top, text='Country, Carrier & Map Coordination', width=50, font='Arial 12 bold', bg='black', fg='red')
    l20 = tkinter.Label(top, text='', width=50, font='Arial 14 bold', bg='black', fg='red')
    saveLocat1on = tkinter.Button(top, text='Save location html', font='Arial 11 bold', activeforeground='gray',
                                  bg='blue', width=20, command=savehtml)


def getInfoByNumber(*args):
    global lat, lng, map
    try:
        phoneNumber = NumberEntry.get()
        if phoneNumber == '' or phoneNumber.startswith(" ") or phoneNumber.endswith(" ") or phoneNumber.isalpha():
            messagebox.showwarning('error', "Incorrect Mobile Number!")
        else:
            number = phonenumbers.parse(phoneNumber)
            location = geo.description_for_number(number, 'en')
            service_pro = phonenumbers.parse(phoneNumber)
            service_provider = carrier.name_for_number(service_pro, "en")
            opencageAPIkey = 'beb4fd7247424a6cb6d1105b9bc46781'
            geocoder = OpenCageGeocode(opencageAPIkey)
            query = str(location)
            result = geocoder.geocode(query)
            lat = result[0]['geometry']['lat']
            lng = result[0]['geometry']['lng']
            map = folium.Map(location=[lat, lng], zoom_start=10)
            folium.Marker([lat, lng], popup=location).add_to(map)
            if service_provider == '' or service_provider == ' ':
                messagebox.showwarning("Error", 'Wrong Mobile Number!')
            else:
                lx0.pack()
                l20.pack()
                saveLocat1on.pack(pady=5)
                l20['text'] = "\n"+service_provider+", "+location+"\n\n"+str(lat)+" "+str(lng)
    except:
        messagebox.showerror('error', "Can't Get Number Carrier!")

def savehtml(*args):
    global OpenHtml, path
    try:
        OpenHtml.destroy()
    except:
        pass
    try:
        path = filedialog.askdirectory(title="Save Location")
        if path == '' or path == ' ':
            messagebox.showwarning("Alert!", "You Not Select Any Directory!")
        else:
            if os.path.exists(f"{path}\{lat}_{lng}_map.html"):
                messagebox.showwarning("Alert!","File Already Exists!")
            else:
                map.save(f"{path}\{lat}_{lng}_map.html")
                messagebox.showinfo("Saved..!", "HTML File has been Saved!")
                sw = messagebox.askyesno("ASK!","Do You Want to Open The Location?")
                if sw == True:
                    webbrowser.open_new_tab(f"{path}\{lat}_{lng}_map.html")
                else:
                    pass
            OpenHtml = Button(top, text='Open HTML', width=15, font='Arial 10 bold', bg='black', fg='blue',
                              activeforeground='gray', command=openHtml)
            OpenHtml.pack(pady=5)
    except:
        messagebox.showerror('Save Error!!', "Can't save file, try again later.")

def openHtml(*args):
    webbrowser.open_new_tab(f"{path}\{lat}_{lng}_map.html")

def BackFromNumber(*args):
    global l0, ll0, lx0, l20, NumberEntry, getNumberButton
    l0.destroy()
    lx0.destroy()
    l20.destroy()
    ll0.destroy()
    getNumberButton.destroy()
    NumberEntry.destroy()
    try:
        OpenHtml.destroy()
    except:
        pass
    saveLocat1on.destroy()
    MainMenu()

#------------------------------------- QR Code ----------------------------------------#

def genrateQrCodeUi(*args):
    global qrCodeTargetLabel, qrCodeTargetEntry, qrCodeTargetNameLabel, qrCodeTargetNameEntry, doneLabel, geenrateButton, backButton, openQrButton
    Menulabel.destroy()
    LocationByIP.destroy()
    LocationByNumber.destroy()
    GenrateQrCode.destroy()
    exiT.destroy()
    Developer.destroy()
    qrCodeTargetLabel = Label(top, text='Target', width=50, font='Arial 18 bold', bg='black', fg='red')
    qrCodeTargetLabel.pack()
    qrCodeTargetEntry = Entry(top, width=20, font='Arial 14 bold', bg='gray', fg='black')
    qrCodeTargetEntry.pack()
    qrCodeTargetNameLabel = Label(top, text='Name of Target', width=50, font='Arial 18 bold', bg='black', fg='red')
    qrCodeTargetNameLabel.pack()
    qrCodeTargetNameEntry = Entry(top, width=20, font='Arial 14 bold', bg='gray', fg='black')
    qrCodeTargetNameEntry.pack()
    qrCodeTargetNameEntry.focus_set()
    qrCodeTargetNameEntry.bind('<Return>', genrateQr)
    qrCodeTargetNameEntry.bind('<Escape>', BackFromQR)
    qrCodeTargetNameEntry.bind('<Return>', genrateQr)
    qrCodeTargetNameEntry.bind('<Escape>', BackFromQR)
    geenrateButton = tkinter.Button(top, text='GENRATE', font='Arial 12 bold', activeforeground='gray', bg='red',
                                    width=15, command=genrateQr)
    geenrateButton.pack(pady=10)
    backButton = tkinter.Button(top, text='Back', width=10, font='Arial 10 bold', bg='black', fg='red',
                                activeforeground='gray', command=BackFromQR)
    backButton.pack()
    doneLabel = Label(top, text='', width=50, font='Arial 12 bold', bg='black', fg='red')
    openQrButton = Button(top, text='Open Qr', width=10, font='Arial 10 bold', bg='black', fg='red',
                          activeforeground='gray', command=openQr)


def genrateQr(*args):
    global filePath
    link = qrCodeTargetEntry.get()
    nameOfCode = qrCodeTargetNameEntry.get()
    if link != '' and nameOfCode != '':
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=2, )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image()
        img.save(f'{nameOfCode}.png')
        filePath = os.getcwd() + '\\' + nameOfCode + '.png'
        doneLabel.pack()
        doneLabel['text'] = f'\nDone Generated!\n'
        openQrButton.pack()
    else:
        messagebox.showerror('Error', 'You Must Insert Target And Name!')


def openQr(*args):
    if os.path.exists(filePath):
        im = Image.open(filePath)
        im.show()
    else:
        messagebox.showwarning('Warning', 'No File Path!')


def BackFromQR(*args):
    qrCodeTargetLabel.destroy()
    qrCodeTargetEntry.destroy()
    qrCodeTargetNameLabel.destroy()
    qrCodeTargetNameEntry.destroy()
    doneLabel.destroy()
    backButton.destroy()
    geenrateButton.destroy()
    openQrButton.destroy()
    MainMenu()

#------------------------------------------- MainMenu ------------------------------------------------#

def MainMenu(*args):
    global LocationByIP, LocationByNumber, GenrateQrCode, Menulabel, exiT, Developer
    top.geometry('300x370+600+150')
    Menulabel = Label(top, text='Get Map', width=50, font='Arial 18 bold', bg='black', fg='red')
    Menulabel.pack(pady=10)
    LocationByIP = Button(top, text='Get Location by IP', font='Arial 12 bold', activeforeground='gray', bg='red',
                          width=25,
                          command=locationByIp)
    LocationByIP.pack(pady=15)

    LocationByNumber = Button(top, text='Get Info & Location by Number', font='Arial 12 bold', activeforeground='gray',
                              bg='red', width=25,
                              command=locationByNumber)
    LocationByNumber.pack()

    Developer = Button(top, text='Dev by: Youssef Alkhodary', font='Arial 8 bold', fg='white', bg='black', width=25,
                           command=developer, height=1, borderwidth=0)
    Developer.pack(pady=15)

def developer(*args):
    webbrowser.open_new_tab("https://userjoo9.github.io/youssefinfo/#main")


#-----------------------------------------__Password Minu__----------------------------------------#


def passwordMinu():
    global passwordEntry, passwordLabel, loginButton, Developer
    top.geometry('300x200+600+150')
    passwordLabel = tkinter.Label(top, text='@%* PASSWORD $&#', width=50, font='Arial 15 bold', bg='black', fg='red')
    passwordLabel.pack(pady=15)
    passwordEntry = tkinter.Entry(top, width=20, font='Arial 14 bold', bg='gray', fg='black', show="*")
    passwordEntry.pack()
    passwordEntry.focus_set()
    passwordEntry.bind('<Return>', checkPassword)
    loginButton = tkinter.Button(top, text='LOGIN', font='Arial 10 bold', activeforeground='gray', bg='red',
                                     width=26, command=checkPassword)
    loginButton.pack(pady=15)

    Developer = Button(top, text='Dev by: Youssef Alkhodary', font='Arial 8 bold', fg='white', bg='black', width=25,
                       command=developer, height=1, borderwidth=0)
    Developer.pack(pady=10)

def checkPassword(*args):
    global switch
    pwd = passwordEntry.get()
    try:
        switch = requests.get("https://pastebin.com/raw/WxHWL0m7").text
        if pwd == switch:
            passwordLabel.destroy()
            passwordEntry.destroy()
            loginButton.destroy()
            Developer.destroy()
            MainMenu()
            messagebox.showinfo("Notify!", "Welcome !!\nاهلا بيك في برنامج جيت ماب, لا تستخدم البرنامج في ما لا يرضي الله")
        else:
            messagebox.showerror("Password error", "Password is wrong!!\nالباسورد غلط متحاولش فيه كتير")
            yesNo = messagebox.askokcancel("Update", "Do you want check updates...\nافتح الموقع شوف التحديثات الجديده")
            if yesNo:
                developer()
            else:
                pass
    except:
        messagebox.showerror("Connection error", "Check internet connection and try again")


#-------------------------------------------- __home__ ----------------------------------------------#

top = Tk()
top.title('Get-Map')
top.resizable(False, False)
top.iconbitmap("images/favicon.ico")
top.configure(background='black')

passwordMinu()

top.mainloop()
