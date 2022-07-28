# See LICENSE.iitm for details
# See LICENSE.vyoma for details

import random
import sys
import cocotb
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.result import TestFailure
from cocotb.clock import Clock

"""
# Clock Generation
@cocotb.coroutine
def clock_gen(signal):
    while True:
        signal.value <= 0
        yield Timer(1) 
        signal.value <= 1
        yield Timer(1) 
"""


@cocotb.test()
async def test_spi_master(dut):

    # clock
    #cocotb.fork(clock_gen(dut.clk))
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start()) 


    mlb=1   
    rstb = 0
    start = 0
    m_tdat = 0b01111100
    cdiv = 1
    dut.rstb.value = rstb
    await Timer(20, units="ns") 
    rstb=1
    dut.rstb.value = rstb
    dut.start.value = start
    dut.tdat.value = m_tdat
    dut.cdiv.value = cdiv

    await Timer(20, units="ns") 
    start=1
    dut.start.value = start
    await Timer(20, units="ns")
    start =0
    dut.start.value = start
    await FallingEdge(dut.sck)
    dut.din.value <= 1
    cocotb.log.info(dut.dout.value)
    await RisingEdge(dut.sck)
    dut.din.value <= 0
    if dut.dout.value != 0:
        raise TestFailure("data mismatch")
    cocotb.log.info(dut.dout.value)
    await RisingEdge(dut.sck)
    dut.din.value <= 1
    if dut.dout.value != 1:
        raise TestFailure("data mismatch")
    cocotb.log.info(dut.dout.value)
    await RisingEdge(dut.sck)
    dut.din.value <= 0
    if dut.dout.value != 1:
        raise TestFailure("data mismatch")
    cocotb.log.info(dut.dout.value)
    await RisingEdge(dut.sck)
    dut.din.value <= 1
    if dut.dout.value != 1:
        raise TestFailure("data mismatch")
    cocotb.log.info(dut.dout.value)
    await RisingEdge(dut.sck)
    dut.din.value <= 1
    if dut.dout.value != 1:
        raise TestFailure("data mismatch")
    cocotb.log.info(dut.dout.value)
    await RisingEdge(dut.sck)
    dut.din.value <= 1
    if dut.dout.value != 1:
        raise TestFailure("data mismatch")
    cocotb.log.info(dut.dout.value)
    await RisingEdge(dut.sck)
    dut.din.value <= 0
    if dut.dout.value != 0:
        raise TestFailure("data mismatch")
    cocotb.log.info(dut.dout.value)
    await RisingEdge(dut.sck)
    if dut.dout.value != 0:
        raise TestFailure("data mismatch")
    await Timer(15,units='ns')

   # cocotb.log.info("Hey There",dut.rdata[0].value)
    assert (dut.done.value == 1) and (dut.ss.value == 1) and (dut.sck.value ==1), "fail"
