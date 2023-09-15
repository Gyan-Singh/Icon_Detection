import pandas as pd
import os

full_path_to_csv = 'C:/Users/gyans/Desktop/New folder (3)/outputs_251-500'

for i in range(0,1001):
    
    check = os.path.isfile(full_path_to_csv + '/' + str(i) +'.csv')
    
    if(check==True):
        print(i,end='\n')
        df = pd.read_csv(full_path_to_csv + '/' + str(i) +'.csv')
        sub_ann = pd.DataFrame(df.iloc[:0, 1:2])
        for col in sub_ann.columns:
            x = col
            
        if x == 'outputs__object__name':
#     print('ho')
            sub_ann = pd.DataFrame(df.iloc[:, 1:2])
            sub_ann['center x'] = ''
            sub_ann['center y'] = ''
            sub_ann['width'] = ''
            sub_ann['height'] = ''

            sub_ann['outputs__object__name'] = df['outputs__object__name'].replace(['star', 'arrow backward', 'arrow forward', 'more', 'menu', 'search', 'close', 'add', 'expand more', 'play', 'check', 'share', 'chat', 'settings', 'info', 'home', 'refresh', 'time', 'emoji', 'edit', 'notifications', 'call', 'pause', 'send', 'delete', 'video cam'], ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25'])

            total_w = df['size__width'][0]
            total_h = df['size__height'][0]
            sub_ann['center x'] = (df['outputs__object__bndbox__xmax'] + df['outputs__object__bndbox__xmin']) / 2
            sub_ann['center x'] = round(sub_ann['center x']/total_w, 7)
            sub_ann['center y'] = (df['outputs__object__bndbox__ymax'] + df['outputs__object__bndbox__ymin']) / 2
            sub_ann['center y'] = round(sub_ann['center y']/total_h, 7)

            sub_ann['width'] = df['outputs__object__bndbox__xmax'] - df['outputs__object__bndbox__xmin']
            sub_ann['width'] = round(sub_ann['width']/total_w, 7)
            sub_ann['height'] = df['outputs__object__bndbox__ymax'] - df['outputs__object__bndbox__ymin']
            sub_ann['height'] = round(sub_ann['height']/total_h,7)
            sub_ann.rename(columns = {'outputs__object__name':'classNumber'}, inplace = True)

        image_name = str(i);

        path_to_save = full_path_to_csv + '/' + image_name + '.txt'

        sub_ann.to_csv(path_to_save, header=False, index=False, sep=' ')