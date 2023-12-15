#define PIN_TRIG_L 11
#define PIN_ECHO_L 12
#define PIN_TRIG_C 9
#define PIN_ECHO_C 8
#define PIN_TRIG_R 3
#define PIN_ECHO_R 2


void setup() {
  
  Serial.begin (9600);

  pinMode(PIN_TRIG_L, OUTPUT);
  pinMode(PIN_ECHO_L, INPUT);
  pinMode(PIN_TRIG_C, OUTPUT);
  pinMode(PIN_ECHO_C, INPUT);
  pinMode(PIN_TRIG_R, OUTPUT);
  pinMode(PIN_ECHO_R, INPUT);
}


long duration, distance, RightSensor,BackSensor,FrontSensor,LeftSensor;


void loop() {

  //SonarSensor(PIN_TRIG_L, PIN_ECHO_L);
  //LeftSensor = distance;
  SonarSensor(PIN_TRIG_C, PIN_ECHO_C);
  FrontSensor = distance;
  //SonarSensor(PIN_TRIG_R, PIN_ECHO_R);
  //RightSensor = distance;

  //Serial.print(LeftSensor);
  //Serial.print(" ");
  Serial.println(FrontSensor);
  //Serial.print(" ");
  //Serial.println(RightSensor);
  delay(100);
}


void SonarSensor(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  duration = pulseIn(echoPin, HIGH);
  distance = (duration/2) / 29.1;
  
}
