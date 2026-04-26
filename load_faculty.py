import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'college_backend.settings')
django.setup()

from core.models import FacultyMember

FacultyMember.objects.all().delete()

data = [
    ("Dr. Kamala H R", "Principal", "MA with 30+ years of experience in academics and research leadership.", "Principal", 1),
    ("Dr. Chandrika G", "Head of Department", "Artificial Intelligence", "Computer Science", 1),
    ("Miss. Tejaswini N", "Assistant Professor", "Data Science", "Computer Science", 2),
    ("Mr. Shreenivas", "Assistant Professor", "Web Development", "Computer Science", 3),
    ("Mr. Naveen Kumar", "Assistant Professor", "Cloud Computing", "Computer Science", 4),
    ("Mrs. Vyshnavi H", "Head of Department", "Financial Management", "Commerce", 1),
    ("Miss. Mamatha N", "Assistant Professor", "Accounting & Taxation", "Commerce", 2),
    ("Mr. Guru Prasad", "Assistant Professor", "Accounting & Taxation", "Commerce", 3),
    ("Unknown", "Assistant Professor", "Accounting & Taxation", "Commerce", 4),
    ("Mrs. Nadiya Nikhath Nayaz", "Asst. Professor", "English", "Languages", 1),
    ("Mr. Hari Krishna", "Assistant Professor", "Kannada", "Languages", 2),
]

for name, desig, spec, dept, order in data:
    FacultyMember.objects.create(name=name, designation=desig, specialization=spec, department=dept, order=order)

print("Faculty loaded successfully!")
