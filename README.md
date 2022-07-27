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

## Is the verification complete ?

# Sequence Detector(Level1Design2)

## Test Scenario **(Important)**
- Test Inputs: all inputs are set to 1
- Expected Output: for sel value from 0 to 30 expected output is 1
- Observed Output in the DUT dut.out = 0 at 13 ns and also at 30n2

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
    SEQ_1011:
        next_state = IDLE;    <== BUG
```

So assigning ``5'b11110: out = inp30;`` and ``5'b01100: out = inp12;`` in the design code will fix the bug.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-mshafi7/blob/master/Images/Seq_Pass.png)

The updated design is checked in as adder_fix.v

## Verification Strategy

## Is the verification complete ?

# (Level2Design)

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

# (Level3)

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