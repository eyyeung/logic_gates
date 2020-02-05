# Logic Gates
## Description
Different logic gates (and, or, nor, xnor, not) classes and connector class to build logical circuit written in Python.

Example includes some test cases and half adder.
## Classes
* LogicGate
 * BinaryGate
   * AndGate
   * OrGate
   * NorGate
   * XnorGate
 * UnaryGate
   * NotGate

* Connector

## Usage
Create new instance of a logic gate with the appropriate class:
'''python
gand1 = AndGate (" AND1 ")
'''
To set the pin of the logic gate by code (only input of 1 or 0 is accepted)
'''python
gand1.setNextPin(1)
'''
Otherwise, when calculating the output, it wil ask for user input on the pins:
'''python
print(gand1.getLabel())
'''
Connectors can be used to connect two gates:
'''python
c1 = Connector(gand1, gor3)
'''
