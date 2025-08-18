import random

Welcome_message = "WELCOME TO ZHYRO GAMES!!"
tikus_position = random.randint (1, 5)

print("******************************")
print(f"|  {Welcome_message}  |")
print("******************************")

nama_user = input("Masukan nama kamu:")

print(f'''
HALLO {nama_user}!  coba perhatikan lubang dibawah ini
|_|   |_|   |_|   |_|   |_|
''')

pilihan_user = int(input("Menurut kamu di lubang berapa tikus kantor berada?  [1/2/3/4/5]: "))

def konfirmasi(pilihan_user):
    konfirm = input(f"Apakah anda yakin memilih {pilihan}? (ya/tidak): ")
    if konfirm.lower() == "ya":
        print(f"Pilihan {pilihan} berhasil dikonfirmasi!\n")
    else:
        print("Pilihan dibatalkan.\n")
        
pilihan = input("Pilih nomor: ")
konfirmasi = input(f"Apakah anda yakin memilih {pilihan}? (ya/tidak): ")
if konfirmasi.lower() == "ya":
    print(f"Pilihan {pilihan} berhasil dikonfirmasi!")
else:
    print("Pilihan dibatalkan.")

if pilihan_user == tikus_position:
	print(f"selamat {nama_user } kamu menang posisi tikus ada di lubang nomor {tikus_position} dan pilihan kamu adalah lubang nomor  {pilihan_user}.")
else:
		print(f"LOSERR! tikus bukan berada disitu tapi di lubang nomor {tikus_position} sedangkan kamu memilih lubang nomor {pilihan_user} ")