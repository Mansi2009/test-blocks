import logging
import math

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

def __main__(record_counts_revolving_trade_count:int,record_counts_total_trade_count:int,score_results:int,total_amount_high_credit:int,revolving_amount_credit_limit:int,revolving_amount_percent_available_credit:int,revolving_amount_current_balance:int,revolving_amount_monthly_payment:int,revolving_amount_high_credit:int,closed_with_balance_amount_current_balance:int,closed_with_balance_amount_monthly_payment:int,AGG101:int,AGG102:int,AT09S:int,AT20S:int,AT31S:int,BALMAG01:int,BC21S:int,PAYMNT10:int,REV83:int,US01S:int,monthly_income:float,internal_monthly_payment:float,installment_amount_monthly_payment:int,open_amount_current_balance:int,installment_amount_current_balance:int)->dict:
    #record_counts_revolving_trade_count treatment
    if record_counts_revolving_trade_count is None or math.isnan(record_counts_revolving_trade_count): 
        record_counts_revolving_trade_count = None
    elif 0 <= record_counts_revolving_trade_count <= 999:
        record_counts_revolving_trade_count = min(30, max(0, record_counts_revolving_trade_count))
    else:
        record_counts_revolving_trade_count = None

    #record_counts_total_trade_count treatment
    if record_counts_total_trade_count is None or math.isnan(record_counts_total_trade_count):
        record_counts_total_trade_count = None
    elif 0 <= record_counts_total_trade_count <= 999:
        record_counts_total_trade_count = min(35, max(0, record_counts_total_trade_count))
    else:
        record_counts_total_trade_count = None

    #score_results treatment
    if score_results is None or math.isnan(score_results):
        score_results = None
    elif 350.0 <= score_results <= 850.0:
        score_results = min(850.0, max(350.0, score_results))
    else:
        score_results = None

    #revolving_amount_credit_limit treatment
    if revolving_amount_credit_limit is None or math.isnan(revolving_amount_credit_limit): 
        revolving_amount_credit_limit = None
    elif 0.0 <= revolving_amount_credit_limit <= 999999999.0:
        revolving_amount_credit_limit = min(20000.0, max(0.0, revolving_amount_credit_limit))
    else:
        revolving_amount_credit_limit = None

    #revolving_amount_percent_available_credit treatment
    if revolving_amount_percent_available_credit is None or math.isnan(revolving_amount_percent_available_credit):
        revolving_amount_percent_available_credit = None
    elif 0.0 <= revolving_amount_percent_available_credit <= 100.0:
        revolving_amount_percent_available_credit = min(100.0, max(0.0, revolving_amount_percent_available_credit))
    else:
        revolving_amount_percent_available_credit = None

    #total_amount_monthly_payment
    if (revolving_amount_monthly_payment is None or math.isnan(revolving_amount_monthly_payment)) and (installment_amount_monthly_payment is None or math.isnan(installment_amount_monthly_payment)):
        total_amount_monthly_payment = None
    else:
        total_amount_monthly_payment = sum(value for value in [revolving_amount_monthly_payment, installment_amount_monthly_payment] if value is not None)


    #total_amount_current_balance
    # if (open_amount_current_balance in [None, ""] or pd.isna(open_amount_current_balance)) and (revolving_amount_current_balance in [None, ""] or pd.isna(revolving_amount_current_balance)) and (installment_amount_current_balance in [None, ""] or pd.isna(installment_amount_current_balance)):
    # if pd.isna(open_amount_current_balance) and pd.isna(revolving_amount_current_balance) and pd.isna(installment_amount_current_balance):
    #     total_amount_current_balance = None
    # else:
    #     total_amount_current_balance = sum(filter(pd.notna, [open_amount_current_balance, revolving_amount_current_balance, installment_amount_current_balance]))
    if (open_amount_current_balance is None or math.isnan(open_amount_current_balance)) and (revolving_amount_current_balance is None or math.isnan(revolving_amount_current_balance)) and (installment_amount_current_balance is None or math.isnan(installment_amount_current_balance)):
        total_amount_current_balance = None
    else:
        total_amount_current_balance = sum(value for value in [open_amount_current_balance, revolving_amount_current_balance, installment_amount_current_balance] if value is not None and value != "")


    #total_amount_current_balance treatment
    if total_amount_current_balance is None or math.isnan(total_amount_current_balance):
        total_amount_current_balance = None
    elif 0.0 <= total_amount_current_balance <= 999999999.0:
        total_amount_current_balance = min(120000.0, max(0.0, total_amount_current_balance))
    else:
        total_amount_current_balance = None

    #revolving_amount_current_balance treatment
    if revolving_amount_current_balance is None or math.isnan(revolving_amount_current_balance):
        revolving_amount_current_balance = None
    elif 0.0 <= revolving_amount_current_balance <= 999999999.0:
        revolving_amount_current_balance = min(20000.0, max(0.0, revolving_amount_current_balance))
    else:
        revolving_amount_current_balance = None

    #revolving_amount_monthly_payment treatment
    if revolving_amount_monthly_payment is None or math.isnan(revolving_amount_monthly_payment):
        revolving_amount_monthly_payment = None
    elif 0.0 <= revolving_amount_monthly_payment <= 999999999.0:
        revolving_amount_monthly_payment = min(500.0, max(0.0, revolving_amount_monthly_payment))
    else:
        revolving_amount_monthly_payment = None

    #revolving_amount_high_credit treatment
    if revolving_amount_high_credit is None or math.isnan(revolving_amount_high_credit):
        revolving_amount_high_credit = None
    elif 0.0 <= revolving_amount_high_credit <= 999999999.0:
        revolving_amount_high_credit = min(20000.0, max(0.0, revolving_amount_high_credit))
    else:
        revolving_amount_high_credit = None

    #AGG101 treatment
    if AGG101 is None or math.isnan(AGG101):
        AGG101 = None
    elif 0.0 <= AGG101 <= 999999999.0:
        AGG101 = min(40000.0, max(0.0, AGG101))
    else:
        AGG101 = 0.0

    #AGG102 treatment
    if AGG102 is None or math.isnan(AGG102):
        AGG102 = None
    elif 0.0 <= AGG102 <= 999999999.0:
        AGG102= min(60000.0, max(0.0, AGG102))
    else:
        AGG102 = 0.0

    #AT09S treatment
    if AT09S is None or math.isnan(AT09S):
        AT09S = None
    elif 0 <= AT09S <= 999:
        AT09S = min(10, max(0, AT09S))
    else:
        AT09S = 0

    #AT20S treatment
    if AT20S is None or math.isnan(AT20S):
        AT20S = None
    elif 0 <= AT20S <= 999:
        AT20S = min(500, max(0, AT20S))
    else:
        AT20S = 0

    #AT31S treatment
    if AT31S is None or math.isnan(AT31S):
        AT31S = None
    elif 0 <= AT31S <= 999:
        AT31S = min(100, max(0, AT31S))
    else:
        AT31S = 0

    #BALMAG01 treatment
    if BALMAG01 is None or math.isnan(BALMAG01):
        BALMAG01 = None
    elif 0.0 <= BALMAG01 <= 600.0:
        BALMAG01 = min(500.0, max(0.0, BALMAG01))
    else:
        BALMAG01 = 500.0

    #BC21S treatment
    if BC21S is None or math.isnan(BC21S):
        BC21S = None
    elif 0 <= BC21S <= 999:
        BC21S = min(100, max(0, BC21S))
    else:
        BC21S = 100

    #PAYMNT10 treatment
    if PAYMNT10 is None or math.isnan(PAYMNT10): 
        PAYMNT10 = None
    elif 0.0 <= PAYMNT10 <= 999.0:
        PAYMNT10 = min(15.0, max(0.0, PAYMNT10))
    else:
        PAYMNT10 = 0.0

    #REV83 treatment
    if REV83 is None or math.isnan(REV83):
        REV83 = None
    elif 0.0 <= REV83 <= 999.0:
        REV83 = min(500.0, max(0.0, REV83))
    else:
        REV83 = 500.0

    #US01S treatment
    if US01S is None or math.isnan(US01S): 
        US01S = None
    elif 0 <= US01S <= 999:
        US01S = min(10, max(0, US01S))
    else:
        US01S = 10
    
    #internal_monthly_payment treatment
    if internal_monthly_payment is None or math.isnan(internal_monthly_payment): 
        internal_monthly_payment = 92.97

    #monthly_income treatment
    # if (monthly_income is not None and monthly_income != "") or pd.isna(monthly_income) or pd.isnull(monthly_income):
    if 0.0 <= monthly_income <= 999999999.0:
            monthly_income = min(8500.0, max(0.0, monthly_income))
    else:
        monthly_income = None

    #pti calculation
    if (monthly_income not in [None, 0.0] and not math.isnan(monthly_income) and internal_monthly_payment not in [None, ""] and not math.isnan(internal_monthly_payment) and total_amount_monthly_payment not in [None, ""] and not math.isnan(total_amount_monthly_payment)):
        pti = (total_amount_monthly_payment + internal_monthly_payment) / monthly_income
    elif ((monthly_income != 0.0) and monthly_income not in [None, ""] and monthly_income != monthly_income) and (total_amount_monthly_payment not in [None, ""] and total_amount_monthly_payment != total_amount_monthly_payment):
        pti = (total_amount_monthly_payment + 92.97) / monthly_income
    else:
        pti = None

    #total_amount_high_credit treatment
    if total_amount_high_credit is None or math.isnan(total_amount_high_credit):
        total_amount_high_credit = None
    elif 0.0 <= total_amount_high_credit <= 999999999.0:
        total_amount_high_credit = min(150000.0, max(0.0, total_amount_high_credit))
    else:
        total_amount_high_credit = None

    #closed_with_balance_amount_current_balance treatment
    if closed_with_balance_amount_current_balance is None or math.isnan(closed_with_balance_amount_current_balance):
        closed_with_balance_amount_current_balance = None
    elif 0.0 <= closed_with_balance_amount_current_balance <= 999999999.0:
        closed_with_balance_amount_current_balance = min(15000.0, max(0.0, closed_with_balance_amount_current_balance))
    else:
        closed_with_balance_amount_current_balance = None

    #closed_with_balance_amount_monthly_payment treatment
    if closed_with_balance_amount_monthly_payment is None or math.isnan(closed_with_balance_amount_monthly_payment):
        closed_with_balance_amount_monthly_payment = None
    elif 0.0 <= closed_with_balance_amount_monthly_payment <= 999999999.0:
        closed_with_balance_amount_monthly_payment = min(300.0, max(0.0, closed_with_balance_amount_monthly_payment))
    else:
        closed_with_balance_amount_monthly_payment = None

    return {"pti" : pti,"score_results" : score_results,"BALMAG01" : BALMAG01,"revolving_amount_monthly_payment" : revolving_amount_monthly_payment,
            "closed_with_balance_amount_current_balance" : closed_with_balance_amount_current_balance,"AT31S" : AT31S,"AT20S" : AT20S,
            "BC21S" : BC21S,"record_counts_revolving_trade_count" : record_counts_revolving_trade_count,"record_counts_total_trade_count" : record_counts_total_trade_count,
            "PAYMNT10" : PAYMNT10,"AGG102" : AGG102,"total_amount_high_credit" : total_amount_high_credit,"revolving_amount_current_balance" : revolving_amount_current_balance,
            "total_amount_current_balance" : total_amount_current_balance,"REV83" : REV83,"revolving_amount_high_credit" : revolving_amount_high_credit,
            "closed_with_balance_amount_monthly_payment" : closed_with_balance_amount_monthly_payment,"revolving_amount_percent_available_credit" : revolving_amount_percent_available_credit,
            "AGG101" : AGG101,"revolving_amount_credit_limit" : revolving_amount_credit_limit,"AT09S" : AT09S,"US01S" : US01S}