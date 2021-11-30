int dato;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  dato=analogRead(A1);
  Serial.println(dato);
  delay(100);
}
