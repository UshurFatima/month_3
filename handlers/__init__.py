from aiogram import Router, F

from .shop import shop_router
from .echo import echo_router
from .start import start_router
from .book_survey import survey_router
from .picture import picture_router
from .mashina_kg import mashina_router
from .group_activities import group_router


private_router = Router()

private_router.include_routers(start_router, survey_router,
                               shop_router, picture_router, mashina_router,
                               echo_router)

private_router.message.filter(F.chat.type == 'private')
