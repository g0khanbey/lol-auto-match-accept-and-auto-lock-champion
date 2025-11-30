from PIL import Image
import os

TARGET_W = 71
TARGET_H = 67

def resize_image(path):
    img = Image.open(path).convert("RGBA")

    # 71x67 olarak yeniden boyutlandır
    resized = img.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)

    # Aynı dosya adına kaydet
    resized.save(path)

def process_all():
    files = [f for f in os.listdir('.') if f.lower().endswith('.png')]
    print(f"{len(files)} PNG bulundu.")

    for f in files:
        print("İşleniyor:", f)
        resize_image(f)

    print("\n✔️ Bitti! Tüm PNG’ler 71×67 oldu.")

if __name__ == "__main__":
    process_all()
