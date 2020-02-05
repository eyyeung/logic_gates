# Making LogicGate in Python , the logic gate takes user input and output either 1 or 0
# To connect multiple logic gates, a connector is used
# A setNextPin(n) can be used to set the input of the logic gate instead of asking for user input
# connector would automatically set the output of the from gate to the input of the to gate

class LogicGate:
    def __init__(self, n):
        # Label is the name of the gate
        self.label = n
    
    def getLabel(self):
        return self.label

    def getOutput(self):
        #This would perform the the necessary calculation and return an output, which can be printed
        output = self.performGateLogic()
        return output

    def getPin(self):
        pin = int(input())
        # input checking, if not 1 or 0, ask user to reenter
        while (pin!=1) and (pin!=0):
            print("Please enter 1 or 0 only: ")
            pin = int(input())
        
        return pin
    
#Binary Gate needs two pins (Two inputs- pin A and pin B)
class BinaryGate(LogicGate):
    def __init__(self, n):
        LogicGate.__init__(self,n)
        self.pinATaken = False
        self.pinBTaken = False

    def getPinA(self):
        if (self.pinATaken== False):
            print("Enter Pin A input for gate %s: (1 or 0)"%(self.label))
            self.pinA = LogicGate.getPin(self)
            self.pinATaken = True
        return self.pinA
    
    def getPinB(self):
        if (self.pinBTaken== False):
            print("Enter Pin B input for gate %s: (1 or 0)"%(self.label))
            self.pinB = LogicGate.getPin(self)
            self.pinBTaken = True
        return self.pinB

    # set the next empty pin to the source (1 or 0 presumbly)
    def setNextPin(self, source):
        if (self.pinATaken == False):
            self.pinA = source
            self.pinATaken = True
        elif (self.pinBTaken == False):
            self.pinB = source
            self.pinBTaken = True
            
#Unary Gate only needs one input / one pin
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinTaken = False
    
    def getPin(self):
        if (self.pinTaken == False):
            print("Enter Pin input for gate %s: "%(self.label))
            self.pin = LogicGate.getPin(self)
            self.pinTaken = True
        return self.pin

    #sets the next empty pin
    def setNextPin(self, source):
        if (self.pinTaken == False):
            self.pin = source
            self.pinTaken = True
        else:
            return

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = BinaryGate.getPinA(self)
        b = BinaryGate.getPinB(self)
        if (a == 1 and b==1):
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = BinaryGate.getPinA(self)
        b = BinaryGate.getPinB(self)
        if (a != b):
            return 1
        elif (b==1 and a==1):
            return 1
        else:
            return 0
class XnorGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = BinaryGate.getPinA(self)
        b = BinaryGate.getPinB(self)
        if (a == b):
            return 1
        else:
            return 0

class XorGate(BinaryGate):
    def __init__(self,n):
        # super().__init__(n) or sepcify BinaryGate.__init__(self,n)
        super().__init__(n)

    def performGateLogic(self):
        a = super().getPinA()
        b = BinaryGate.getPinB(self)
        if (a != b):
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        pin = UnaryGate.getPin(self)
        if (pin == 1):
            return 0
        elif (pin == 0):
            return 1
            
#Connector class will have a fromgate and a togate, it will have instances of LogicGate but not part of the hierarchy- has a HAS-A relationship (no inheritance)

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        self.getInput()
    #This allow us to set the output from a from gate as an input to the to gate
    def getInput(self):
        self.togate.setNextPin(self.fromgate.getOutput())

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

# Testing the gate

# gand = XorGate("gand")
# print(gand.getOutput())

# Testing the conncector
gand1 = AndGate (" AND1 ") #creating an AND Gate with the name " AND1 "
gand2 = AndGate (" AND2 ") #creating an AND Gate with the name " AND2 "
gor3= OrGate(" OR ") #creating a OR Gate with the name " OR "
gnot4= NotGate(" NOT ") #Creating a NOT Gate with the name " NOT "

gand1.setNextPin(1) # this sets the first pin of the AND gate to 1
gand1.setNextPin(1) # sets the second pin of the AND gate to 1
gand2.setNextPin(0) # sets the first pin of the AND gate to 0
gand2.setNextPin(0) # sets the second pin of the AND gate to 0

c1 = Connector(gand1, gor3) # Connects gand1 and gor3 so the output of gand1 would be the first input of gor3
c2 = Connector(gand2, gor3) # Connects gand2 and gor3 so the output of gand2 would be the second input of gor3
c3 = Connector(gor3, gnot4) # Connects gor3 to gnot4, so output of gor3 is input to gnot4

print (gnot4.getLabel(),"( (",gand1.getPinA(),gand1.getLabel(),gand1.getPinB(),")",gor3.getLabel(),"(",gand2.getPinA(),gand2.getLabel(),gand2.getPinB(),") )","results in ",gnot4.getOutput())

#building a half adder in Python using the existing Logic Gates
#Half adder should have a Carry and a Sum
#Desired output:
# Inputs	Outputs
# A	B	C	S
# 0	0	0	0
# 1	0	0	1
# 0	1	0	1
# 1	1	1	0

def half_adder(A=0,B=0):
    # return sum then carry
    gsum = XorGate("sum")
    gcarry = AndGate("carry")
    gsum.setNextPin(A)
    gsum.setNextPin(B)
    gcarry.setNextPin(A)
    gcarry.setNextPin(B)
    halfadder_sum = gsum.getOutput()
    halfadder_carry = gcarry.getOutput()
    halfadder = {'carry':halfadder_carry, 'sum': halfadder_sum}
    return halfadder
half_adder = half_adder()
print(half_adder)