class Role:
    """
    Constants for the various roles scoped in the application ecosystem
    """

    ADMINISTRATOR = {
        "name": "administrador",
        "description": "The highest level of authorization in the application"
    }
    CLIENT = {
        "name": "client",
        "description": "Role for the usual user who enters the application, to consume services, activities, etc"
    }
    PROFESSIONAL = {
        "name": "professional",
        "description": "Role for the professional who provides services, activities, etc"
    }