# Weather-app-using-API
To understand how to use APIs (Application Programming Interfaces) to retrieve data from external sources such as weather and location services. The goal was to connect Python with real-time data systems and interpret the returned information.
✅ Objective:
To understand how to use APIs (Application Programming Interfaces) to retrieve data from external sources such as weather and location services. The goal was to connect Python with real-time data systems and interpret the returned information.

🔍 Activities Performed:
Connected to OpenWeatherMap API to fetch real-time weather data based on city input.

Used ipinfo.io API to detect the user’s current IP-based location.

Integrated Nominatim (geopy) for geocoding functionality.

💡 Key Concepts Learned:
Constructing and sending HTTP requests using the requests library.

Receiving and decoding JSON-formatted responses.

Extracting specific data fields (e.g., temperature, weather condition) from nested JSON objects.

⚠️ Challenges:
Understanding JSON hierarchy and key-paths for nested data.

Handling request errors like invalid responses or connectivity issues.

🧠 Reflections:
This week introduced a real-world context to Python programming. The ability to fetch dynamic data made the experience practical and highly engaging. It demonstrated Python’s strength in handling web communication.

✅ APIs
•	The code interacts with the OpenWeatherMap API.
•	It also makes an API request to ipinfo.io 
•	The Nominatim API from geopy is used for geocoding 
✅ JSON Parsing
•	The API responses from OpenWeatherMap and ipinfo.io return JSON data.
•	The code extracts specific information using data = response.json() and accesses values like data["main"]["temp"], data["weather"][0]["description"], etc.
✅ Error Handling
•	The try-except blocks handle possible errors when fetching weather data (get_weather(city)), detecting location (detect_location()), and updating the map (update_map(city)).
•	If an error occurs (e.g., network issues, invalid city input), it catches the exception and updates the UI with a meaningful message.
✅ Libraries like requests
•	The requests library is used for making HTTP requests to APIs.
•	It helps fetch weather data, detect the user's IP-based location, and retrieve JSON responses from APIs.
