# Authentication & Authorization models
from app.user.model import User
from app.role.model import Rol  # User roles and permissions
from app.client_user.model import ClientUser  # Client/Professional-specific user extensions

# Service-related models
from app.category.model import Category  # Service categories taxonomy
from app.client_services.model import ClientService  # Main services offered
from app.user_service_get.model import UserServiceGet  # Services acquired by users

# Client/Professional support models
from app.client_frequently_asked_questions.model import ClientFrequentlyAskedQuestions
from app.client_review_services.model import ClientReviewService  # Service feedback system

# Financial models
from app.history_payment.model import HistoryPayment  # Payment transaction records
from app.user_history_payment.model import UserHistoryPayment  # User-specific payment history

# Shared utilities
from app.file.model import File  # File storage system