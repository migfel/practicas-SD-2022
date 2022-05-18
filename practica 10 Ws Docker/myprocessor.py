class MyProcessor:     
    def run(self, df):        
        return df.agg(['mean', 'min', 'max'])