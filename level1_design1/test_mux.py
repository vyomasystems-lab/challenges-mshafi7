# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    A = 20
    x=1
    dut.sel.value = A
    #cocotb.log.info('##### CTB: Develop your test here ########')
    #for i in range(30):
    dut.inp20.value = 1

    await Timer(2, units='ns')
    assert dut.out.value == 1, f"Adder result is incorrect: {dut.inp30.value} != 1"
        
        #dut._log.info(f'A={A:05} B={B:05} model={A+B:05} DUT={int(dut.sum.value):05}')
        #assert dut.sum.value == A+B, "Randomised test failed with: {A} + {B} = {SUM}".format(
         #   A=dut.a.value, B=dut.b.value, SUM=dut.sum.value)
