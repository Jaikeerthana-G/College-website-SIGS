from django.db import models

class AdmissionApplication(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    COURSE_CHOICES = [
        ('BCA', 'BCA'),
        ('BCA AI/ML', 'BCA AI/ML'),
        ('B.Com', 'B.Com'),
    ]

    # Personal Information
    fullname = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    aadhar = models.CharField(max_length=20)

    # Address Details
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    # Academic Information
    board = models.CharField(max_length=100)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    passing_year = models.IntegerField()
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)

    # Documents
    marksheet_12th = models.FileField(upload_to='admissions/marksheets/')
    id_proof = models.FileField(upload_to='admissions/id_proofs/')
    passport_photo = models.ImageField(upload_to='admissions/photos/')

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.course}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=100, blank=True, null=True)
    icon_class = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class FacultyMember(models.Model):
    DEPARTMENT_CHOICES = [
        ('Principal', 'Principal'),
        ('Computer Science', 'Computer Science'),
        ('Commerce', 'Commerce'),
        ('Languages', 'Languages'),
    ]

    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='Computer Science')
    image = models.ImageField(upload_to='faculty/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['department', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.department})"


class Announcement(models.Model):
    MEDIA_TYPES = [
        ('none', 'None'),
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    multimedia_file = models.FileField(upload_to='announcements/', blank=True, null=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='none')
    date_posted = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

class HeroSection(models.Model):
    title = models.CharField(max_length=200, default="Sarvodaya Institute of Graduate Studies")
    subtitle = models.CharField(max_length=200, default="Empowering Minds. Transforming Futures.")
    video = models.FileField(upload_to='hero/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return "Hero Section Settings"

class GalleryMedia(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('audio', 'Audio'),
    ]
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='image')
    file = models.FileField(upload_to='gallery/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Gallery Media"

    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()})"
