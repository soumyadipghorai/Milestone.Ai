from sqlalchemy.orm import Session
from models.db_models import *
from models.database import get_db
import logging
from datetime import datetime
import pandas as pd 

db = get_db()

def add_entry(success_key: str, success_value, entry) :  
    db.add(entry)
    db.commit()
    return {"message" : "success", success_key : success_value} 

def insert_into_language_guidelines() -> dict: 
    df = pd.read_csv('database/language_guideline.csv')
    for i in range(len(df)) : 
        db_entry = LanguageGuidelines(
            name = df['name'].iloc[i], guideline = df['guideline'].iloc[i]
        )
        db.add(db_entry)
        db.commit()

