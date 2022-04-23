from rest_framework.routers import SimpleRouter
from .views import WorkoutViewset

router = SimpleRouter()
router.register('workouts', WorkoutViewset)

urlpatterns = router.urls