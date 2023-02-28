import glob, os
import json
import tqdm

def main():

    scene_jsons = glob.glob('procthor-scene-json/*/*')

    small_houses = []
    large_houses = []
    
    for sc_js in  tqdm.tqdm(scene_jsons):
        with open(sc_js, 'r') as fp:
            scene = json.load(fp)
        
        scene_name = os.path.basename(sc_js).split('.json')[0]
        num_rooms = len(scene['rooms'])
        if num_rooms >= 1 and num_rooms <= 3:
            small_houses.append(scene_name)
        elif num_rooms >= 7 and num_rooms <= 10:
            large_houses.append(scene_name)

    print(len(small_houses))
    print(len(large_houses))

    with open('small_houses.txt', 'w') as fp:
        for sm in small_houses:
            fp.write(sm + '\n')
        
    with open('large_houses.txt', 'w') as fp:
        for lm in large_houses:
            fp.write(lm + '\n')

if __name__ == '__main__':
    main()
