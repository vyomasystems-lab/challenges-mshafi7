# Bit manipulation coprocessor(Level2Design)

## Test Scenario **(Important)**
- Test Inputs: All instructions shown in the video are taken and random values are assigned to other three inputs  
- Expected Output: Python Model output should match the Dut output
- Observed Output: There are 11 mismatches out of 34 instructions.

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

![](https://github.com/vyomasystems-lab/challenges-mshafi7/blob/master/Images/level2_fail.png)



## Design Fix






## Verification Strategy
[0x00007033,0x00006033,0x00004033,0x40007033,0x40004022,0x00001033,0x00005033,0x20001033,0x20005033,0x60001033,0x60005033,0x48001033,0x28001033,0x68001033,0x48005033,0x28001033,0x68005033,
    0x00001013,0x00005013,0x40005013,0x20001013,0x20005013,0x60005013,0x48001013,0x28001013,0x68001013,0x48005013,0x28005013,0x68005013,0x06001033,0x06005033,0x04001033,0x04005033,0x04001013]

The above values are passed as 32 bit instructions to the input and the dut output is compared with expected output using for loop.  
## Is the verification complete ?
- The Verification is complete but Bugs are not fixed.
