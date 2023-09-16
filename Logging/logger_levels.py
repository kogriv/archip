import logging


# Устанавливаем уровень журналирования для корневого логгера
# logger = logging.getLogger()
# logging.root.setLevel(logging.DEBUG)

logging.basicConfig(level=logging.ERROR)

# Создаем родительский логгер и устанавливаем его уровень
parent_logger = logging.getLogger('parent_logger')
parent_logger.setLevel(logging.INFO)

# Создаем наследуемый логгер как подлоггер родительского логгера
# child_logger = parent_logger.getChild('child_logger')
# child_logger.setLevel(logging.DEBUG)

# Уровень журналирования наследуемого логгера будет унаследован от родительского
# effective_level = child_logger.getEffectiveLevel()
#
# print(f"Effective Level for child_logger: {effective_level}")

effective_level = parent_logger.getEffectiveLevel()
print(f"Effective Level for parent_logger: {effective_level}")

# Попробуем зарегистрировать сообщения на разных уровнях
# child_logger.debug("child_logger:: This is a debug message")
# child_logger.info("child_logger:: This is an info message")
# child_logger.warning("child_logger:: This is an warning message")
# child_logger.error("child_logger:: This is an error message")
# child_logger.critical("child_logger:: This is an critical message")

parent_logger.debug("parent_logger:: This is a debug message")
parent_logger.info("parent_logger:: This is an info message")
parent_logger.warning("parent_logger:: This is an warning message")
parent_logger.error("parent_logger:: This is an error message")
parent_logger.critical("parent_logger:: This is an critical message")
