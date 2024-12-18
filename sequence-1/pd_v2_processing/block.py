import logging
import xgboost as xgb
import joblib
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

def __main__(pti : float,score_results : int,BALMAG01 : int,revolving_amount_monthly_payment : int,closed_with_balance_amount_current_balance : int,AT31S : int,AT20S : int,BC21S : int,record_counts_revolving_trade_count : int,record_counts_total_trade_count : int,PAYMNT10 : int,AGG102 : int,total_amount_high_credit : int,revolving_amount_current_balance : int,total_amount_current_balance : int,REV83 : int,revolving_amount_high_credit : int,closed_with_balance_amount_monthly_payment : int,revolving_amount_percent_available_credit : int,AGG101 : int,revolving_amount_credit_limit : int,AT09S : int,US01S : int)->dict:

    input_data = {
        "pti": pti, "score_results": score_results, "BALMAG01": BALMAG01,
        "revolving_amount_monthly_payment": revolving_amount_monthly_payment,
        "closed_with_balance_amount_current_balance": closed_with_balance_amount_current_balance,
        "AT31S": AT31S, "AT20S": AT20S, "BC21S": BC21S,
        "record_counts_revolving_trade_count": record_counts_revolving_trade_count,
        "record_counts_total_trade_count": record_counts_total_trade_count, "PAYMNT10": PAYMNT10,
        "AGG102": AGG102, "total_amount_high_credit": total_amount_high_credit,
        "revolving_amount_current_balance": revolving_amount_current_balance,
        "total_amount_current_balance": total_amount_current_balance, "REV83": REV83,
        "revolving_amount_high_credit": revolving_amount_high_credit,
        "closed_with_balance_amount_monthly_payment": closed_with_balance_amount_monthly_payment,
        "revolving_amount_percent_available_credit": revolving_amount_percent_available_credit,
        "AGG101": AGG101, "revolving_amount_credit_limit": revolving_amount_credit_limit,
        "AT09S": AT09S, "US01S": US01S, "has_mortgage": None
    }

    # Load model
    try:
        # model = joblib.load("./xgboost_model.joblib") 
        model = joblib.load("C:/Users/cbollu/Downloads/test_blocks/test_blocks/sequence-1/pd_v2_processing/xgboost_model.joblib") 
    except Exception as e:
        logger.exception("An unexpected error occurred while loading the model.")
        raise e
    df_pre_processed = pd.DataFrame(input_data, index=[0])

    if df_pre_processed.empty:
        print("PD V2 Pre Processed DataFrame is empty.")

    expected_features = model.feature_names
    actual_features = df_pre_processed.columns.tolist()
    missing_features = [feature for feature in expected_features if feature not in actual_features]
    
    # Add missing features as None (NaN) values
    for feature in missing_features:
        df_pre_processed[feature] = None

    # Convert object columns to categorical
    for col in df_pre_processed.columns:
        if df_pre_processed[col].dtype == 'object':
            df_pre_processed[col] = pd.Categorical(df_pre_processed[col])

    # Prepare data for prediction
    dmatrix = xgb.DMatrix(df_pre_processed[expected_features], enable_categorical=True)
    
    # Make prediction
    prediction = model.predict(dmatrix)[0]

    return {"probability": prediction}