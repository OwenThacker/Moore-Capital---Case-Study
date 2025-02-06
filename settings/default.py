import os

CPD_LBWS = [10, 21, 63, 126, 256]
CPD_DEFAULT_LBW = 21
BACKTEST_AVERAGE_BASIS_POINTS = [None, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
USE_KM_HYP_TO_INITIALISE_KC = True

CPD_QUANDL_OUTPUT_FOLDER = lambda lbw: os.path.join(
    "data", f"quandl_cpd_{(lbw if lbw else 'none')}lbw"
)

CPD_QUANDL_OUTPUT_FOLDER_DEFAULT = CPD_QUANDL_OUTPUT_FOLDER(CPD_DEFAULT_LBW)

FEATURES_QUANDL_FILE_PATH = lambda lbw: os.path.join(
    "data", f"quandl_cpd_{(lbw if lbw else 'none')}lbw.csv"
)

FEATURES_QUANDL_FILE_PATH_DEFAULT = FEATURES_QUANDL_FILE_PATH(CPD_DEFAULT_LBW)

QUANDL_TICKERS = ['ABN NA Equity', 'ACA FP Equity', 'AIBG ID Equity', 'AZA SS Equity',
       'BAMI IM Equity', 'BARC LN Equity', 'BBVA SQ Equity', 'BCP PL Equity',
       'BCVN SE Equity', 'BG AV Equity', 'BGN IM Equity', 'BIRG ID Equity',
       'BKT SQ Equity', 'BMPS IM Equity', 'BNP FP Equity', 'BPE IM Equity',
       'BPSO IM Equity', 'CABK SQ Equity', 'CBK GY Equity', 'CMBN SE Equity',
       'DANSKE DC Equity', 'DBK GY Equity', 'DNB NO Equity', 'EBS AV Equity',
       'FBK IM Equity', 'GLE FP Equity', 'HSBA LN Equity', 'INGA NA Equity',
       'INVP LN Equity', 'ISP IM Equity', 'JYSK DC Equity', 'KBC BB Equity',
       'LLOY LN Equity', 'NDA FH Equity', 'NWG LN Equity', 'PEO PW Equity',
       'PKO PW Equity', 'RBI AV Equity', 'RILBA DC Equity', 'SAB SQ Equity',
       'SAN SQ Equity', 'SB1NO NO Equity', 'SEBA SS Equity', 'SHBA SS Equity',
       'SPL PW Equity', 'STAN LN Equity', 'SWEDA SS Equity', 'SYDB DC Equity',
       'UCG IM Equity'
]

ALL_QUANDL_CODES = ['ABN NA Equity', 'ACA FP Equity', 'AIBG ID Equity', 'AZA SS Equity',
       'BAMI IM Equity', 'BARC LN Equity', 'BBVA SQ Equity', 'BCP PL Equity',
       'BCVN SE Equity', 'BG AV Equity', 'BGN IM Equity', 'BIRG ID Equity',
       'BKT SQ Equity', 'BMPS IM Equity', 'BNP FP Equity', 'BPE IM Equity',
       'BPSO IM Equity', 'CABK SQ Equity', 'CBK GY Equity', 'CMBN SE Equity',
       'DANSKE DC Equity', 'DBK GY Equity', 'DNB NO Equity', 'EBS AV Equity',
       'FBK IM Equity', 'GLE FP Equity', 'HSBA LN Equity', 'INGA NA Equity',
       'INVP LN Equity', 'ISP IM Equity', 'JYSK DC Equity', 'KBC BB Equity',
       'LLOY LN Equity', 'NDA FH Equity', 'NWG LN Equity', 'PEO PW Equity',
       'PKO PW Equity', 'RBI AV Equity', 'RILBA DC Equity', 'SAB SQ Equity',
       'SAN SQ Equity', 'SB1NO NO Equity', 'SEBA SS Equity', 'SHBA SS Equity',
       'SPL PW Equity', 'STAN LN Equity', 'SWEDA SS Equity', 'SYDB DC Equity',
       'UCG IM Equity'
]

COMMODITIES_TICKERS = ['ABN NA Equity', 'ACA FP Equity', 'AIBG ID Equity', 'AZA SS Equity',
       'BAMI IM Equity', 'BARC LN Equity', 'BBVA SQ Equity', 'BCP PL Equity',
       'BCVN SE Equity', 'BG AV Equity', 'BGN IM Equity', 'BIRG ID Equity',
       'BKT SQ Equity', 'BMPS IM Equity', 'BNP FP Equity', 'BPE IM Equity',
       'BPSO IM Equity', 'CABK SQ Equity', 'CBK GY Equity', 'CMBN SE Equity',
       'DANSKE DC Equity', 'DBK GY Equity', 'DNB NO Equity', 'EBS AV Equity',
       'FBK IM Equity', 'GLE FP Equity', 'HSBA LN Equity', 'INGA NA Equity',
       'INVP LN Equity', 'ISP IM Equity', 'JYSK DC Equity', 'KBC BB Equity',
       'LLOY LN Equity', 'NDA FH Equity', 'NWG LN Equity', 'PEO PW Equity',
       'PKO PW Equity', 'RBI AV Equity', 'RILBA DC Equity', 'SAB SQ Equity',
       'SAN SQ Equity', 'SB1NO NO Equity', 'SEBA SS Equity', 'SHBA SS Equity',
       'SPL PW Equity', 'STAN LN Equity', 'SWEDA SS Equity', 'SYDB DC Equity',
       'UCG IM Equity'
]

OTHER_TICKERS = ['ABN NA Equity', 'ACA FP Equity', 'AIBG ID Equity', 'AZA SS Equity',
       'BAMI IM Equity', 'BARC LN Equity', 'BBVA SQ Equity', 'BCP PL Equity',
       'BCVN SE Equity', 'BG AV Equity', 'BGN IM Equity', 'BIRG ID Equity',
       'BKT SQ Equity', 'BMPS IM Equity', 'BNP FP Equity', 'BPE IM Equity',
       'BPSO IM Equity', 'CABK SQ Equity', 'CBK GY Equity', 'CMBN SE Equity',
       'DANSKE DC Equity', 'DBK GY Equity', 'DNB NO Equity', 'EBS AV Equity',
       'FBK IM Equity', 'GLE FP Equity', 'HSBA LN Equity', 'INGA NA Equity',
       'INVP LN Equity', 'ISP IM Equity', 'JYSK DC Equity', 'KBC BB Equity',
       'LLOY LN Equity', 'NDA FH Equity', 'NWG LN Equity', 'PEO PW Equity',
       'PKO PW Equity', 'RBI AV Equity', 'RILBA DC Equity', 'SAB SQ Equity',
       'SAN SQ Equity', 'SB1NO NO Equity', 'SEBA SS Equity', 'SHBA SS Equity',
       'SPL PW Equity', 'STAN LN Equity', 'SWEDA SS Equity', 'SYDB DC Equity',
       'UCG IM Equity'
]

# TODO get rid of the ones not used get
PINNACLE_ASSET_CLASS_MAPPING = {'ABN NA Equity', 'ACA FP Equity', 'AIBG ID Equity', 'AZA SS Equity',
       'BAMI IM Equity', 'BARC LN Equity', 'BBVA SQ Equity', 'BCP PL Equity',
       'BCVN SE Equity', 'BG AV Equity', 'BGN IM Equity', 'BIRG ID Equity',
       'BKT SQ Equity', 'BMPS IM Equity', 'BNP FP Equity', 'BPE IM Equity',
       'BPSO IM Equity', 'CABK SQ Equity', 'CBK GY Equity', 'CMBN SE Equity',
       'DANSKE DC Equity', 'DBK GY Equity', 'DNB NO Equity', 'EBS AV Equity',
       'FBK IM Equity', 'GLE FP Equity', 'HSBA LN Equity', 'INGA NA Equity',
       'INVP LN Equity', 'ISP IM Equity', 'JYSK DC Equity', 'KBC BB Equity',
       'LLOY LN Equity', 'NDA FH Equity', 'NWG LN Equity', 'PEO PW Equity',
       'PKO PW Equity', 'RBI AV Equity', 'RILBA DC Equity', 'SAB SQ Equity',
       'SAN SQ Equity', 'SB1NO NO Equity', 'SEBA SS Equity', 'SHBA SS Equity',
       'SPL PW Equity', 'STAN LN Equity', 'SWEDA SS Equity', 'SYDB DC Equity',
       'UCG IM Equity'
}
