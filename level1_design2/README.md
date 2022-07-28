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

The updated design is checked in as seq_detect_1011_Fix.v

## Verification Strategy

## Is the verification complete ?
