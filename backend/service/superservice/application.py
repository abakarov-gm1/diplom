
# Проверка данных от aplication id если его нет в бд то кидаем запрос на получение новой записи сохраняем в бд


def get_full_applications(all_applications):
    for i in all_applications:
        print(i["Id"])





# curl -X POST --location 'http://vo-online-test.citis.ru:8100/api/api/cls/get' \
# --header 'Content-Type: application/json' \
# --header 'Session-Key: skey+1da1681ae54fa849d2d3640bd6dcf33bd8b01acd+2025-06-13_19-38' \
# --data '{
#   "ogrn": "1020502629180",
#   "kpp": "057201001",
#   "cls": "DirectionCls"
# }'