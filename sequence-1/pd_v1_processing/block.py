import logging
import h2o

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)


def __main__(pti:float, score_results:int, revolving_amount_monthly_payment:int, AT31S:int, total_amount_high_credit:int, AT20S:int, BALMAG01:int, record_counts_revolving_trade_count:int, PAYMNT10:int, closed_with_balance_amount_current_balance:int, REV83:int, AGG102:int, BC21S:int, record_counts_total_trade_count:int, revolving_amount_current_balance:int, total_amount_current_balance:int, revolving_amount_high_credit:int, US01S:int, AGG101:int, closed_with_balance_amount_monthly_payment:int, revolving_amount_credit_limit:int, revolving_amount_percent_available_credit:int, AT09S:int)->dict:
    input_data = {
        "pti": pti, "score_results": score_results, "revolving_amount_monthly_payment": revolving_amount_monthly_payment,
        "AT31S": AT31S, "total_amount_high_credit": total_amount_high_credit, "AT20S": AT20S, "BALMAG01": BALMAG01,
        "record_counts_revolving_trade_count": record_counts_revolving_trade_count, "PAYMNT10": PAYMNT10,
        "closed_with_balance_amount_current_balance": closed_with_balance_amount_current_balance, "REV83": REV83,
        "AGG102": AGG102, "BC21S": BC21S, "record_counts_total_trade_count": record_counts_total_trade_count,
        "revolving_amount_current_balance": revolving_amount_current_balance, "total_amount_current_balance": total_amount_current_balance,
        "revolving_amount_high_credit": revolving_amount_high_credit, "US01S": US01S, "AGG101": AGG101,
        "closed_with_balance_amount_monthly_payment": closed_with_balance_amount_monthly_payment,
        "revolving_amount_credit_limit": revolving_amount_credit_limit, "revolving_amount_percent_available_credit": revolving_amount_percent_available_credit,
        "AT09S": AT09S
    }

    h2o.init(max_mem_size="16G")
    try:
        if h2o.cluster().is_running():
            print("H2o running successfully.")
            model_pd_v1 = h2o.load_model("C:/Users/cbollu/Downloads/test_blocks/test_blocks/sequence-1/pd_v1_processing/trees_300_depth_2_min_rows_0.03_count_0")
            expected_features = model_pd_v1.columns
            for feature in expected_features:
                if feature not in input_data:
                    input_data[feature] = None
            input_list = [input_data.get(feature, None) for feature in expected_features]
            row_h2o = h2o.H2OFrame([input_list], column_names=expected_features)

            prediction = model_pd_v1.predict(row_h2o)
            predictions_df = prediction.as_data_frame()
            return {'probability': predictions_df['p1'].iloc[0]}

    except Exception as error:
            print(f"Error while predicting: {error}")
            return {'error': str(error)}
    finally:
            h2o.cluster().shutdown()