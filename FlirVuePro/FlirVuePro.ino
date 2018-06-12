const int PWM3pin = 10;
const int PWM4pin = 11;

const int timer = 60;
int captured = 0;
char rx_byte;

void setup() {
  Serial.begin(9600);
  rx_byte = 0;
  pinMode(PWM3pin,OUTPUT);
  pinMode(PWM4pin,OUTPUT);
}

int positionColorPalette = 0;
int _counterChange = 0;
int _counterTrigger = 0;
void loop() {
  if (Serial.available() > 0){
     rx_byte = Serial.read();
    if ((rx_byte >= 48) && (rx_byte <= 57)){
      if (rx_byte == '1'){
//      // CHANGE COLOR PALETTE = 1
//      pwmLOW(PWM4pin, timer);
      // TRIGGER 1 COLOR PALETTE
      pwmHIGH(PWM3pin, timer);
      pwmLOW(PWM3pin, timer);
//      // CHANGE COLOR PALETTE = 2
//      pwmMID(PWM4pin, timer);
//      // TRIGGER 1 COLOR PALETTE
//      pwmHIGH(PWM3pin, timer);
//      pwmLOW(PWM3pin, timer);
//      // CHANGE COLOR PALETTE = 3
//      pwmHIGH(PWM4pin, timer);
//      // TRIGGER 1 COLOR PALETTE
//      pwmHIGH(PWM3pin, timer);
//      pwmLOW(PWM3pin, timer);
//      // ALL PWM TO LOW
//      pwmLOW(PWM4pin, timer);
//      pwmLOW(PWM3pin, timer);
      rx_byte = 0;
      captured++;
      Serial.println(captured);
      }
    }
  } else {
    pwmLOW(PWM4pin, timer);
    pwmLOW(PWM3pin, timer);
  }
}
// PWM 50Hz HIGH=2ms/20ms
static void pwmHIGH(int _pin, int _timer) {
  int _counter = 0;
  while (_counter < _timer){
    digitalWrite(_pin,HIGH);
    delay(2);
    digitalWrite(_pin,LOW);
    delay(18);
    _counter++;
  }
  Serial.println("pwmHIGH=" + String(_pin));
}
// PWM 50Hz MID=1.5ms/20ms
static void pwmMID(int _pin, int _timer) {
  int _counter = 0;
  while (_counter < _timer){
    digitalWrite(_pin,HIGH);
    delayMicroseconds(1500);
    digitalWrite(_pin,LOW);
    delay(18);
    delayMicroseconds(500);
    _counter++;
  }
  Serial.println("pwmMID=" + String(_pin));
}
// PWM 50Hz LOW=1ms/20ms
static void pwmLOW(int _pin, int _timer) {
  int _counter = 0;
  while (_counter < _timer){
    digitalWrite(_pin,HIGH);
    delay(1);
    digitalWrite(_pin,LOW);
    delay(19);
    _counter++;
  }
  Serial.println("pwmLOW=" + String(_pin));
}

