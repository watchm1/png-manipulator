class Helper:
    @staticmethod
    def StringEmptyChecker(value: str):
        if(value and value.strip):
            return True
        else:
            return False