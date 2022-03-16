from icecream import ic
from context.domains import Dataset
from context.models import Model


class TitanicModel:
    model = Model()
    dataset = Dataset()

    def __init__(self, train_fname, test_fname):
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출

    def preprocess(self):
        df = self.train
        ic(f'트레인 컬럼 {df.columns}')
        ic(f'트레인 헤드 {df.head()}')
        ic(df)
        ic(type(df))
        df = self.drop_feature(df)
        df = self.name_nominal(df)
        df = self.pclass_ordinal(df)
        df = self.sex_nominal(df)
        df = self.age_ratio(df)
        df = self.embarked_nominal(df)
        df = self.create_label(df)
        df = self.create_train(df)
        return df

    @staticmethod
    def create_label(df) -> object:
        return df

    @staticmethod
    def create_train(df) -> object:
        return df

    def drop_feature(self, df) -> object:

        '''
        self.sibSp_nominal_garbage(df)
        self.parch_nominal_garbage(df)
        self.ticket_ordinal_garbage(df)
        self.fare_ratio_garbage(df)
        self.cabin_ordinal_garbage(df)
        '''
        return df

    '''
    Categorical vs Quantitative -> 구간의 유무
    Cate -> nominal (이름) vs ordinal (순서)
    Quan -> interval (상대적) vs ratio (절대적)
    '''

    @staticmethod
    def pclass_ordinal(df) -> object:
        return df

    @staticmethod
    def name_nominal(df) -> object:
        return df

    @staticmethod
    def sex_nominal(df) -> object:
        return df

    @staticmethod
    def age_ratio(df) -> object:
        return df

    @staticmethod
    def sibSp_nominal_garbage(df) -> object:
        return df

    @staticmethod
    def parch_nominal_garbage(df) -> object:
        return df

    @staticmethod
    def ticket_ordinal_garbage(df) -> object:
        return df

    @staticmethod
    def fare_ratio_garbage(df) -> object:
        return df

    @staticmethod
    def cabin_ordinal_garbage(df) -> object:
        return df

    @staticmethod
    def embarked_nominal(df) -> object:
        return df
