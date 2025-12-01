from src.core.shared import shared, Shared
from src.core.arg_parser import args, Args, Mode
from src.actions import gather_loop


def main():        

    if shared.mode == Mode.GATHER_DATA:
        dataset_file_path = shared.config.data.save_path
        gather_loop(dataset_file_path)

    
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
    
    
    