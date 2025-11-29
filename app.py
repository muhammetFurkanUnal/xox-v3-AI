from src.core.shared import shared, Shared
from src.core.arg_parser import args, Args, Mode
from src.actions import DataActs, train, TestActs
from src.models import AutoencoderManager


def main():        

    if shared.mode == Mode.LOAD_DATA:
        # write your data procedure here
        pass

    
    elif shared.mode == Mode.TRAIN:
        # write your train procedure here
        pass

        
    elif shared.mode == Mode.TEST:
        # write your test procedure here
        pass


    elif shared.mode == Mode.DEBUG:
        # write your debugging procedure here
        pass

    
    
if __name__ == "__main__":
    main()
    
    
    