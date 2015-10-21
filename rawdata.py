
fred = {'response': {'termsofService': 'http://www.wunderground.com/weather/api/d/terms.html', 'version': '0.1', 'features': {'conditions': 1}}, 'current_observation': {'observation_location': {'country': 'US', 'elevation': '436 ft', 'full': 'Silvergrove, Cary, North Carolina', 'longitude': '-78.798088', 'latitude': '35.806118', 'city': 'Silvergrove, Cary', 'country_iso3166': 'US', 'state': 'North Carolina'}, 'visibility_km': '16.1', 'UV': '0.0', 'relative_humidity': '70%', 'wind_dir': 'SW', 'feelslike_string': '52.9 F (11.6 C)', 'wind_mph': 0.0, 'icon': 'clear', 'history_url': 'http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=KNCCARY73', 'heat_index_string': 'NA', 'ob_url': 'http://www.wunderground.com/cgi-bin/findweather/getForecast?query=35.806118,-78.798088', 'pressure_in': '30.33', 'windchill_f': 'NA', 'temperature_string': '52.9 F (11.6 C)', 'precip_1hr_metric': ' 0', 'local_tz_short': 'EDT', 'wind_kph': 0, 'local_epoch': '1445390619', 'local_time_rfc822': 'Tue, 20 Oct 2015 21:23:39 -0400', 'weather': 'Clear', 'visibility_mi': '10.0', 'precip_1hr_in': '0.00', 'observation_epoch': '1445390619', 'wind_gust_mph': 0, 'heat_index_c': 'NA', 'wind_gust_kph': 0, 'pressure_trend': '0', 'local_tz_long': 'America/New_York', 'observation_time_rfc822': 'Tue, 20 Oct 2015 21:23:39 -0400', 'precip_today_string': '0.00 in (0 mm)', 'precip_1hr_string': '0.00 in ( 0 mm)', 'local_tz_offset': '-0400', 'nowcast': '', 'temp_c': 11.6, 'forecast_url': 'http://www.wunderground.com/US/NC/Cary.html', 'estimated': {}, 'image': {'title': 'Weather Underground', 'url': 'http://icons.wxug.com/graphics/wu2/logo_130x80.png', 'link': 'http://www.wunderground.com'}, 'dewpoint_string': '43 F (6 C)', 'dewpoint_f': 43, 'windchill_string': 'NA', 'precip_today_metric': '0', 'icon_url': 'http://icons.wxug.com/i/c/k/nt_clear.gif', 'wind_string': 'Calm', 'feelslike_f': '52.9', 'pressure_mb': '1027', 'precip_today_in': '0.00', 'windchill_c': 'NA', 'heat_index_f': 'NA', 'observation_time': 'Last Updated on October 20, 9:23 PM EDT', 'display_location': {'country': 'US', 'full': 'Cary, NC', 'longitude': '-78.79499817', 'city': 'Cary', 'zip': '27513', 'state_name': 'North Carolina', 'elevation': '147.00000000', 'wmo': '99999', 'latitude': '35.80550003', 'state': 'NC', 'country_iso3166': 'US', 'magic': '1'}, 'wind_degrees': 223, 'station_id': 'KNCCARY73', 'temp_f': 52.9, 'dewpoint_c': 6, 'feelslike_c': '11.6', 'solarradiation': '0'}}

# test = fred['current_observation']['wind_degrees']
# temp = fred['current_observation']['temp_f']
location = fred['current_observation']['display_location']['city']
weather = fred['current_observation']['weather']
ts = fred['current_observation']['temperature_string']
rh = fred['current_observation']['relative_humidity']
winds = fred['current_observation']['wind_string']
windg = fred['current_observation']['wind_gust_kph']
dews = fred['current_observation']['dewpoint_string']


# print("The current 'wind_degrees' are: {}".format(test))
# print("The local temperature is: {}".format(temp))
print("In the city of: {}, the weather is {}.".format(location, weather))
print("the temperature is: {}".format(ts))
print("the relative humidity is: {}".format(rh))
print("the winds are: {}".format(winds))
print("the gusts is: {}".format(windg))
print("the dewpoint: {}".format(dews))
