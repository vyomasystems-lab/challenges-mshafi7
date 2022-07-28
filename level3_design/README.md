# SPI Master Controller(Level3)

## Test Scenario **(Important)**
- Test Inputs: a ramdom input data is given and start signal is asserted
- Expected Output: The data should be transmitted bit by bit at Falling edge of sck and the done, sck, slave select(ss) should turn high after transmission.
- Observed Output: 

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

![](https://github.com/vyomasystems-lab/challenges-mshafi7/blob/master/Images/Level3_pass.png)


So assigning ``ss=0`` in the design code will fix the bug.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-mshafi7/blob/master/Images/Level3_pass.png)

The updated design is checked in as SPI_fix.v

## Verification Strategy

## Is the verification complete ?
