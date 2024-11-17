#include <SoftwareSerial.h>

// Example data sensors (replace with real sensors in your setup)
float vehicleSpeed = 60.5; // Example speed in km/h
float gpsLatitude = 37.7749; // Example latitude
float gpsLongitude = -122.4194; // Example longitude

void setup() {
  Serial.begin(9600); // Start serial communication
  Serial.println("Starting V2X Data Capture...");
}

void loop() {
  // Simulate data capture
  String data = String(vehicleSpeed) + "," + 
                String(gpsLatitude) + "," + 
                String(gpsLongitude);

  // Send data over serial to Python
  Serial.println(data);
  delay(1000); // Delay for 1 second
}
