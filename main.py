##  this is just a poc rn so dont make fun of me
##  if you do i will literally groom you

#pip install python-weather
#pip install pygame

if __name__=="__main__":
  import python_weather
  import pygame

  import asyncio
  import os

  async def getweather():
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
      # fetch a weather forecast from a city
      weather = await client.get('New York')
      
      # returns the current day's forecast temperature (int)
      print(weather.current.temperature)
      
      # get the weather forecast for a few days
      for forecast in weather.forecasts:
        print(forecast)
        
        # hourly forecasts
        for hourly in forecast.hourly:
          print(f' --> {hourly!r}')
  
  #shameless api rip lmao
  #add ui with pygame later
  #oooh ooh and its judt likr buddy hoolllyy
