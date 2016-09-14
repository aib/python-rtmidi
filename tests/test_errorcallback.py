#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for the error callback"""

import unittest
import unittest.mock

import rtmidi


class TestErrorCallback(unittest.TestCase):

    INVALID_PORT_NUMBER = 9999
    MIDI_OUT_ERROR_USER_DATA = 'midiOutError'
    MIDI_IN_ERROR_USER_DATA = 'midiInError'

    def setUp(self):
        self.midi_out = rtmidi.MidiOut()
        self.midi_in = rtmidi.MidiIn()

    def test_midiout_error_callback(self):
        errcb = unittest.mock.Mock()
        self.midi_out.set_error_callback(errcb, self.MIDI_OUT_ERROR_USER_DATA)
        self.midi_out.open_port(self.INVALID_PORT_NUMBER)
        errcb.assert_called_with(rtmidi.ERRORTYPE_INVALID_PARAMETER,
                                 unittest.mock.ANY,
                                 self.MIDI_OUT_ERROR_USER_DATA)

    def test_midiin_error_callback(self):
        errcb = unittest.mock.Mock()
        self.midi_in.set_error_callback(errcb, self.MIDI_IN_ERROR_USER_DATA)
        self.midi_in.open_port(self.INVALID_PORT_NUMBER)
        errcb.assert_called_with(rtmidi.ERRORTYPE_INVALID_PARAMETER,
                                 unittest.mock.ANY,
                                 self.MIDI_IN_ERROR_USER_DATA)


if __name__ == '__main__':
    unittest.main()
