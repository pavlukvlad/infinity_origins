import pygame, os, sys, random, noise, time

part_size = 8

def generate_chunk(x,y):
    parts_data = []
    tr_generate = False
    st_generate = False
    stones=[]
    for y_pos in range(part_size): 
        for x_pos in range(part_size):
            target_x = x * part_size + x_pos
            target_y = y * part_size + y_pos
            tile_type = 0 # nothing

            target_h = int(noise.pnoise1(target_x * 0.1, repeat = 99999999)*5)
            if target_y > 8-target_h and target_y < 8-target_h+4:
                tile_type = 'd1' # dirt
                if random.randint(1,100) == 1 and not st_generate:
                    tile_type='s1'
                    st_generate = True
                    stones = [random.randint(2,4), random.randint(2,4), target_x,target_y,0,0]
                    stones.append(random.randint(1,115))
                    if stones[6] > 0 and stones[6] <=50:
                        stones[6] = 's1'
                    elif stones[6]>50 and stones[6]<=75:
                        stones[6] = 'co'
                    elif stones[6]>75 and stones[6]<=95:
                        stones[6] = 'copo'                    
                    elif stones[6]>95 and stones[6]<=105:
                        stones[6] = 'io'
                    elif stones[6]>105 and stones[6]<=115:
                        stones[6] = 'go'                    
                      

            elif target_y == 8-target_h+4:
                tile_type = 'd3'
            elif target_y > 8-target_h+4:
                tile_type = 's1'
            elif target_y == 8-target_h:
                tile_type = 'gb1' # grass
                if target_y<5:
                    tile_type='gb4'
                

            elif target_y == 8-target_h-1:
                if random.randint(1,4) == 1:
                    tile_type = f'g{random.randint(2,3)}' # plant
                else:
                    if random.randint(1,9) == 1:
                        tile_type = f'f{random.randint(1,2)}'
                        

                if tr_generate:
                    if random.randint(1,2) == 1:
                        tile_type = ['tr1', random.randint(0,4)]
                        tree_height = random.randint(1,9)
                        for p_y in range(tree_height):
                            parts_data.append([[target_x,target_y-(p_y+1)],['tr2', random.randint(0,8)]])
                        if tree_height != 1 and target_y-tree_height-1<5:
                            parts_data.append([[target_x,target_y-tree_height-1],['tr3', 0]])
                        else:
                            parts_data.append([[target_x,target_y-tree_height-1],['tr3', 0]])
                    else:
                        tr_generate = False
                        

                else:
                    if random.randint(1,15) == 1:
                        tile_type = ['tr1', random.randint(0,4)]
                        tree_height = random.randint(1,9)
                        for p_y in range(tree_height):
                            parts_data.append([[target_x,target_y-(p_y+1)],['tr2', random.randint(0,8)]])
                        if tree_height != 1 and target_y-tree_height-1<5:
                            parts_data.append([[target_x,target_y-tree_height-1],['tr3', 0]])
                        else:
                            parts_data.append([[target_x,target_y-tree_height-1],['tr3', 0]])
                        tr_generate = True


            if st_generate:
                if target_x==stones[2]+stones[4]and target_y==stones[3]+stones[5]:
                    if isinstance(tile_type, str)and tile_type!='gb1':
                        if stones[5] == 0:
                            tile_type='d3'
                            parts_data.append([[target_x,target_y+1],stones[6]])
                        else:
                            tile_type=stones[6]
                    stones[4]+=1
                    if stones[4]==stones[0] and stones[5]==stones[1]:
                        st_generate=False
                    if stones[4]==stones[0]:
                        stones[5]+=1
                        stones[4]=0
                
                    


            if tile_type != 0:
                if not [[target_x,target_y],'s1'] in parts_data:
                    parts_data.append([[target_x,target_y],tile_type])

    return parts_data




def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect,movement,tiles):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types


