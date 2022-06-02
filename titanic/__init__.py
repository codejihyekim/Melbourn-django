from titanic.templates import TitanicTemplates
from titanic.views import TitanicView
from titanic.models import TitanicModel

if __name__ == '__main__':

    #view = TitanicView()


    while 1:
        menu = input('1.템플릿 2.전처리')
        if menu == '1':
            print('#### 1.템플릿 ####')
            # view.preprocess('test.csv', 'train.csv')
            templates = TitanicTemplates(fname='train.csv')
            templates.visualize()
            break
        elif menu == '2':
            print('#### 2.전처리 ####')
            model = TitanicModel()
            model.learning(train_fname='train.csv', test_fname='test.csv')
            break
