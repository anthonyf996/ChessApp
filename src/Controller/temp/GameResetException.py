class GameResetException(Exception):
  def __init__(self, message = "USER_INPUT_RESET"):
    super().__init__(message)
