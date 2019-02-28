class GameExitException(Exception):
  def __init__(self, message = "USER_INPUT_QUIT"):
    super().__init__(message)
