# Weather App

This project is a simple weather application using Python, Tkinter, and the OpenWeatherMap API. The application allows users to select an Indian state and display the current weather, temperature, and humidity.

## Prerequisites

- Python 3.x
- Tkinter
- Pillow
- requests

## Getting Started

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. **Install dependencies:**

    ```bash
    pip install pillow requests
    ```

### OpenWeatherMap API Key

To run this application, you need an API key from OpenWeatherMap. You can get one by signing up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).

Replace the `api_key` variable in the `get_weather` function with your API key:

```python
api_key = "your_openweathermap_api_key"
