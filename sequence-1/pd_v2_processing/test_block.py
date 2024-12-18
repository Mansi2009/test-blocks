import unittest
from block import __main__

class TestBlock(unittest.TestCase):

    def test_main_success(self):
        result = __main__(pti= 0.3277136364,score_results= 600.0,BALMAG01= 196.0,revolving_amount_monthly_payment= 56.0,closed_with_balance_amount_current_balance= 8411.0,AT31S= 71.0,AT20S= 166.0,BC21S= 4.0,record_counts_revolving_trade_count= 9.0,record_counts_total_trade_count= 18.0,PAYMNT10= 4.0,AGG102= 24994.0,total_amount_high_credit= 53807.0,revolving_amount_current_balance= 1635.0,total_amount_current_balance= 38353.0,REV83= 0.0,revolving_amount_high_credit= 1720.0,closed_with_balance_amount_monthly_payment= 0.0,revolving_amount_percent_available_credit= 18.0,AGG101= 11043.0,revolving_amount_credit_limit= 2000.0,AT09S= 4.0,US01S= 0.0)
        self.assertAlmostEqual(result['probability'], 0.33663413, places=7)

    # def test_main_invalid_input(self):
    #     with self.assertRaises(TypeError):
    #         __main__(pti= 231,score_results= 600.0,BALMAG01= 196.0,revolving_amount_monthly_payment= 56.0,closed_with_balance_amount_current_balance= 8411.0,AT31S= 71.0,AT20S= 166.0,BC21S= 4.0,record_counts_revolving_trade_count= 9.0,record_counts_total_trade_count= 18.0,PAYMNT10= 4.0,AGG102= 24994.0,total_amount_high_credit= 53807.0,revolving_amount_current_balance= 1635.0,total_amount_current_balance= 38353.0,REV83= 0.0,revolving_amount_high_credit= 1720.0,closed_with_balance_amount_monthly_payment= 0.0,revolving_amount_percent_available_credit= 18.0,AGG101= 11043.0,revolving_amount_credit_limit= 2000.0,AT09S= 4.0,US01S= 0.0)

if __name__ == "__main__":
    unittest.main()
