import os
print("""
1.Nmap
2.Bettercap
      """)

Ip = input("Ip yi Giriniz: ")
secim = input("bir seçim giriniz: ")

if secim == "1":
    os.system("nmap -sV " + Ip)

elif secim == "2":
    os.system("sudo bettercap")
    

else:
    print("lütfen doğru bir seçim yapınız ")
    
