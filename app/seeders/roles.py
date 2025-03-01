class Role:
    """
    Constants for the various roles scoped in the application ecosystem
    """

    ADMINISTRATOR = {
        "name": "administrador",
        "description": "The highest level of authorization in the application"
    }
    CONSUMER = {
        "name": "consumer",
        "description": "Role for the usual user who enters the application, to consume services, activities, etc"
    }
    CLIENT = {
        "name": "service_provisioner",
        "description": "Role for service provisioner, add services, activities, etc"
    }