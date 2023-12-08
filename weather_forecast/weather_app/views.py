from django.shortcuts import render
from .weather_lookup import get_weather_forecast
from django.conf import settings
def weather_lookup(request):
    if request.method == 'POST':
        time_input = request.POST.get('time_input')

        API_KEY = settings.API_KEY
        CALICUT_COORDINATES = {'lat': 11.2588, 'lon': 75.7804}

        try:
            weather_data = get_weather_forecast(API_KEY, **CALICUT_COORDINATES, time_input=time_input)
            try:
                if weather_data.startswith("No weather data"):
                        return render(request, 'weather_lookup.html', {'weather_data_error': weather_data})

            except:
                    return render(request, 'weather_lookup.html', {'weather_data': weather_data})
            

        except Exception as e:
            
            return render(request, 'weather_lookup.html', {'weather_data_error': str(e)})

    return render(request, 'weather_lookup.html')
