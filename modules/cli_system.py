import argparse

def run_parser() -> dict:
    parser = argparse.ArgumentParser (
        prog='Glenth' ,
        description='glenth helps you find the total length of videos in a folder.' ,
    )

    parser.add_argument ('-t', '--type', default='all', choices=['mpg', 'mpeg', 'mp4', 'mov', 'mkv'], help='Choose specific file type (default : all)')
    parser.add_argument ('-d', '--target-dir', default='.', help='choose a directory (default : current directory)')

    args = parser.parse_args()
    all = True
    if args.type != 'all':
        all = False
    return {'type' : args.type, 'target' : args.target_dir, 'all' : all}

