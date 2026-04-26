import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_backend.settings')
django.setup()

from core.models import GalleryMedia
from django.core.files import File

# Create media directory if it doesn't exist
media_gallery_dir = os.path.join('media', 'gallery')
os.makedirs(media_gallery_dir, exist_ok=True)

# Path to the sample static image
static_img_path = r'c:\Users\Admin\Desktop\college-website - Copy\college-website\assets\images\sample.jpg'

if os.path.exists(static_img_path):
    for i, title in enumerate(["Campus View", "Library", "Computer Lab", "Auditorium", "Event", "Students"]):
        with open(static_img_path, 'rb') as f:
            django_file = File(f, name=f'sample_{i}.jpg')
            GalleryMedia.objects.create(title=title, media_type='image', file=django_file, order=i)
    print("Gallery populated successfully with sample images!")
else:
    print(f"Sample image not found at {static_img_path}")
