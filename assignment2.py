import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import geopy.distance

# Define center of town coordinates
center_of_town = (35.220833, -97.443611)


def get_weather_code(location, time):
  # Implement logic to retrieve weather code based on location and time (e.g., using an API)
  # Replace this with your implementation
  # For now, we'll just return a dummy value
  return 0

def get_side_of_town(location):
  # Use geopy to calculate direction from location to center of town
  geocoder = geopy.Nominatim(user_agent="assignment2.py")
  location_coordinates = geocoder.geocode(location).xy
  dx, dy = map(lambda x: x[0] - x[1], zip(location_coordinates, center_of_town))
  cardinal_directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
  angle = (math.atan2(dy, dx) + np.pi) % (2 * np.pi)
  return cardinal_directions[int(angle / (np.pi / 4))]

def process_file(url):
  response = urlopen(url)
  soup = BeautifulSoup(response.read(), 'html.parser')

  # Extract relevant data (day, time, location, nature, EMS status)
  # Implement logic to extract data from the specific structure of your PDFs
  # This is just an example structure
  data = []
  for incident in soup.find_all('div', class_='incident'):
    day_of_week = ...  # Extract day of week from incident data
    time_of_day = ...   # Extract time of day from incident data
    location = ...     # Extract location from incident data
    nature = ...       # Extract nature of incident from incident data
    ems_stat = ...     # Extract EMS status from incident data
    data.append((day_of_week, time_of_day, location, nature, ems_stat))

  # Rank locations and incident natures by frequency
  location_counts = {loc: 0 for loc in set([d[2] for d in data])}
  for loc in [d[2] for d in data]:
    location_counts[loc] += 1
  location_ranks = {loc: rank for rank, loc in enumerate(sorted(location_counts, key=location_counts.get, reverse=True), 1)}

  nature_counts = {nat: 0 for nat in set([d[3] for d in data])}
  for nat in [d[3] for d in data]:
    nature_counts[nat] += 1
  nature_ranks = {nat: rank for rank, nat in enumerate(sorted(nature_counts, key=nature_counts.get, reverse=True), 1)}

  # Augment data with additional features
  for i, (day, time, location, nature, ems) in enumerate(data):
    weather_code = get_weather_code(location, time)
    side_of_town = get_side_of_town(location)
    rank = i + 1  # Order incidents by appearance in the PDF
    print(f"{day}\t{time}\t{weather_code}\t{location_ranks[location]}\t{side_of_town}\t{rank}\t{nature_ranks[nature]}\t{nature}\t{ems}")

def main():
  if len(sys.argv) != 3 or sys.argv[1] != "--urls":
    print("Usage: python assignment2.py --urls <filename>", file=sys.stderr)
    sys.exit(1)

  with open(sys.argv[2]) as f:
    for url in f:
      process_file(url.strip())

if __name__ == "__main__":
  main()
