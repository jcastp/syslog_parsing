import unittest
import libparser

class ParserTest(unittest.TestCase):

    def test_check_time(self):
        final_date = libparser.time_convert("Feb 16 17:02:26")
        self.assertEqual(final_date, "2015-02-16 17:02:26")
        return

    def test_clean_message(self):
        test1 = b'<14>Feb 16 17:02:30 hefaistos jcastp: test3'
        expected_result_1 = 'Feb 16 17:02:30 hefaistos jcastp: test3'
        self.assertEqual(libparser.clean_message(test1), expected_result_1)
        test2 = b'<86>Feb 16 17:09:01 hefaistos CRON[13579]: pam_unix(cron:session): session opened for user root by (uid=0)'
        expected_result_2 = 'Feb 16 17:09:01 hefaistos CRON[13579]: pam_unix(cron:session): session opened for user root by (uid=0)'
        self.assertEqual(libparser.clean_message(test2), expected_result_2)
        return

    def test_classify_lines(self):
        syslog_line = 'Feb 16 17:02:30 hefaistos jcastp: test3'
        audit_line = 'type=DAEMON_END msg=audit(1423656756.999:2346): auditd normal halt, sending auid=4294967295 pid=-1 subj= res=success'
        self.assertEqual(libparser.classify_lines(syslog_line), "syslog")
        self.assertEqual(libparser.classify_lines(audit_line), "audit")
        return



if __name__ == "__main__":
    unittest.main()
