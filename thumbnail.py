import os
import numpy as np
import cv2
import random

def load_image_from_file(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    return img

def load_images_from_folders(folders):
    images = {}
    for key, folder in folders.items():
        if not os.path.exists(folder):
            print(f"{folder} bulunamadı, atlanıyor.")
            continue
        images[key] = []
        for filename in os.listdir(folder):
            if filename.endswith(".png"):  # Sadece .png dosyalarını al
                img_path = os.path.join(folder, filename)
                img = load_image_from_file(img_path)
                if img is not None:
                    images[key].append(img)
        print(f"{key} klasöründen {len(images[key])} resim yüklendi.")
    return images

def place_image_on_canvas(canvas, image, x, y):
    h, w = image.shape[:2]

    # Eğer resim 4 kanallıysa (RGBA), transparan arka planla birlikte yerleştir
    if image.shape[2] == 4:
        alpha_channel = image[:, :, 3] / 255.0
        for c in range(0, 3):
            canvas[y:y+h, x:x+w, c] = alpha_channel * image[:, :, c] + (1 - alpha_channel) * canvas[y:y+h, x:x+w, c]
    else:
        canvas[y:y+h, x:x+w] = image

    return canvas

def resize_image_proportionally(image, target_height=None, target_width=None):
    h, w = image.shape[:2]
    if target_height and target_width:
        scaling_factor = min(target_height / h, target_width / w)
    elif target_height:
        scaling_factor = target_height / h
    else:
        scaling_factor = target_width / w
    
    new_size = (int(w * scaling_factor), int(h * scaling_factor))
    return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)

def create_dress_combination(urunler):
    canvas_size = (2000, 1500, 3)
    canvas = np.full(canvas_size, 255, dtype=np.uint8)  # Beyaz arka plan

    dress = random.choice(urunler['dress'])
    shoes = random.choice(urunler['shoes'])
    bag = random.choice(urunler['bags'])
    glasses = random.choice(urunler['glasses'])
    accessuar = random.choice(urunler['accessuar'])

    dress_resized = resize_image_proportionally(dress, target_height=1400)
    shoes_resized = resize_image_proportionally(shoes, target_height=450)
    bag_resized = resize_image_proportionally(bag, target_height=470)
    glasses_resized = resize_image_proportionally(glasses, target_height=450)
    accessuar_resized = resize_image_proportionally(accessuar, target_height=450)

    # Ortalamak için x, y pozisyonları
    canvas = place_image_on_canvas(canvas, dress_resized, (canvas_size[1] - dress_resized.shape[1]) // 2, 300)
    canvas = place_image_on_canvas(canvas, shoes_resized, (canvas_size[1] - shoes_resized.shape[1]) // 2, 1450)
    
    
    # Tuval sınırlarını kontrol ederek yerleştirme
    bag_x = (canvas_size[1] - bag_resized.shape[1]) // 2 + 300
    if bag_x + bag_resized.shape[1] > canvas_size[1]:
        bag_x = canvas_size[1] - bag_resized.shape[1] - 20
    canvas = place_image_on_canvas(canvas, bag_resized, bag_x, 800)
    
    glasses_x = 200
    if glasses_x + glasses_resized.shape[1] > canvas_size[1]:
        glasses_x = canvas_size[1] - glasses_resized.shape[1] - 20
    canvas = place_image_on_canvas(canvas, glasses_resized, glasses_x, 350)

    accessuar_x = canvas_size[1] - accessuar_resized.shape[1] - 200
    if accessuar_x < 0:
        accessuar_x = 0
    canvas = place_image_on_canvas(canvas, accessuar_resized, accessuar_x, 250)

    return canvas

def create_tops_bottom_combination(urunler):
    canvas_size = (2000, 1500, 3)
    canvas = np.full(canvas_size, 255, dtype=np.uint8)  # Beyaz arka plan

    tops = random.choice(urunler['tops'])
    bottoms = random.choice(urunler['bottoms'])
    shoes = random.choice(urunler['shoes'])
    glasses = random.choice(urunler['glasses'])
    accessuar = random.choice(urunler['accessuar'])
    bag = random.choice(urunler['bags'])

    tops_resized = resize_image_proportionally(tops, target_height=750)
    bottoms_resized = resize_image_proportionally(bottoms, target_height=800)  # Aynı yapı için top ve bottom'ı tek bir resim olarak düşün
    shoes_resized = resize_image_proportionally(shoes, target_height=400)
    glasses_resized = resize_image_proportionally(glasses, target_height=450)
    accessuar_resized = resize_image_proportionally(accessuar, target_height=450)
    bag_resized = resize_image_proportionally(bag, target_height=470)

    # Ortalamak için x, y pozisyonları
    canvas = place_image_on_canvas(canvas, tops_resized, (canvas_size[1] - tops_resized.shape[1]) // 2, 330)
    canvas = place_image_on_canvas(canvas, bottoms_resized, (canvas_size[1] - bottoms_resized.shape[1]) // 2, 870)
    canvas = place_image_on_canvas(canvas, shoes_resized, (canvas_size[1] - shoes_resized.shape[1]) // 2, 1450)

    
    
    # Tuval sınırlarını kontrol ederek yerleştirme
    bag_x = (canvas_size[1] - bag_resized.shape[1]) // 2 + 300
    if bag_x + bag_resized.shape[1] > canvas_size[1]:
        bag_x = canvas_size[1] - bag_resized.shape[1] - 20
    canvas = place_image_on_canvas(canvas, bag_resized, bag_x, 800)
    
    glasses_x = 200
    if glasses_x + glasses_resized.shape[1] > canvas_size[1]:
        glasses_x = canvas_size[1] - glasses_resized.shape[1] - 20
    canvas = place_image_on_canvas(canvas, glasses_resized, glasses_x, 350)

    accessuar_x = canvas_size[1] - accessuar_resized.shape[1] - 200
    if accessuar_x < 0:
        accessuar_x = 0
    canvas = place_image_on_canvas(canvas, accessuar_resized, accessuar_x, 250)

    return canvas

def main():
    base_folder = r'C:\\Users\\Monster\\Desktop\\ibexStaj\\transp.image'

    folders = {
        'dress': os.path.join(base_folder, 'dress'),
        'shoes': os.path.join(base_folder, 'shoes'),
        'bottoms': os.path.join(base_folder, 'bottoms'),
        'jacket': os.path.join(base_folder, 'jacket'),
        'glasses': os.path.join(base_folder, 'glasses'),
        'bags': os.path.join(base_folder, 'bags'),
        'tops': os.path.join(base_folder, 'tops'),
        'accessuar': os.path.join(base_folder, 'accessuar')
    }

    images = load_images_from_folders(folders)

    if 'dress' in images and len(images['dress']) > 0:
        final_image_dress = create_dress_combination(images)
        cv2.imwrite('combined_image_final_dress.png', final_image_dress)

    if 'tops' in images and len(images['tops']) > 0 and 'bottoms' in images and len(images['bottoms']) > 0:
        final_image_tops_bottom = create_tops_bottom_combination(images)
        cv2.imwrite('combined_image_final_topbottom.png', final_image_tops_bottom)

if __name__ == "__main__":
    main()
