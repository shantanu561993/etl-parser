# -*- coding: utf-8 -*-

import unittest

from etl.parsers.kernel import Thread_TypeGroup1
from etl.parsers.kernel.core import build_mof
from etl.wmi import EventTraceGroup


class TestMofThreadParser(unittest.TestCase):
    def test_thread_v3_type_group_1_type1(self):
        payload = b'\x04\x00\x00\x00\x18\x01\x00\x00\x00\x90K\x17\x8b\x9e\xff\xff\x00 K\x17\x8b\x9e\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\xcfkm\x03\xf8\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x05\x02\x00\x00\x00'

        obj = build_mof(EventTraceGroup.EVENT_TRACE_GROUP_THREAD, 3, 1, payload)
        self.assertIsInstance(obj, Thread_TypeGroup1),
        self.assertEqual(obj.get_process_id(), 4)
        self.assertEqual(obj.get_thread_id(), 280)

    def test_thread_v3_type_group_1_type2(self):
        payload = b'\x04\x00\x00\x00\\\x01\x00\x00\x00\x10S\x17\x8b\x9e\xff\xff\x00\xa0R\x17\x8b\x9e\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x80\x9a\xb8q\x03\xf8\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x05\x02\x00\x00\x00'

        obj = build_mof(EventTraceGroup.EVENT_TRACE_GROUP_THREAD, 3, 2, payload)
        self.assertIsInstance(obj, Thread_TypeGroup1),
        self.assertEqual(obj.get_process_id(), 4)
        self.assertEqual(obj.get_thread_id(), 348)

    def test_thread_v3_type_group_1_type3(self):
        payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0&s\x03\xf8\xff\xff\x00`&s\x03\xf8\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xd0O|m\x03\xf8\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00'

        mof = build_mof(EventTraceGroup.EVENT_TRACE_GROUP_THREAD, 3, 3, payload)
        self.assertIsInstance(mof, Thread_TypeGroup1),
        self.assertEqual(mof.get_process_id(), 0)
        self.assertEqual(mof.get_thread_id(), 0)

    def test_thread_v3_type_group_1_type4(self):
        payload = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd0&s\x03\xf8\xff\xff\x00`&s\x03\xf8\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\xd0O|m\x03\xf8\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00'
        mof = build_mof(EventTraceGroup.EVENT_TRACE_GROUP_THREAD, 3, 4, payload)
        self.assertIsInstance(mof, Thread_TypeGroup1),
        self.assertEqual(mof.get_process_id(), 0)
        self.assertEqual(mof.get_thread_id(), 0)