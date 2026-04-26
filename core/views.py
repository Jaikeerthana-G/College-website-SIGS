from django.shortcuts import render, redirect
from django.db.models import Case, When, Value, IntegerField
from .models import AdmissionApplication, ContactMessage, Course, FacultyMember, Announcement, HeroSection, GalleryMedia

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            # We can add a success message here using django messages framework
    
    courses = Course.objects.all()
    announcements = Announcement.objects.filter(is_active=True)
    hero_section = HeroSection.objects.filter(is_active=True).first()
    gallery_media = GalleryMedia.objects.filter(is_active=True)
    
    context = {
        'courses': courses,
        'announcements': announcements,
        'hero_section': hero_section,
        'gallery_media': gallery_media,
    }
    return render(request, 'core/index.html', context)

def faculty(request):
    faculty_members = FacultyMember.objects.annotate(
        department_order=Case(
            When(department='Principal', then=1),
            When(department='Computer Science', then=2),
            When(department='Commerce', then=3),
            When(department='Languages', then=4),
            default=5,
            output_field=IntegerField(),
        )
    ).order_by('department_order', 'order', 'name')
    
    context = {
        'faculty_members': faculty_members,
    }
    return render(request, 'core/faculty.html', context)

def admission(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        aadhar = request.POST.get('aadhar')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        board = request.POST.get('board')
        percentage = request.POST.get('percentage')
        passing_year = request.POST.get('passing_year')
        course = request.POST.get('course')
        
        # Files
        marksheet_12th = request.FILES.get('marksheet_12th')
        id_proof = request.FILES.get('id_proof')
        passport_photo = request.FILES.get('passport_photo')

        AdmissionApplication.objects.create(
            fullname=fullname, dob=dob, gender=gender, phone=phone, email=email, aadhar=aadhar,
            address=address, city=city, state=state, pincode=pincode, board=board,
            percentage=percentage, passing_year=passing_year, course=course,
            marksheet_12th=marksheet_12th, id_proof=id_proof, passport_photo=passport_photo
        )
        # Redirect to a success page or back with success message
        return redirect('index')

    return render(request, 'core/admission.html')
