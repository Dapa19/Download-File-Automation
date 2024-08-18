import os
import shutil

# Definisikan path untuk folder unduhan dan folder tujuan
download_folder = r"C:\Users\USER\Downloads"
image_folder = "D:/Saved Image"
video_folder = "D:/Saved Video"
music_folder = "D:/Saved Music"

# Buat folder tujuan jika belum ada
#os.makedirs(image_folder, exist_ok=True)
#os.makedirs(video_folder, exist_ok=True)
#os.makedirs(music_folder, exist_ok=True)

# Ekstensi file yang ingin dipindahkan
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
video_extensions = ['.mp4', '.avi', '.mov', '.wmv', '.mkv']
music_extensions = ['.mp3', '.wav', '.aac', '.flac', '.ogg']

# Fungsi untuk memindahkan file
def move_files(folder, extensions, destination):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        if os.path.isfile(file_path) and any(file_name.lower().endswith(ext) for ext in extensions):
            shutil.move(file_path, os.path.join(destination, file_name))
            print(f"Memindahkan {file_name} ke {destination}")

# Loop utama
while True:
    print("==========Pilih Menu==========")
    print("1. Pindahkan Gambar \n2. Pindahkan Video \n3. Pindahkan Music \n4. Pindahkan Semuanya \n\n0. Keluar")
    pilihan = int(input("Pilih Menu (1-4) : "))

    if pilihan == 1:
        move_files(download_folder, image_extensions, image_folder)
        print("Pindah file selesai.")
    elif pilihan == 2:
        move_files(download_folder, video_extensions, video_folder)
        print("Pindah file selesai.")
    elif pilihan == 3:
        move_files(download_folder, music_extensions, music_folder)
        print("Pindah file selesai.")
    elif pilihan == 4:
        move_files(download_folder, image_extensions, image_folder)
        move_files(download_folder, video_extensions, video_folder)
        move_files(download_folder, music_extensions, music_folder)
        print("Pindah file selesai.")
    elif pilihan == 0:
        print("Berhasil Keluar")
        break
    else:
        print("Pilihan Tidak Valid, Silahkan Pilih Ulang")

    input("Tekan Enter untuk melanjutkan...")