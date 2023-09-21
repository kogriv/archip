import logging


logging.basicConfig(level=logging.DEBUG)

# Устанавливаем уровень журналирования для корневого логгера
# logger = logging.getLogger()
logging.root.setLevel(logging.INFO)

# Создаем родительский логгер и устанавливаем его уровень
parent_logger = logging.getLogger('parent_logger')
parent_logger.setLevel(logging.INFO)
parent_logger.propagate = True

# Создаем наследуемый логгер как подлоггер родительского логгера
child_logger = parent_logger.getChild('child_logger')
child_logger.setLevel(logging.WARNING)
child_logger.propagate = True

# Уровень журналирования наследуемого логгера будет унаследован от родительского
effective_level = child_logger.getEffectiveLevel()
#
print("Effective Level for child_logger: {effective_level}")

effective_level = parent_logger.getEffectiveLevel()
print(f"Effective Level for parent_logger: {effective_level}")

# Попробуем зарегистрировать сообщения на разных уровнях
child_logger.debug("This is a debug message")
child_logger.info("This is an info message")
child_logger.warning("This is an warning message")
child_logger.error("This is an error message")
child_logger.critical("This is an critical message")

parent_logger.debug("This is a debug message")
parent_logger.info("This is an info message")
parent_logger.warning("This is an warning message")
parent_logger.error("This is an error message")
parent_logger.critical("This is an critical message")
