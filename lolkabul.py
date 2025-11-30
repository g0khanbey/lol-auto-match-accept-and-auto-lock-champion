import cv2
import numpy as np
from mss import mss
import mouse
import keyboard
import tkinter as tk
import time
import os

calisiyor_accept = False
calisiyor_pick = False
sct = mss()

accept_img = cv2.imread("src/accept.png", cv2.IMREAD_COLOR)
hazir_img = cv2.imread("src/hazir.png", cv2.IMREAD_COLOR)
ara_img = cv2.imread("src/ara.png", cv2.IMREAD_COLOR)

def load_champions():
    champs = {}
    path = os.path.join("src", "champion_icons", "champions.txt")
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "=" in line:
                    ad, resim = line.split("=", 1)
                    champs[ad.strip().lower()] = resim.strip()
    except Exception as e:
        print("[ERROR] champions.txt okunamadı:", e)
    print("[INFO] champions.txt yüklendi:", champs)
    return champs

champions = load_champions()

current_champion_img = None
current_champion_name = ""

def ara_yap():
    print("[ARA] ara.png aranıyor...")
    screenshot = np.array(sct.grab(sct.monitors[1]))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
    result = cv2.matchTemplate(screenshot, ara_img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.75)
    bulundu = False
    for pt in zip(*loc[::-1]):
        x = pt[0] + ara_img.shape[1] // 2
        y = pt[1] + ara_img.shape[0] // 2
        print(f"[ARA] ara.png bulundu → tıklanıyor {x}, {y}")
        mouse.move(x, y)
        mouse.click()
        bulundu = True
        break
    if not bulundu:
        print("[ARA] ara.png bulunamadı!")
        return False
    time.sleep(0.25)
    isim = sampiyon_entry.get().strip()
    print(f"[ARA] '{isim}' yazılıyor...")
    keyboard.write(isim)
    time.sleep(0.1)
    keyboard.press("enter")
    keyboard.release("enter")
    print(f"[ARA] Arama tamamlandı: '{isim}'")
    return True

def match_scaled(haystack, needle):
    resized = cv2.resize(needle, (71, 67))
    result = cv2.matchTemplate(haystack, resized, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.74)
    for pt in zip(*loc[::-1]):
        x = pt[0] + 71 // 2
        y = pt[1] + 67 // 2
        return x, y
    return None

def sampiyon_kitleme():
    if not calisiyor_pick or current_champion_img is None:
        return
    screenshot = np.array(sct.grab(sct.monitors[1]))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
    print(f"[PICK] {current_champion_name} aranıyor...")
    coord = match_scaled(screenshot, current_champion_img)
    if coord:
        x, y = coord
        print(f"[PICK] Bulundu → tıklanıyor {x},{y}")
        mouse.move(x, y)
        mouse.click()
        time.sleep(0.4)
        hazir_coord = match_icon(screenshot, hazir_img)
        if hazir_coord:
            hx, hy = hazir_coord
            print(f"[LOCK-IN] hazir.png tıklanıyor {hx},{hy}")
            mouse.move(hx, hy)
            mouse.click()
    if calisiyor_pick:
        root.after(1500, sampiyon_kitleme)

def match_icon(screenshot, icon):
    result = cv2.matchTemplate(screenshot, icon, cv2.TM_CCOEFF_NORMED)
    loc = np.where(result >= 0.75)
    for pt in zip(*loc[::-1]):
        x = pt[0] + icon.shape[1] // 2
        y = pt[1] + icon.shape[0] // 2
        return x, y
    return None

def ara_ve_kitle():
    global calisiyor_pick, current_champion_img, current_champion_name
    basari = ara_yap()
    if not basari:
        durum_label.config(text="Arama bulunamadı!")
        return
    isim = sampiyon_entry.get().strip().lower()
    if isim not in champions:
        durum_label.config(text="Şampiyon listede yok!")
        return
    yol = os.path.join("src", "champion_icons", champions[isim])
    current_champion_img = cv2.imread(yol, cv2.IMREAD_COLOR)
    current_champion_name = isim.capitalize()
    calisiyor_pick = True
    durum_label.config(text=f"Durum: {current_champion_name} aranıyor")
    print(f"[INFO] Şampiyon kitleme başladı: {current_champion_name}")
    sampiyon_kitleme()

def durdur_ara_kitle():
    global calisiyor_pick
    calisiyor_pick = False
    durum_label.config(text="Durum: Şampiyon kitleme durdu")
    print("[INFO] Ara + Kitle işlemi durduruldu!")

def mac_kabul_kontrol():
    if not calisiyor_accept:
        return
    screenshot = np.array(sct.grab(sct.monitors[1]))
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
    coord = match_icon(screenshot, accept_img)
    if coord:
        x, y = coord
        print(f"[ACCEPT] Bulundu → tıklanıyor {x},{y}")
        mouse.move(x, y)
        mouse.click()
    root.after(2000, mac_kabul_kontrol)

root = tk.Tk()
root.title("LoL Otomatik Sistem")
root.geometry("650x500")

tk.Button(root, text="Başlat Maç Kabul", font=("Arial", 12),
          command=lambda: [globals().update({'calisiyor_accept': True}), mac_kabul_kontrol()]).pack(pady=3)

tk.Button(root, text="Durdur Maç Kabul", font=("Arial", 12),
          command=lambda: globals().update({'calisiyor_accept': False})).pack(pady=3)

tk.Label(root, text="Şampiyon İsmi:", font=("Arial", 12)).pack(pady=5)
sampiyon_entry = tk.Entry(root, font=("Arial", 12))
sampiyon_entry.pack(pady=5)

tk.Button(root, text="Ara + Şampiyon Kitle", font=("Arial", 13), command=ara_ve_kitle).pack(pady=6)
tk.Button(root, text="Ara + Şampiyon Kitle Durdur", font=("Arial", 13), command=durdur_ara_kitle).pack(pady=6)

durum_label = tk.Label(root, text="Durum: Bekleniyor", font=("Arial", 11), fg="blue")
durum_label.pack(pady=10)

uyari = tk.Label(
    root,
    text=(
        "UYARI:\n"
        "Bu yazılım Riot Games tarafından desteklenmez.\n"
        "Otomasyon tespiti durumunda ceza alma ihtimali vardır.\n"
        "Kullanım tamamen sizin sorumluluğunuzdadır.\n"
        "Sistem 1280x720 çözünürlük için optimize edilmiştir.\n"
        "Şampiyon seçmiyorsa champion_icons/champions.txt kontrol edin."
    ),
    font=("Arial", 10),
    fg="red",
    justify="center"
)
uyari.pack(pady=10)

root.mainloop()
