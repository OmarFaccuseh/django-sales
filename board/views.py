from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from .models import Profile, Instrumento, Metricas
from .forms import InstrumentoForm
from django.forms import modelformset_factory
import random


def dashboard(request):
    return render(request, "dashboard.html")


def config(request):
    return render(request, "config.html")


# genera un form editable para cada instrumento (formset)
@login_required
def tabla(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    metrica = Metricas.objects.filter(profile=profile).first()

    instrumentoFormSet = modelformset_factory(Instrumento, form=InstrumentoForm, extra=1)
    if request.method == 'POST':
        formset = instrumentoFormSet(request.POST, queryset=metrica.instrumentos.all())
        if formset.is_valid():
            new_instrumentos = formset.save(commit=False)
            for instrumento in new_instrumentos:
                if instrumento.pk:
                    instrumento.save()
                else:
                    instrumento.save()
                    metrica.instrumentos.add(instrumento)
            for instrumento in formset.deleted_objects:
                metrica.instrumentos.remove(instrumento)
            # metrica.instrumentos.set(new_instrumentos)
            return redirect('board:tabla')
        else:
            for form in formset:
                if form.errors:
                    print(form.errors)
            messages.error(request, "Hubo un error al guardar el instrumento")
            return redirect('board:tabla')

    else:
        formset = instrumentoFormSet(queryset=metrica.instrumentos.all())
    return render(request, "tabla.html", {'formset': formset, 'metrica': metrica})


@login_required
def graficas(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    metrica = Metricas.objects.filter(profile=profile).first()

    instrumentos = metrica.instrumentos.all()
    data_instrumentos = []

    for i in instrumentos:
        r, g, b = generate_random_color()  # Genera un color base
        border_color = f'rgba({r}, {g}, {b}, 1)'
        lighter_r, lighter_g, lighter_b = lighten_color(r, g, b)
        background_color = f'rgba({lighter_r}, {lighter_g}, {lighter_b}, 0.2)'

        data_instrumentos.append({
            'nombre': i.name,
            'porc_anual': i.porcentaje_anual,  # Suponiendo que tienes un campo 'rendimiento_anual'
            'congelamiento_dias': i.congelamiento_dias,
            'monto': i.monto,
            'gains_mes': i.gains_mes,
            'gains_anual': i.gains_anual,
            'backgroundColor': background_color,
            'borderColor': border_color,
        })

    return render(request, "metricas.html", {'data_instrumentos': data_instrumentos})


def eliminarInstrumento(request, pk):
    if request.method == 'POST':
        instrumento = get_object_or_404(Instrumento, pk=pk)
        instrumento.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("board:dashboard"))


# utillery
def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def lighten_color(r, g, b, factor=0.2):
    r = min(int(r + (255 - r) * factor), 255)
    g = min(int(g + (255 - g) * factor), 255)
    b = min(int(b + (255 - b) * factor), 255)
    return r, g, b
