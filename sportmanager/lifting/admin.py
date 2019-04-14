from django.contrib import admin
from django import forms
from lifting.models import BaseExercise, Set, Exercise, Workout

# Register your models here.
# class SetForm(forms.ModelForm):
    # """ something newer
    # """
    # class Meta:
        # model = DocumentMetaDataValue
        # fields = '__all__'

# class DocumentMetaDataValueInline(admin.TabularInline):
    # model = DocumentMetaDataValue
    # form = Fred

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = '__all__'

    sets = forms.ModelMultipleChoiceField(queryset=Set.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['sets'].initial = self.instance.set_set.all()

    def save(self, *args, **kwargs):
        # FIXME: 'commit' argument is not handled
        # TODO: Wrap reassignments into transaction
        # NOTE: Previously assigned Workouts are silently reset
        instance = super(WorkoutForm, self).save(commit=False)
        self.fields['sets'].initial.update(workout=None)
        self.cleaned_data['sets'].update(workout=instance)
        return instance

class WorkoutAdmin(admin.ModelAdmin):
    form = WorkoutForm
class BaseExerciseAdmin(admin.ModelAdmin):
    """"""
    pass
class ExerciseAdmin(admin.ModelAdmin):
    """"""
    pass
class WorkoutAdmin(admin.ModelAdmin):
    """"""
    pass
class SetAdmin(admin.ModelAdmin):
    """"""
    pass


admin.site.register(Set, SetAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(BaseExercise, BaseExerciseAdmin)
admin.site.register(Workout, WorkoutAdmin)
