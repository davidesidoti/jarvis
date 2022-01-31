#include <Servo.h>

Servo mask1;
Servo mask2;

int maskReceived = 0;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(1);

  mask1.attach(3);
  mask2.attach(5);

  for (int i = 90; i > 0; i--) {
    mask1.write(i);
    delay(5);
  }

  for (int i = 90; i > 0; i--) {
    mask2.write(i);
    delay(5);
  }
}

void loop() {
  while (!Serial.available());
  maskReceived = Serial.readString().toInt();

  if (maskReceived == 0) {
    for (int i = 90; i > 0; i--) {
      mask1.write(i);
      delay(5);
    }

    for (int i = 90; i > 0; i--) {
      mask2.write(i);
      delay(5);
    }
  }
  else if (maskReceived == 1) {
    for (int i = 0; i < 90; i++) {
      mask1.write(i);
      delay(5);
    }

    for (int i = 0; i < 90; i++) {
      mask2.write(i);
      delay(5);
    }
  }
}
