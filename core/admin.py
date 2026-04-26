from django.contrib import admin
from .models import AdmissionApplication, ContactMessage, Course, FacultyMember, Announcement, HeroSection, GalleryMedia

@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'course', 'email', 'phone', 'submitted_at')
    search_fields = ('fullname', 'email', 'aadhar')
    list_filter = ('course', 'gender', 'submitted_at')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'order')
    search_fields = ('title', 'description')
    list_editable = ('order',)

@admin.register(FacultyMember)
class FacultyMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'designation', 'order')
    list_filter = ('department',)
    search_fields = ('name', 'designation', 'specialization')
    list_editable = ('order',)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'is_active')
    list_filter = ('is_active', 'date_posted')
    search_fields = ('title', 'content')

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')

@admin.register(GalleryMedia)
class GalleryMediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'order', 'is_active')
    list_filter = ('media_type', 'is_active')
    list_editable = ('order', 'is_active')
