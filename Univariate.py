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

    def freqTable(columnName,data):
        freqTable = pd.DataFrame(columns['Unique_values','Frequency','Relative_Frequency','CumSum'])
        freqTable['Unique_values']=data['ssc_p'].value_counts().index
        freqTable['Frequency']=data['ssc_p'].value_counts().values
        freqTable['Relative_Frequency']=(freqTable['Frequency']/103)
        freqTable['CumSum']=freqTable['Relative_Frequency'].cumsum()
        return freqTable
        
    def Univariate(data,quan):
        descriptive = pd.DataFrame(index=['mean','median','mode','Q1:25%','Q2:50%','Q3:75%','99%',
                                          'Q4:100%','IQR','1.5rule','Lesser','Greater','Min','Max','Variance','Std_Deviation'],columns=quan)
        for columnName in quan:
            descriptive[columnName]['mean']=data[columnName].mean()
            descriptive[columnName]['median']=data[columnName].median()
            descriptive[columnName]['mode']=data[columnName].mode()[0]
            descriptive[columnName]['Q1:25%']=data.describe()[columnName]['25%']
            descriptive[columnName]['Q2:50%']=data.describe()[columnName]['50%']
            descriptive[columnName]['Q3:75%']=data.describe()[columnName]['75%']
            descriptive[columnName]['99%']=np.percentile(data[columnName],99)
            descriptive[columnName]['Q4:100%']=data.describe()[columnName]['max']
            descriptive[columnName]['IQR']=descriptive[columnName]['Q3:75%']-descriptive[columnName]['Q1:25%']
            descriptive[columnName]['1.5rule']=1.5*descriptive[columnName]['IQR']
            descriptive[columnName]['Lesser']=descriptive[columnName]['Q1:25%']-descriptive[columnName]['1.5rule']
            descriptive[columnName]['Greater']=descriptive[columnName]['Q3:75%']+descriptive[columnName]['1.5rule']
            descriptive[columnName]['Min']=data[columnName].min()
            descriptive[columnName]['Max']=data[columnName].max()
            descriptive[columnName]['Variance']=data[columnName].var()
            descriptive[columnName]['Std_Deviation']=data[columnName].std()
        return descriptive