uint16_t selectPin = 2;
uint16_t horizPin = 0;
uint16_t vertPin = 1;
int16_t horizCalibration;
int16_t vertCalibration;

int16_t mapJoystick(int16_t value, int16_t calibration) {
  return map(value, 0, 1023, -64, 63) - calibration;
}

void setup() {
  Serial.begin(9600);
  pinMode(selectPin, INPUT);
  digitalWrite(selectPin, HIGH);

  Serial.println(" ");
  Serial.println(" ");

  horizCalibration = mapJoystick(analogRead(horizPin), 0);
  vertCalibration = mapJoystick(analogRead(vertPin), 0);
  Serial.print("Initial values: Horiz: ");
  Serial.print(horizCalibration);
  Serial.print("; Vert: ");
  Serial.println(vertCalibration);
}

void loop() {
  int16_t horiz = mapJoystick(analogRead(horizPin), horizCalibration);
  int16_t vert = mapJoystick(analogRead(vertPin), vertCalibration);
  uint16_t selected = digitalRead(selectPin);

  Serial.print("Horiz: ");
  Serial.print(horiz);
  Serial.print("; Vert: ");
  Serial.print(vert);
  Serial.print("; Selected? ");
  Serial.println(selected);
}
