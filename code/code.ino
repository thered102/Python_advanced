void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}
int a = 0;
int b = 0;

void loop() {
  a = a + 1;
  b = b - 1;
  String str = "@" + String(a) + "#" + String(b) + "$";
  Serial.println(str);
  // put your main code here, to run repeatedly:
  if (Serial.available())
  {
    int inByte = Serial.read();
    Serial.write(inByte);
  if (inByte == 'S')
  {
    digitalWrite(13, HIGH);
  }
  else
  digitalWrite(13, LOW);
  }

  // digitalWrite(13, LOW);
  // delay(5000);
  // digitalWrite(13, HIGH);
  // delay(5000);
  delay(1000);
}
