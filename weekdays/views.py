from django.shortcuts import render
from django.http import HttpResponse
weekdays_data = [
            {'uzbek': 'Dushanba', 'russian': 'Понедельник', 'english': 'Monday'},
            {'uzbek': 'Seshanba', 'russian': 'Вторник', 'english': 'Tuesday'},
            {'uzbek': 'Chorshanba', 'russian': 'Среда', 'english': 'Wednesday'},
            {'uzbek': 'Payshanba', 'russian': 'Четверг', 'english': 'Thursday'},
            {'uzbek': 'Juma', 'russian': 'Пятница', 'english': 'Friday'},
            {'uzbek': 'Shanba', 'russian': 'Суббота', 'english': 'Saturday'},
            {'uzbek': 'Yakshanba', 'russian': 'Воскресенье', 'english': 'Sunday'},]
def hafta(request):
        global weekdays_data
        return render(request, 'hafta.html', {'weekdays_data': weekdays_data})
def hafta_uz(request):
    global weekdays_data
    return render(request, 'hafta_uz.html', {'weekdays_data': weekdays_data})

def hafta_ru(request):
    global weekdays_data
    return render(request, 'hafta_ru.html', {'weekdays_data': weekdays_data})


def hafta_eng(request):
    global weekdays_data
    return render(request, 'hafta_eng.html', {'weekdays_data': weekdays_data})


