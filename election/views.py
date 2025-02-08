from django.shortcuts import render, get_object_or_404
from .models import PollingUnit, AnnouncedPuResults, Lga

def polling_unit_selection(request):
    polling_units = PollingUnit.objects.all()
    return render(request, 'polling_unit_selection.html', {'polling_units': polling_units})

def polling_unit_results(request):
    if request.method == 'POST':
        uniqueid = request.POST.get('uniqueid')
        polling_unit = get_object_or_404(PollingUnit, uniqueid=uniqueid)
        results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=uniqueid)
        return render(request, 'polling_unit_results.html', {'polling_unit': polling_unit, 'results': results})
    return render(request, 'polling_unit_selection.html')

def lga_results(request):
    if request.method == 'POST':
        lga_id = request.POST.get('lga_id')
        polling_units = PollingUnit.objects.filter(lga_id=lga_id)
        results = AnnouncedPuResults.objects.filter(polling_unit_uniqueid__in=polling_units)
        party_totals = {}
        for result in results:
            party_totals[result.party_abbreviation] = party_totals.get(result.party_abbreviation, 0) + result.party_score
        return render(request, 'lga_results.html', {'party_totals': party_totals})
    lgas = Lga.objects.all()
    return render(request, 'lga_selection.html', {'lgas': lgas})

def add_polling_unit_results(request):
    if request.method == 'POST':
        polling_unit_id = request.POST['polling_unit_id']
        parties = request.POST.getlist('party_abbreviation')
        scores = request.POST.getlist('party_score')
        for party, score in zip(parties, scores):
            AnnouncedPuResults.objects.create(polling_unit_uniqueid_id=polling_unit_id, party_abbreviation=party, party_score=score)
        return render(request, 'success.html')
    return render(request, 'add_results.html')

