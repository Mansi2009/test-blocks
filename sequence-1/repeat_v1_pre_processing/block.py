import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

def __main__(record_counts_negative_trade_count:int, record_counts_installment_trade_count:int, 
             record_counts_total_trade_count:int, record_counts_total_inquiry_count:int, record_counts_revolving_trade_count:int, 
             score_results:float, installment_amount_monthly_payment:float, revolving_amount_percent_available_credit:float, G069S:int, 
             AT24S:int, BR02S:int, BI02S:int, AGG103:float, ALL231:float, AT12S:int, IN20S:int, AT33A:int, AT35A:int, AT28A:int, AT34B:int, 
             S061S:int, RE102S:int)->dict:

    #record_counts_negative_trade_count treatment
    if record_counts_negative_trade_count is None or math.isnan(record_counts_negative_trade_count):
        record_counts_negative_trade_count = 8
    elif 0 <= record_counts_negative_trade_count <= 999:
        record_counts_negative_trade_count = min(8, max(0, record_counts_negative_trade_count))
    else:
        record_counts_negative_trade_count = None

    #record_counts_installment_trade_count treatment
    if record_counts_installment_trade_count is None or math.isnan(record_counts_installment_trade_count):
        record_counts_installment_trade_count = 20
    elif 0 <= record_counts_installment_trade_count <= 999:
        record_counts_installment_trade_count = min(20, max(0, record_counts_installment_trade_count))
    else:
        record_counts_installment_trade_count = None

    #record_counts_total_trade_count treatment
    if record_counts_total_trade_count is None or math.isnan(record_counts_total_trade_count):
        record_counts_total_trade_count = 35
    elif 0 <= record_counts_total_trade_count <= 999:
        record_counts_total_trade_count = min(35, max(0, record_counts_total_trade_count))
    else:
        record_counts_total_trade_count = None

    #record_counts_total_inquiry_count treatment
    if record_counts_total_inquiry_count is None or math.isnan(record_counts_total_inquiry_count):
        record_counts_total_inquiry_count = 30
    elif 0 <= record_counts_total_inquiry_count <= 999:
        record_counts_total_inquiry_count = min(30, max(0, record_counts_total_inquiry_count))
    else:
        record_counts_total_inquiry_count = None

    #record_counts_revolving_trade_count treatment
    if record_counts_revolving_trade_count is None or math.isnan(record_counts_revolving_trade_count):
        record_counts_revolving_trade_count = 15
    elif 0 <= record_counts_revolving_trade_count <= 999:
        record_counts_revolving_trade_count = min(15, max(0, record_counts_revolving_trade_count))
    else:
        record_counts_revolving_trade_count = None

    #score_results treatment
    if score_results is None or math.isnan(score_results):
        score_results = 541.0
    elif 350.0 <= score_results <= 850.0:
        score_results = min(700.0, max(541.0, score_results))
    else:
        score_results = None

    #installment_amount_monthly_payment treatment
    if installment_amount_monthly_payment is None or math.isnan(installment_amount_monthly_payment):
        installment_amount_monthly_payment = 456.8794643
    elif 0.0 <= installment_amount_monthly_payment <= 999999999.0:
        installment_amount_monthly_payment = min(1500.0, max(0.0, installment_amount_monthly_payment))
    else:
        installment_amount_monthly_payment = None

    #revolving_amount_percent_available_credit treatment
    if revolving_amount_percent_available_credit is None or math.isnan(revolving_amount_percent_available_credit):
        revolving_amount_percent_available_credit = 100.0
    elif 0.0 <= revolving_amount_percent_available_credit <= 100.0:
        revolving_amount_percent_available_credit = min(100.0, max(0.0, revolving_amount_percent_available_credit))
    else:
        revolving_amount_percent_available_credit = None

    #G069S treatment
    if G069S is None or math.isnan(G069S):
        G069S = 0
    elif 0 <= G069S <= 999:
        G069S = min(6, max(0, G069S))
    else:
        G069S = 0

    #AT24S treatment
    if AT24S is None or math.isnan(AT24S):
        AT24S = 0
    elif 0 <= AT24S <= 999:
        AT24S = min(20, max(0, AT24S))
    else:
        AT24S = 0

    #BR02S treatment
    if BR02S is None or math.isnan(BR02S):
        BR02S = 0
    elif 0 <= BR02S <= 999:
        BR02S = min(5, max(0, BR02S))
    else:
        BR02S = 0

    #BI02S treatment
    if BI02S is None or math.isnan(BI02S):
        BI02S = 0
    elif 0 <= BI02S <= 999:
        BI02S = min(3, max(0, BI02S))
    else:
        BI02S = 0

    #AGG103 treatment
    if AGG103 is None or math.isnan(AGG103):
        AGG103 = 0.0
    elif 0.0 <= AGG103 <= 999999999.0:
        AGG103 = min(60000.0, max(0.0, AGG103))
    else:
        AGG103 = 0.0

    #ALL231 treatment
    if ALL231 is None or math.isnan(ALL231):
        ALL231 = 0.0
    elif 0.0 <= ALL231 <= 999999999.0:
        ALL231 = min(500.0, max(0.0, ALL231))
    else:
        ALL231 = 0.0

    #AT12S treatment
    if AT12S is None or math.isnan(AT12S):
        AT12S = 0
    elif 0 <= AT12S <= 999:
        AT12S = min(10, max(0, AT12S))
    else:
        AT12S = 0

    #IN20S treatment
    if IN20S is None or math.isnan(IN20S):
        IN20S = 0
    elif 0 <= IN20S <= 999:
        IN20S = min(150, max(0, IN20S))
    else:
        IN20S = 0

    #AT33A treatment
    if AT33A is None or math.isnan(AT33A):
        AT33A = 0
    elif 0 <= AT33A <= 999999999:
        AT33A = min(100000, max(0, AT33A))
    else:
        AT33A = 0

    #AT35A treatment
    if AT35A is None or math.isnan(AT35A):
        AT35A = 0
    elif 0 <= AT35A <= 999999999:
        AT35A = min(15000, max(0, AT35A))
    else:
        AT35A = 0

    #AT28A treatment
    if AT28A is None or math.isnan(AT28A):
        AT28A = 0
    elif 0 <= AT28A <= 999999999:
        AT28A = min(80000, max(0, AT28A))
    else:
        AT28A = 0

    #AT34B treatment
    if AT34B is None or math.isnan(AT34B):
        AT34B = 150
    elif 0 <= AT34B <= 999:
        AT34B = min(150, max(0, AT34B))
    else:
        AT34B = 0

    #S061S treatment
    if S061S is None or math.isnan(S061S):
        S061S = 40
    elif 0 <= S061S <= 84:
        S061S = min(40, max(0, S061S))
    else:
        S061S = 0

    #RE102S treatment
    if RE102S is None or math.isnan(RE102S):
        RE102S = 0
    elif 0 <= RE102S <= 999999999:
        RE102S = min(3000, max(0, RE102S))
    else:
        RE102S = 0

    return {
    "score_results" : score_results,
    "AT34B" : AT34B,
    "AT12S" : AT12S,
    "revolving_amount_percent_available_credit" : revolving_amount_percent_available_credit,
    "AT28A" : AT28A,
    "record_counts_total_trade_count" : record_counts_total_trade_count,
    "record_counts_negative_trade_count" : record_counts_negative_trade_count,
    "record_counts_revolving_trade_count" : record_counts_revolving_trade_count,
    "AT33A" : AT33A,
    "AT35A" : AT35A,
    "record_counts_total_inquiry_count" : record_counts_total_inquiry_count,
    "IN20S" : IN20S,
    "RE102S" : RE102S,
    "installment_amount_monthly_payment" : installment_amount_monthly_payment,
    "S061S" : S061S,
    "record_counts_installment_trade_count" : record_counts_installment_trade_count,
    "BR02S" : BR02S,
    "AGG103" : AGG103,
    "ALL231" : ALL231,
    "G069S" : G069S,
    "AT24S" : AT24S,
    "BI02S" : BI02S
}

