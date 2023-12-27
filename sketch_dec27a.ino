
#include <Bounce2.h>

int button = 2;
int button1 = 3;

int led = 12;
int led1 = 13;

Bounce debouncer = Bounce();
Bounce debouncer1 = Bounce();


void setup() {

  pinMode(button,INPUT_PULLUP);
  debouncer.attach(button);
  debouncer.interval(5);
  pinMode(button1,INPUT_PULLUP);
  debouncer1.attach(button1);
  debouncer1.interval(5);
  
  Serial.begin(9600);
  
 
  
}

void loop() {
  debouncer.update();
  debouncer1.update();

  
  if(debouncer.fell())
  {
    
    Serial.println("right");
    digitalWrite(led, HIGH); 
   
  }
  if(debouncer.rose())
  {
    //Serial.println(" ");
    digitalWrite(led, LOW); 
  }  

  
  if(debouncer1.fell())
  {
    Serial.println("left");
    digitalWrite(led1, HIGH);
  }
  if(debouncer1.rose())
  {
    //Serial.println(" ");
    digitalWrite(led1, LOW);
  }  
}
