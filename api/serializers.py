from rest_framework import serializers
from dastur.models import *


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name','slug','description']
        model = Standard



class SubjectdSerializer(serializers.ModelSerializer):
    standards = StandardSerializer(read_only=True)
    class Meta:
        fields = ['subject_id','name','standards','slug','image','description','standards']
        model = Subject



class LessondSerializer(serializers.ModelSerializer):
    standard = StandardSerializer(read_only=True)
    created_by = User()
    subject = SubjectdSerializer(read_only=True)
    class Meta:
        fields = ['lesson_id','standard','created_by','created_at','subject','name','position','slug','video','ppt','Notes','standard','created_by']
        model = Lesson



class WorkingDaysSerializer(serializers.ModelSerializer):
    standard = StandardSerializer(read_only=True)
    class Meta:
        fields = ['standard','day','standard']
        model = WorkingDays



class TimeSlotsSerializer(serializers.ModelSerializer):
    standard = StandardSerializer(read_only=True)
    class Meta:
        fields = ['standard','start_time','end_time','standard']
        model = TimeSlots


class SlotSubjectSerializer(serializers.ModelSerializer):
    standard = StandardSerializer(read_only=True)
    day = WorkingDaysSerializer(read_only=True)
    slot = TimeSlotsSerializer(read_only=True)
    slot_subject = SubjectdSerializer(read_only=True)
    class Meta:
        fields = ['standard','day','slot','slot_subject','standard','day','slot','slot_subject']
        model = SlotSubject



class CommentSerializer(serializers.ModelSerializer):
    lesson_name = LessondSerializer(read_only=True)
    class Meta:
        fields = ['lesson_name','comment_name','author','body','date_added','lesson_name'] 
        model = Comment



class ReplySerializer(serializers.ModelSerializer):
    comment_name = CommentSerializer(read_only=True)
    class Meta:
        fields = ['comment_name','reply_body','author','date_added','comment_name'] 
        model = Reply