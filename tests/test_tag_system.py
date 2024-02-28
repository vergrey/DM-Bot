from teg_system.tag_data import TagData
from teg_system.tag_manager import TagsManager


async def test_TagData():
    try:
        tag_data_1 = TagData("test_id")
        tag_data_2 = TagData()  # Проверяем создание объекта без идентификатора
    except Exception as err:
        print(err)
        return False
    
    # Проверяем, что идентификаторы установлены правильно
    if tag_data_1.get_id() == "test_id" and tag_data_2.get_id() is None:
        print("TagData test successful.")
        return True
    else:
        print("TagData test failed.")
        return False

async def test_TagsManager():
    try:
        tags_manager = TagsManager()
    except Exception as err:
        print(err)
        return False
    
    # Создаем несколько объектов TagData для тестирования
    tag_data_1 = TagData("tag1")
    tag_data_2 = TagData("tag2")
    tag_data_3 = TagData("tag3")
    
    # Создаем список тегов и добавляем теги
    tags_list = []
    tags_manager.add(tags_list, tag_data_1)
    tags_manager.add(tags_list, tag_data_2)
    
    # Проверяем, что теги успешно добавлены
    if len(tags_list) == 2 and tag_data_1 in tags_list and tag_data_2 in tags_list:
        print("TagsManager add test successful.")
    else:
        print("TagsManager add test failed.")
        return False
    
    # Удаляем один из тегов
    tags_manager.rm(tags_list, tag_data_2)
    
    # Проверяем, что тег успешно удален
    if len(tags_list) == 1 and tag_data_2 not in tags_list:
        print("TagsManager rm test successful.")
    else:
        print("TagsManager rm test failed.")
        return False
    
    # Сортируем список тегов
    tags_manager.sort_arr(tags_list)
    
    # Проверяем, что список тегов отсортирован по идентификаторам
    sorted_ids = [tag.get_id() for tag in tags_list]
    if sorted_ids == sorted(sorted_ids):
        print("TagsManager sort_arr test successful.")
        return True
    else:
        print("TagsManager sort_arr test failed.")
        return False