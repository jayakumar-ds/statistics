class Univariate():
    def qualQuan(data):
        qual = []
        quan = []
        
        for column in data.columns:
            if data[column].dtype == 'object'or data[column].dtype.name == 'category':
                qual.append(column)
            else:
                quan.append(column)
        return qual,quan    
   