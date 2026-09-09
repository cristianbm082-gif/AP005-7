#Micropython
from machine import Pin
from time import sleep

led = Pin(2,Pin.OUT)

led.on()
sleep(1)
led.off()

C++
void setup() {
  pinMode(2, OUTPUT);    
  digitalWrite(2, HIGH); 
  delay(1000);           
  digitalWrite(2, LOW);  
}

void loop() {
  
}
