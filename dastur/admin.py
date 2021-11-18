from django.contrib import admin
from .models import *
# Register your models here.


# admin.site.register(Standard)
# admin.site.register(Subject)
# admin.site.register(Lesson)
# admin.site.register(Comment)
# admin.site.register(Reply)
# admin.site.register(WorkingDays)
# admin.site.register(TimeSlots)
# admin.site.register(SlotSubject)

@admin.register(Standard)
class StandartAdmin(admin.ModelAdmin):
    list_display = ['name','slug','description']
    list_filter = ['name','description']
    search_fields = ['name','description']
    prepopulated_fields = {'slug':('name',)}



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['lesson_name','comment_name','author','body','date_added']
    list_filter = ['lesson_name','comment_name','author','body','date_added']    
    search_fields = ['lesson_name','comment_name','author','body','date_added']



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject_id','slug','name','standards','description','image']
    list_filter = ['subject_id','slug','name','standards','description']
    search_fields = ['subject_id','slug','name','standards','description']
    prepopulated_fields = {'slug':('name','subject_id')}


@admin.register(Lesson)
class LesoonAdmin(admin.ModelAdmin):
    list_display = ['lesson_id','slug','name','standard','created_by','created_at','subject','position','video','ppt','Notes']
    list_filter = ['lesson_id','slug','name','standard','created_by','created_at','subject','position','ppt','Notes']
    search_fields = ['lesson_id','slug','name','standard','created_by','created_at','subject','position','ppt','Notes']
    prepopulated_fields = {'slug':('name','lesson_id','position')}



@admin.register(WorkingDays)
class WorkingDaysAdmin(admin.ModelAdmin):
    list_display = ['day','standard']
    list_filter = ['day','standard']
    search_fields = ['day']


@admin.register(TimeSlots)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['start_time','end_time','standard']
    list_filter = ['start_time','end_time','standard']
    search_fields = ['start_time','end_time','standard']



@admin.register(SlotSubject)
class SlotSubjectAdmin(admin.ModelAdmin):
    list_display = ['day','slot','slot_subject','standard']
    list_filter = ['day','slot','slot_subject','standard']
    search_fields = ['day','slot','slot_subject','standard']



@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['comment_name','reply_body','author','date_added']
    list_filter = ['comment_name','reply_body','author','date_added']
    search_fields = ['comment_name','reply_body','author','date_added']
