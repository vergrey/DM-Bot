# Документация по файлу `bin_file_data.py`

## `BinFileData.__init__`<br>
Инициализация объекта FileWork.<br>
<br>**Args:**<br>
file_path (str): Путь к файлу.<br>
<br>**Attributes:**<br>
path (str): Полный путь к файлу.<br>
data (object): Данные файла.<br>
cached (bool): Флаг указывающий, кэшированы ли данные.<br>
file_hash (str): Хэш файла.<br>
<br>
## `BinFileData.create_file`<br>
Создание директории и файла, если они не были созданы ранее.<br>
<br>**Returns:**<br>
bool: Возвращает True если файл был создан, иначе False<br>
<br>
## `BinFileData.load_data`<br>
Загрузка данных с использованием кэширования и проверки хеша файла.<br>
<br>**Returns:**<br>
object: Загруженные данные файла.<br>
<br>**Raises:**<br>
FileNotFoundError: Если файл не найден.<br>
<br>
## `BinFileData.save_data`<br>
Сохранение данных.<br>
<br>
## `BinFileData.data`<br>
Возвращает текущие данные класса<br>
<br>**Returns:**<br>
any: Данные, записанные в классе<br>
<br>
Записывает в data класса кастомные данные<br>
<br>**Args:**<br>
data (any): Данные для записи в класс<br>
<br>