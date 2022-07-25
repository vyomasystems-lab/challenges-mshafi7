# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

from model_mkbitmanip import *

# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 

# Sample Test
@cocotb.test()
def ANDN1(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))
    
    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    #mav_putvalue_instr = 0x101010B3
    func7 = 0b0100000*(2**25)
    func3 = 0b110*(2**12)
    opcode = 0b0110011
    x = func7 + func3 + opcode

    # expected output from the model
    #expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)
    mav_putvalue=mav_putvalue_src1 | (~mav_putvalue_src2)
    mav_putvalue=mav_putvalue & 0xffffffff
    mav_putvalue=(mav_putvalue<<1)|1
    expected_mav_putvalue = mav_putvalue

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    #dut.mav_putvalue_instr.value = mav_putvalue_instr
    dut.mav_putvalue_instr.value = x
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def ORN2(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    #mav_putvalue_instr = 0x101010B3
    func7 = 0b0100000*(2**25)
    func3 = 0b111*(2**12)
    opcode = 0b0110011
    x = func7 + func3 + opcode

    # expected output from the model
    #expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)
    mav_putvalue=mav_putvalue_src1 & (~mav_putvalue_src2)
    mav_putvalue=mav_putvalue & 0xffffffff
    mav_putvalue=(mav_putvalue<<1)|1
    expected_mav_putvalue = mav_putvalue

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    #dut.mav_putvalue_instr.value = mav_putvalue_instr
    dut.mav_putvalue_instr.value = x
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def XNOR3(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    #mav_putvalue_instr = 0x101010B3
    func7 = 0b0100000*(2**25)
    func3 = 0b100*(2**12)
    opcode = 0b0110011
    x = func7 + func3 + opcode

    # expected output from the model
    #expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)
    mav_putvalue=mav_putvalue_src1 ^ (~mav_putvalue_src2)
    mav_putvalue=mav_putvalue & 0xffffffff
    mav_putvalue=(mav_putvalue<<1)|1
    expected_mav_putvalue = mav_putvalue

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    #dut.mav_putvalue_instr.value = mav_putvalue_instr
    dut.mav_putvalue_instr.value = x
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

@cocotb.test()
def SLO4(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))

    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    #mav_putvalue_instr = 0x101010B3
    func7 = 0b0100000*(2**25)
    func3 = 0b100*(2**12)
    opcode = 0b0110011
    x = func7 + func3 + opcode

    # expected output from the model
    #expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)
    shamt1 =mav_putvalue_src2 & (31)
    out=((mav_putvalue_src1)<< shamt1)
    res=out
    min_i=0
    max_i=shamt1
    if(shamt1==0):
       mav_putvalue = out
    else:
        while (min_i<max_i):
            res=((1 << min_i) | res)
            min_i=min_i+1
            mav_putvalue=res & 0xffffffff
    mav_putvalue=(mav_putvalue<<1)|1

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    #dut.mav_putvalue_instr.value = mav_putvalue_instr
    dut.mav_putvalue_instr.value = x
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message
