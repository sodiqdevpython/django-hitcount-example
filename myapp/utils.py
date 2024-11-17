from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

def calculate_hit_count(request, obj):
    """
    Ushbu funksiya berilgan obyekt uchun ko'rishlar sonini hisoblaydi
    va saqlaydi.
    """
    # HitCount modelini olish va obyekt uchun ko'rishlar sonini yangilash
    hit_count = get_hitcount_model().objects.get_for_object(obj)
    hit_mixin = HitCountMixin()
    hit_mixin.hit_count(request, hit_count)
