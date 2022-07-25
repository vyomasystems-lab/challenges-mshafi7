# FINAL REPORT
# MUX Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

*Make sure to include the Gitpod id in the screenshot*

![](https://i.imgur.com/miWGA1o.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in 4-bit inputs *a* and *b* and gives 5-bit output *sum*

The values are assigned to the input port using 
```
dut.a.value = 7
dut.b.value = 5
```

The assert statement is used for comparing the adder's outut to the expected value.

The following error is seen:
```
assert dut.sum.value == A+B, "Adder result is incorrect: {A} + {B} != {SUM}, expected value={EXP}".format(
                     AssertionError: Adder result is incorrect: 7 + 5 != 2, expected value=12
```
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
