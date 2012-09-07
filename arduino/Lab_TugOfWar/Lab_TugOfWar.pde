/* Tug of war game:

Two players, Player 1 and Player 2, are at a 
board consisting of 2 push buttons and 3 LEDS

There are 3 LEDs
    RED1 GRN RED2
and 2 buttons
    B1 B2

The objective is to push your button faster than your opponent
so that when time runs out you have the rope on your side.

Whoever has pushed their button the most times will be
winning, and their red LED will turn on.  If the two buttons
are within Threshold of each other, then the players are
currently tied, and the green LED will be on.
   
*/
int P1LEDLowPin = 10;
int P1LEDHighPin = 11;
int P2LEDLowPin = 8;
int P2LEDHighPin = 5;
int LEDEvenPin = 9;

int P1ButtonPin = 7;
int P2ButtonPin = 6;

void configureLEDPinToBeDigitalOutput(int pin) {
  pinMode(pin, OUTPUT);
}

void setButtonPinToInput(int pin) {
  pinMode(pin, INPUT);
  digitalWrite(pin, HIGH);
}

void setup() {
  configureLEDPinToBeDigitalOutput(P1LEDLowPin);
  configureLEDPinToBeDigitalOutput(P1LEDHighPin);
  configureLEDPinToBeDigitalOutput(P2LEDLowPin);
  configureLEDPinToBeDigitalOutput(P2LEDHighPin);
  configureLEDPinToBeDigitalOutput(LEDEvenPin);

  setButtonPinToInput(P1ButtonPin);
  setButtonPinToInput(P2ButtonPin);
}

/* PushCount is incremented when player 1 pushes their
   button, and decremented when player 2 pushes their 
   button.  So if it is > 0 player 1 has made more pushes
   and if it is < 0 player 2 has made more pushes.
*/

int PushCount = 0;

/* PushCount has to be Threshold far away from zero before a
   player is considered to be winning.
*/

int Threshold = 5;
int HighThreshold = 8;

void turnOnLED(int pin) {
    digitalWrite(pin, HIGH);
}

void turnOffLED(int pin) {
    digitalWrite(pin, LOW);
}

void loop() {
  if ( digitalRead(P1ButtonPin) == LOW ) {
    PushCount++;
  }
  if ( digitalRead(P2ButtonPin) == LOW ) {
    PushCount--;
  }
 
  if ( PushCount > Threshold ) {
    turnOnLED(P1LEDLowPin);
    turnOffLED(P2LEDLowPin);
    turnOffLED(LEDEvenPin);
    if ( PushCount > HighThreshold ) {
      turnOnLED(P1LEDHighPin);
    } else {
      turnOffLED(P1LEDHighPin);
    }
  } else if ( PushCount < (0-Threshold) ) {
    turnOffLED(P1LEDLowPin);
    turnOnLED(P2LEDLowPin);
    turnOffLED(LEDEvenPin);
    if ( PushCount < (0-HighThreshold) ) {
      turnOnLED(P2LEDHighPin);
    } else {
      turnOffLED(P2LEDHighPin);
    }
  } else {
    turnOffLED(P1LEDLowPin);
    turnOffLED(P2LEDLowPin);
    turnOnLED(LEDEvenPin);
    turnOffLED(P1LEDHighPin);
    turnOffLED(P2LEDHighPin);
  }

  // wait 50 mS for any button bounce to die out
  delay(50);
}

