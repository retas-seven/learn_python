class Editor:

    SUMMARY_KEY_LIST = [
        'isbn',
        'title',
        'publisher',
        'pubdate',
        'cover',
        'author',
    ]

    HANMOTO_KEY_LIST = [
        'datecreated',
        'datemodified',
    ]

    MEASURE_KEY_LIST = [
        'MeasureType',
        'Measurement',
        'MeasureUnitCode',
    ]

    def edit_book(self, book):
        '''
        書籍情報を編集する
        '''
        result_dict = {}
        self.__edit_dict(result_dict, Editor.SUMMARY_KEY_LIST, book.get('summary'))
        self.__edit_dict(result_dict, Editor.HANMOTO_KEY_LIST, book.get('hanmoto'))
        self.__edit_dict(result_dict, Editor.MEASURE_KEY_LIST, book.get('onix').get('DescriptiveDetail').get('Measure')[0])
        return result_dict

    def __edit_dict(self, result_dict, key_list, book_dict):
        '''
        書籍情報の辞書から必要な情報を取得する
        '''
        for key in key_list:
            result_dict[key] = book_dict.get(key)
