from django.shortcuts import render
import json
import urllib.request

def index(request): 
    if request.method == 'POST': 
        city = request.POST['city']
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=239da6863bd92c4d702928d7e17a26d9'
        source = urllib.request.urlopen(api_url).read()
        list_of_data = json.loads(source)
        
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": f"{list_of_data['coord']['lon']} {list_of_data['coord']['lat']}",
            "temp": f"{list_of_data['main']['temp']}k",
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
    else: 
        data = {}
    return render(request, "main/index.html", data)
