#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2018 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import scratch_radio_swig as scratch_radio

class qa_cic_interpolator_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        srcData = (
            1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        refData = (
            1.0/25, 3.0/25, 6.0/25, 10.0/25, 15.0/25, 18.0/25,
            19.0/25, 18.0/25, 15.0/25, 10.0/25, 6.0/25, 3.0/25,
            1.0/25, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        source = blocks.vector_source_c(srcData)
        interpolator = scratch_radio.cic_interpolator_cc(5, 3)
        sink = blocks.vector_sink_c()
        self.tb.connect(source, interpolator)
        self.tb.connect(interpolator, sink)
        self.tb.run()
        self.assertComplexTuplesAlmostEqual(refData, sink.data())

    def test_002_t (self):
        srcData = (
            1, 1, 1, 1, 1, 0, 0, 0, 0, 0)
        refData = (
            1.0/25, 3.0/25, 6.0/25, 10.0/25, 15.0/25,
            19.0/25, 22.0/25, 24.0/25, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 24.0/25, 22.0/25, 19.0/25,
            15.0/25, 10.0/25, 6.0/25, 3.0/25, 1.0/25,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0)
        source = blocks.vector_source_c(srcData)
        interpolator = scratch_radio.cic_interpolator_cc(5, 3)
        sink = blocks.vector_sink_c()
        self.tb.connect(source, interpolator)
        self.tb.connect(interpolator, sink)
        self.tb.run()
        self.assertComplexTuplesAlmostEqual(refData, sink.data())

if __name__ == '__main__':
    gr_unittest.run(qa_cic_interpolator_cc, "qa_cic_interpolator_cc.xml")