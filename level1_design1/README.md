# MUX Design Verification(Level1Design1)

## Test Scenario **(Important)**
- Test Inputs: all inputs are set to 1
- Expected Output: for sel value from 0 to 30 expected output is 1
- Observed Output in the DUT dut.out = 0 at 13 ns and also at 30n2

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following
![](https://github.com/vyomasystems-lab/challenges-mshafi7/blob/master/Images/Mux_Fail_1.png)

```
      5'b01011: out = inp11;
      5'b01101: out = inp12;    <== Bug "two cases with 01101"
      5'b01101: out = inp13;
      5'b01110: out = inp14;
```
![](https://github.com/vyomasystems-lab/challenges-mshafi7/blob/master/Images/Mux_Fail_2.png)
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
