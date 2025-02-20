import pandas as pd
from faker import Faker
from cryptography.fernet import Fernet
import hashlib

class ClinicalAnonymizer:
    def __init__(self, config):
        self.faker = Faker()
        self.key = Fernet.generate_key()
        self.rules = config
        
    def pseudonymize(self, df):
        """GDPR-compliant pseudonymization"""
        # Direct identifiers
        df['patient_id'] = df['patient_id'].apply(
            lambda x: hashlib.sha256(x.encode() + self.key).hexdigest()
        )
        
        # Quasi-identifiers
        if 'birth_date' in df:
            df['birth_year'] = df['birth_date'].dt.year
            del df['birth_date']
            
        # Sensitive data encryption
        if 'diagnosis' in df:
            fernet = Fernet(self.key)
            df['diagnosis'] = df['diagnosis'].apply(
                lambda x: fernet.encrypt(x.encode())
            )
            
        return df
    
    def risk_assessment(self, df):
        """Calculate re-identification risk"""
        quasi_identifiers = self.rules['quasi_identifiers']
        return df.groupby(quasi_identifiers).size().reset_index(name='count')
