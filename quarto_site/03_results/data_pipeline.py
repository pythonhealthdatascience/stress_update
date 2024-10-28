"""
Module: data_pipeline

Supporting and main functions used to read and clean/format of STRESS review dataset.
"""

import numpy as np
import pandas as pd

from typing import Optional

# Constants
REVIEW_CSV_FILE_PATH = "PY_STRESS.csv"
APP_FILTER_COLUMN_NAME = "used"
APP_FILTER_VALUE = "Yes"

def recode_whitespace(df: pd.DataFrame) -> pd.DataFrame:
    '''
    recode whitespace as "_" and strip head/tail whitespace just in case
    '''
    # strip leading and lagging white space
    df.columns = df.columns.str.strip()
    # replace remaining whitespace with "_"
    df.columns = df.columns.str.replace(" ", "_")
    return df

def strip_punctuation(df: pd.DataFrame) -> pd.DataFrame:
    '''
    strip select punction from column headers
    '''
    df.columns = df.columns.str.replace("?", "")
    df.columns = df.columns.str.replace("'", "")
    df.columns = df.columns.str.replace("-", "_")
    df.columns = df.columns.str.replace("/", "")
    return df

def cols_to_lower(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert all column names in a dataframe to lower case

    Params:
    ------
    df - pandas.DataFrame

    Returns:
    -------
    out: pandas.DataFrame
    """
    new_cols = [c.lower() for c in df.columns]
    df.columns = new_cols
    return df

def drop_non_english_language(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Check for "Not in English" recorded in any column
    Return all other rows.
    '''
    return df[~df.isin(['Not in English']).any(axis=1)]

#| code-fold: true
def load_review_dataset(
    path: Optional[str] = REVIEW_CSV_FILE_PATH,
) -> pd.DataFrame:
    """Read full data extraction data set for the review from a CSV file.
    Returns cleaned dataset.

    Assumes data is stored in .csv

    Cleaning pipeline for dataset:
    1. drop redunance columns
    2. drop rows that contain all NAs
    3. drop rows that are no in English
    3. rename columns with complex strings
    4. strip all punctuation from column headers
    5. column headers to lower case
    6. replace all whitespace in headers with "_"
    7. convert all blank strings in cells to NaN
    8. recode variables to be internally consistent in naming
    9. perform type conversion for integer fields
    10. type conversion for categorical fields
    

    Parameters:
    ----------
    path: str, optional (default=REVIEW_CSV_FILE_PATH)
        path or URL for review dataset.

    Returns:
    --------
    out: pd.DataFrame

    """

    # SETUP FOR DATASET CLEAN

    # cols to drop from data read in
    cols_to_remove = [
        "Unnamed: 0",
        "...27",
        "Questions to be asked from authors / experts",
        "Fatemeh's Note",
        "Note",
    ]

    # simple type conversions
    type_conversions = {"year": "UInt16"}

    # renaming of columns to names suitable for analysis
    new_labels = {
        "1. Objectives (purpose, model outputs, aims of experimentation)": "stress_objectives",
        "2. Logic (base model overview diagram, base model logic, scenario logic, algorithms, components)": "stress_logic",
        "3. Data (data sources, input parameters, preprocessing, assumptions": "stress_logic",
        "4. Experimentation (initialisation, run length, estimation approach)": "stress_exp",
        "5. Implementation (software and programming language, random sampling, model execution, system specification)": "stress_imp",
        "6. Code access (computer model sharing statement)": "stress_code",
    }

    # used to recode variables so they are consistent.
    recoded_variables = {"used": {"NO": "No"}}

    # DATA CLEANING PIPELINE
    clean = (
        pd.read_csv(path, index_col="No")
        # drop redundant index column
        .drop(labels=cols_to_remove, axis=1)
        # drop all blank rows (this will remove the blank 3 rows at end of CSV)
        .dropna(how="all")
        # drop all studies that do not use an English language
        .pipe(drop_non_english_language)
        # rename verbose column headers
        .rename(columns=new_labels)
        # remove any punctutation i.e. "?" and "-"
        .pipe(strip_punctuation)
        # all columns headers to lower case
        .pipe(cols_to_lower)
        # replace all whitespace with "_" in col headers
        .pipe(recode_whitespace)
        # replace all whitespace and blank strings in fields with NaN
        .replace(r"^\s*$", np.nan, regex=True)
        # recoded variables e.g. used "NO" becomes "No"
        .replace(recoded_variables)
        # update the type of columns to int where needed
        .astype(type_conversions)
        # categorical variables
        .assign(
            used=lambda x: pd.Categorical(x["used"]),
            type_of_paper=lambda x: pd.Categorical(x["type_of_paper"]),
            partially=lambda x: pd.Categorical(x["partially"]),
            method=lambda x: pd.Categorical(x["method"]),
            software=lambda x: pd.Categorical(x["software"]),
            source_code_access=lambda x: pd.Categorical(
                x["source_code_access"]
            ),
            application_area=lambda x: pd.Categorical(x["application_area"]),
            target_authors=lambda x: pd.Categorical(x["target_authors"]),
            stress_implementation=lambda x: pd.Categorical(
                x["stress_implementation"]
            ),
            hybridisation=lambda x: pd.Categorical(x["hybridisation"])
        )
    )
    return clean

def filter_to_application_studies(clean_df: pd.DataFrame) -> pd.DataFrame:
    """Filter the cleaned dataset down to studies that used stress to report
    a simulation study.

    Parameters:
    ----------
    clean_df: pd.DataFrame
        Review dataframe. The main assumption is that this has passed through
        the main cleaning pipeline

    Returns:
    -------
    out: pd.DataFrame
    """
    # Used?: a Yes/No variable.
    filtered_df = clean_df[clean_df[APP_FILTER_COLUMN_NAME] == APP_FILTER_VALUE]
    return filtered_df