// Guardian Wing Drone Controller
#include <Arduino.h>

#define LED_PIN 2  // ESP32 dahili LED

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  Serial.println("SIM: Drone sistem hazır");
}

void loop() {
  if(Serial.available() && Serial.read() == 'T') {
    digitalWrite(LED_PIN, HIGH);
    Serial.println("EMERGENCY: Kalkış yapılıyor!");
    delay(3000);  // 3 saniye bekle
    digitalWrite(LED_PIN, LOW);
  }
}