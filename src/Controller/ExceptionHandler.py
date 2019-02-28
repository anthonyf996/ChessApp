class ExceptionHandler:
  def __init__(self, func, exceptions = [], callback = None, fin = None):
    self.func = func
    self.exceptions = exceptions
    self.callback = callback
    self.fin = fin

  def executeFunc(self):
    try:
      return self.func()
    except Exception as e:
      match = False
      for ex in self.exceptions:
        if issubclass( type( e ), type( ex ) ):
          print( e )

          if self.callback is not None:
            self.callback()
            match = True
            break

      if not match:
        raise( e )
    finally:
      if self.fin is not None:
        self.fin()
