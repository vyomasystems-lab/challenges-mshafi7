# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1011011(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    x=[1,0,1,1,0,1,1]
    for i in range(len(x)):
        cocotb.log.info(f'input={x[i]} and output={int(dut.seq_seen.value)}')
        dut.inp_bit.value = x[i]
        await FallingEdge(dut.clk)
    cocotb.log.info(f'output={int(dut.seq_seen.value)}')
    assert dut.seq_seen.value == 1


@cocotb.test()
async def test_seq_bug111011(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset

    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    x=[1,1,1,0,1,1]
    for i in range(len(x)):
        cocotb.log.info(f'input={x[i]} and output={int(dut.seq_seen.value)}')
        dut.inp_bit.value = x[i]
        await FallingEdge(dut.clk)
    cocotb.log.info(f'output={int(dut.seq_seen.value)}')
    assert dut.seq_seen.value == 1

