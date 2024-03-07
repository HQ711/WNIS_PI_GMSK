"""
Embedded Python Blocks:


Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""


import numpy as np
from gnuradio import gr
import time




class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
   """Embedded Python Block example - a simple multiply const"""


   def __init__(self, default_parameters = 0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Print Message',   # will show up in GRC
            in_sig=[np.byte],
            out_sig=None
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.dr_start_time = None
        self.dr_count_packet = None
        #Initialize Timer
        self.dr_start_time = time.time()
        self.dr_count_packet = 0


   def work(self, input_items, output_items):
        """example: multiply with constant"""
        for data in input_items[0]:
            # print(data)
            # try:
            #     print(chr(data),end='')
            # except:
            #     pass
            self.dr_count_packet += 1
            if time.time() - self.dr_start_time >= 1:
                #print("data rate:", self.dr_count_packet*8/(time.time() - self.dr_start_time)/1000,'kbps')
                print(self.dr_count_packet*8/(time.time() - self.dr_start_time)/1000)
                self.dr_count_packet = 0
                self.dr_start_time = time.time()
        # print(input_items[0][:])
        # output_items[0][:] = input_items[0] * self.example_param
        return len(input_items[0])




