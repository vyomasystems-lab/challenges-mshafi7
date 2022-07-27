# MUX Design Verification(Level1Design1)

## Test Scenario **(Important)**
- Test Inputs: all inputs are set to 1
- Expected Output: for sel value from 0 to 30 expected output is 1
- Observed Output in the DUT dut.out = 0 at 13 ns and also at 30n2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
      5'b01011: out = inp11;
      5'b01101: out = inp12;    <== Bug "two cases with 01101"
      5'b01101: out = inp13;
      5'b01110: out = inp14;
```
```
      5'b11101: out = inp29;    <== inp30 is not assigned
      default: out = 0;
    endcase
```

So assigning ``5'b11110: out = inp30;`` and ``5'b01100: out = inp12;`` in the design code will fix the bug.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-mshafi7/blob/master/Images/MUX_pass.png)

The updated design is checked in as adder_fix.v

## Verification Strategy
Assigning a constant value to all the input except select line and creating a loop in which select line value is varied and output is observed. If output doesn't match the input value commonly assigned then there is a bug. For every loop there is 1ns Delay so we can find the bug based on failure time.
## Is the verification complete ?
- Yes the Verification is Complete

# Sequence Detector(Level1Design2)

## Test Scenario **(Important)**
- Test Inputs: 111011 and 1011011 (overlaping Sequence)
- Expected Output: Machine should detect sequence for overlapping sequence
- Observed Output in the DUT dut.out = Sequence not detected for overlapping sequence 

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
      SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;    <== Bug
        else
```
```
      SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;     <== BUG
```
```
    SEQ_1011:
        next_state = IDLE;    <== BUG
```

So assigning ``next_state = SEQ_1;`` in else of SEQ_1 state, assigning ``next_state = SEQ_10;`` in else of SEQ_101 state and putting if condition ``if(inp_bit == 1)
        next_state = SEQ_1;
      else
        next_state = SEQ_10;
      end`` in SEQ_1011 state fixed the bug.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-mshafi7/blob/master/Images/Seq_Pass.png)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?

# Bit manipulation coprocessor(Level2Design)

## Test Scenario **(Important)**
- Test Inputs: All instructions shown in the video are taken and random values are assigned to other three inputs  
- Expected Output: Python Model output should match the Dut output
- Observed Output: There are 11 mismatches out of 34 instructions.

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following



So assigning ``5'b11110: out = inp30;`` and ``5'b01100: out = inp12;`` in the design code will fix the bug.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as adder_fix.v

## Verification Strategy
[0x00007033,0x00006033,0x00004033,0x40007033,0x40004022,0x00001033,0x00005033,0x20001033,0x20005033,0x60001033,0x60005033,0x48001033,0x28001033,0x68001033,0x48005033,0x28001033,0x68005033,
    0x00001013,0x00005013,0x40005013,0x20001013,0x20005013,0x60005013,0x48001013,0x28001013,0x68001013,0x48005013,0x28005013,0x68005013,0x06001033,0x06005033,0x04001033,0x04005033,0x04001013]

The above values are passed as 32 bit instructions to the input and the dut output is compared with expected output using for loop.  
## Is the verification complete ?
- The Verification is complete but Bugs are not fixed.

# SPI Master Controller(Level3)

## Test Scenario **(Important)**
- Test Inputs: all inputs are set to 1
- Expected Output: for sel value from 0 to 30 expected output is 1
- Observed Output in the DUT dut.out = 0 at 13 ns and also at 30n2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
      5'b01011: out = inp11;
      5'b01101: out = inp12;    <== Bug "two cases with 01101"
      5'b01101: out = inp13;
      5'b01110: out = inp14;
```
```
      5'b11101: out = inp29;    <== inp30 is not assigned
      default: out = 0;
    endcase
```

So assigning ``5'b11110: out = inp30;`` and ``5'b01100: out = inp12;`` in the design code will fix the bug.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://i.imgur.com/5XbL1ZH.png)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?