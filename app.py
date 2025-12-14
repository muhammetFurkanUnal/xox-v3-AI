from src.core.shared import shared, Shared
from src.core.arg_parser import args, Args, Mode
from src.actions import *


def main():        

    if shared.mode == Mode.GATHER_DATA:
        dataset_file_path = f"{shared.config.data.gather_save_folder}/dataset_v1.csv"
        gather_loop(dataset_file_path)


    elif shared.mode == Mode.CLEAN_DATA:
        dataset_file_path = f"{shared.config.data.gather_save_folder}/dataset_v1.csv"
        df = import_raw_dataset(dataset_file_path)
        df = find_target(df)
        
        winner_x, winner_o, draw_x, draw_o = XO_draw_split(df)

        winner_x = drop_extras(winner_x)
        winner_o = drop_extras(winner_o)
        draw_x = drop_extras(draw_x)
        draw_o = drop_extras(draw_o)

        dataset_x = merge_dfs([
            winner_x,
            draw_x,
            switch_OX(draw_o),
            switch_OX(winner_o)
        ])
        
        dataset_o = merge_dfs([
            winner_o,
            draw_o,
            switch_OX(draw_x),
            switch_OX(winner_x)
        ])

        dataset_x_path = f"{shared.config.data.clean_save_folder}/x_dataset_v1.csv"
        dataset_o_path = f"{shared.config.data.clean_save_folder}/o_dataset_v1.csv"
        save_clean_dataset(dataset_x, dataset_x_path)
        save_clean_dataset(dataset_o, dataset_o_path)


    
    elif shared.mode == Mode.AUGMENT_DATA:
        clean_dataset_path_x = f"{shared.config.data.clean_save_folder}/x_dataset_v1.csv"
        clean_dataset_path_o = f"{shared.config.data.clean_save_folder}/o_dataset_v1.csv"
        clean_x = import_clean_dataset(clean_dataset_path_x)
        clean_o = import_clean_dataset(clean_dataset_path_o)

        for i in range(len(clean_x)):
            for name, func in augmentations.items():
                augmented_x = func(tuple(clean_x.iloc[i]))
                path = f"{shared.config.data.aug_save_folder}/x_dataset_v1.csv"
                append_aug_dataset(augmented_x, path)

                augmented_o = func(tuple(clean_o.iloc[i]))
                path = f"{shared.config.data.aug_save_folder}/o_dataset_v1.csv"
                append_aug_dataset(augmented_o, path)



    elif shared.mode == Mode.TRAIN:
        start_training()

        
    elif shared.mode == Mode.TEST:
        # write your test procedure here
        pass


    elif shared.mode == Mode.DEBUG:
        aug_dataset_path_x = f"{shared.config.data.aug_save_folder}/o_dataset_v1.csv"
        aug_x = import_clean_dataset(aug_dataset_path_x)

        # clean_dataset_path_x = f"{shared.config.data.clean_save_folder}/x_dataset_v1.csv"
        # clean_x = import_clean_dataset(clean_dataset_path_x)

        for i in range(10):
            board = aug_x.iloc[2000 + i]
            print()
            print(board["target"])
            visualize_row(board)

        # dataset_file_path = f"{shared.config.data.gather_save_folder}/dataset_v1.csv"
        # df = import_raw_dataset(dataset_file_path)
        # winner_x, winner_o, draw_x, draw_o = XO_draw_split(df)
        # winner_x = find_target(winner_x)
        # winner_o = find_target(winner_o)
        # draw_x = find_target(draw_x)
        # draw_o = find_target(draw_o)

        # for i in range(10):
        #         board = winner_x.iloc[0 + i]
        #         print()
        #         print("ID: ", board["game_id"])
        #         print(board["target"])
        #         visualize_row(board)

    
    

if __name__ == "__main__":
    main()
    
    
    