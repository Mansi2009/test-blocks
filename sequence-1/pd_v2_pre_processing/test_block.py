import unittest
from block import __main__

class TestBlock(unittest.TestCase):

    def test_main_success(self):
        result = __main__(record_counts_revolving_trade_count= 9,record_counts_total_trade_count= 18,score_results= 600,total_amount_high_credit= 53807,revolving_amount_credit_limit= 2000,revolving_amount_percent_available_credit= 18,revolving_amount_current_balance= 1635,revolving_amount_monthly_payment= 56,revolving_amount_high_credit= 1720,closed_with_balance_amount_current_balance= 8411,closed_with_balance_amount_monthly_payment= 0,AGG101= 11043,AGG102= 24994,AT09S= 4,AT20S= 166,AT31S= 71,BALMAG01= 196,BC21S= 4,PAYMNT10= 4,REV83= 0,US01S= 0,open_amount_current_balance= None,installment_amount_current_balance= 36718,monthly_income= 2200.00,internal_monthly_payment=  None,installment_amount_monthly_payment= 572)
        
        expected_result = {"pti": 0.3277136364,"score_results": 600.0,"BALMAG01": 196.0,"revolving_amount_monthly_payment": 56.0,"closed_with_balance_amount_current_balance": 8411.0,"AT31S": 71.0,"AT20S": 166.0,"BC21S": 4.0,"record_counts_revolving_trade_count": 9.0,"record_counts_total_trade_count": 18.0,"PAYMNT10": 4.0,"AGG102": 24994.0,"total_amount_high_credit": 53807.0,"revolving_amount_current_balance": 1635.0,"total_amount_current_balance": 38353.0,"REV83": 0.0,"revolving_amount_high_credit": 1720.0,"closed_with_balance_amount_monthly_payment": 0.0,"revolving_amount_percent_available_credit": 18.0,"AGG101": 11043.0,"revolving_amount_credit_limit": 2000.0,"AT09S": 4.0,"US01S": 0.0}
        for key, expected_value in expected_result.items():
            if isinstance(expected_value, float):
                self.assertAlmostEqual(result[key], expected_value, places=6, msg=f"Mismatch for {key}")
            else:
                self.assertEqual(result[key], expected_value, msg=f"Mismatch for {key}")


    def test_main_invalid_input(self):
        with self.assertRaises(TypeError):
            __main__(record_counts_revolving_trade_count= 9,record_counts_total_trade_count= 18,score_results= 600,total_amount_high_credit= 53807,revolving_amount_credit_limit= 2000,revolving_amount_percent_available_credit= 18,revolving_amount_current_balance= 1635,revolving_amount_monthly_payment= 56,revolving_amount_high_credit= 1720,closed_with_balance_amount_current_balance= 8411,closed_with_balance_amount_monthly_payment= 0,AGG101= 11043,AGG102= 24994,AT09S= 4,AT20S= 166,AT31S= 71,BALMAG01= 196,BC21S= 4,PAYMNT10= 4,REV83= 0,US01S= 0,open_amount_current_balance= None,installment_amount_current_balance= 36718,monthly_income= "2200.00",internal_monthly_payment=  None,installment_amount_monthly_payment= 572)  # Invalid input type (string)

if __name__ == "__main__":
    unittest.main()
