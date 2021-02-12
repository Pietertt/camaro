#define echoPin 2
#define trigPin 3
#define ldrPin A0
#define pirPin 7

long duration;
int distance;
int ldr;
int valid;
int pirState = LOW;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ldrPin, INPUT);
  pinMode(pirPin, INPUT);
 
  Serial.begin(9600);
}

void loop() {
  DDRB = 0x3F;
  
  PORTB = B0111111;
  delay(10);
  PORTB = B0000000;
  
  digitalWrite(trigPin, LOW);
  delay(1000);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  valid = digitalRead(pirPin);

  duration = pulseIn(echoPin, HIGH);
  
  distance = duration * 0.034 / 2;
  
  ldr = map(analogRead(ldrPin), 0, 1023, 0, 100);
 
  Serial.println("s" + String(distance)  + "/" + "x" + String(ldr) + "/" + "v" + String(valid));
  
  delay(1000);
}
