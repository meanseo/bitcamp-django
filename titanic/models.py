from icecream import ic
from context.domains import Dataset
from context.models import Model


class TitanicModel:
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼 {self.train.columns}')
        ic(f'트레인 헤드 {self.train.head()}')
        ic(self.train)
        ic(type(self.train))

    def preprocess(self):
        self.fare_ratio_garbage()
        self.cabin_ordinal_garbage()
        self.parch_nominal_garbage()
        self.ticket_ordinal_garbage()
        self.sibSp_nominal_garbage()
        self.name_nominal()
        self.pclass_ordinal()
        self.sex_nominal()
        self.age_ratio()
        self.embarked_nominal()
        self.create_label()
        self.create_train()

    def create_label(self) -> object:
        pass

    def create_train(self) -> object:
        pass

    def drop_feature(self) -> object:
        pass

    '''
    Categorical vs Quantitative -> 구간의 유무
    Cate -> nominal (이름) vs ordinal (순서)
    Quan -> interval (상대적) vs ratio (절대적)
    '''
    def pclass_ordinal(self) -> object:
        pass

    def name_nominal(self) -> object:
        pass

    def sex_nominal(self) -> object:
        pass

    def age_ratio(self) -> object:
        pass

    def sibSp_nominal_garbage(self) -> object:
        self.drop_feature()

    def parch_nominal_garbage(self) -> object:
        self.drop_feature()

    def ticket_ordinal_garbage(self) -> object:
        self.drop_feature()

    def fare_ratio_garbage(self) -> object:
        self.drop_feature()

    def cabin_ordinal_garbage(self) -> object:
        self.drop_feature()

    def embarked_nominal(self) -> object:
        pass




