from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.shermas.my_data import MainDATA
from utils.db_api.shermas.my_second_data import SecondDATA
from utils.db_api.shermas.user import User


async def add_user(user_id: int, first_name: str, last_name: str, username: str, status: str):
    try:
        user = User(user_id=user_id, first_name=first_name, last_name=last_name, username=username, status=status)
        await user.create()

    except UniqueViolationError:
        print('пользователь не добавлен')


async def fun_for_get_my_data(type_o: str, product_group: str, availability_of_comp: str,
                              new_article: str, old_article: str, name: str, price_in_euro: str,
                              price_in_rub: str, discount_group: str, ean_upc_code: str, net_weight_kg: str,
                              gross_weight_kg: str, length_excluding_packaging_mm: str,
                              width_excluding_packaging_mm: str,
                              height_without_packaging_mm: str, approximate_delivery_time: str, group: str, ):
    try:
        data = MainDATA(type_o=type_o, product_group=product_group, availability_of_comp=availability_of_comp,
                        new_article=new_article, old_article=old_article, name=name, price_in_euro=price_in_euro,
                        price_in_rub=price_in_rub, discount_group=discount_group, ean_upc_code=ean_upc_code,
                        net_weight_kg=net_weight_kg, gross_weight_kg=gross_weight_kg,
                        length_excluding_packaging_mm=length_excluding_packaging_mm,
                        width_excluding_packaging_mm=width_excluding_packaging_mm,
                        height_without_packaging_mm=height_without_packaging_mm,
                        approximate_delivery_time=approximate_delivery_time, group=group, )
        await data.create()

    except UniqueViolationError:
        print('ошибка данных ')


async def fun_get_my_second_data(article: str, description: str, price_eur_without_nds: str, change_article: str):
    try:
        sec_data = SecondDATA(article=article, description=description, price_eur_without_nds=price_eur_without_nds,
                              change_article=change_article)
        await sec_data.create()

    except UniqueViolationError:
        print('пользователь не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):  # Получает данные о пользователе из БД
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def select_my_data(new_article):  # Получает данные из 1 эксельки из БД
    data = await MainDATA.query.where(MainDATA.new_article == new_article).gino.first()
    return data


async def select_my_second_data(article):  # Получает данные из 2 эксельки из БД
    data_plus = await SecondDATA.query.where(SecondDATA.article == article).gino.first()
    return data_plus


async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()
