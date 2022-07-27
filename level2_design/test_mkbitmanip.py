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
def Bitmanip_test(dut):

    # clock
    cocotb.fork(clock_gen(dut.CLK))
    
    # reset
    dut.RST_N.value <= 0
    yield Timer(10) 
    dut.RST_N.value <= 1

    ######### CTB : Modify the test to expose the bug #############
    # input transaction
   # y=random.randint(0, 1000)
   #'0x{0:08X}'.format(20)
    mav_putvalue_src1 = 0x213
    mav_putvalue_src2 = 0x0
    mav_putvalue_src3 = 0x0
    mav_putvalue_instr = 0x101010B3
    
    x=[0x00007033,0x00006033,0x00004033,0x40007033,0x40004022,0x00001033,0x00005033,0x20001033,0x20005033,0x60001033,0x60005033,0x48001033,0x28001033,0x68001033,0x48005033,0x28001033,0x68005033,
    0x00001013,0x00005013,0x40005013,0x20001013,0x20005013,0x60005013,0x48001013,0x28001013,0x68001013,0x48005013,0x28005013,0x68005013,0x06001033,0x06005033,0x04001033,0x04005033,0x04001013]
    
    # expected output from the model
    #expected_mav_putvalue = bitmanip(x, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)
    

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    #dut.mav_putvalue_instr.value = mav_putvalue_instr
    cout=0
    for i in range(len(x)):
        dut.mav_putvalue_instr.value = x[i]
        expected_mav_putvalue = bitmanip(x[i], mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)
        yield Timer(1,units='ns') 
        # obtaining the output
        dut_output = dut.mav_putvalue.value
        cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
        cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
        # comparison
        error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
        if dut_output != expected_mav_putvalue:
            cout=cout+1
        cocotb.log.info(f'Total mismatches = {cout}')
    if cout != 0:
        assert False

